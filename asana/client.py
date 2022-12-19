from types import ModuleType
import json
import platform
import time
import string
import warnings

import requests

from . import error, resources, session, __version__
from .page_iterator import CollectionPageIterator
import urllib.parse as urlparse

# Create a dict of resource classes
RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    classified_name = string.capwords(name, '_').replace('_', '')
    if classified_name == "BatchApi":
        classified_name = "BatchAPI"
    if classified_name == "AuditLogApi":
        classified_name = "AuditLogAPI"
    if isinstance(module, ModuleType) and classified_name in module.__dict__:
        RESOURCE_CLASSES[name] = module.__dict__[classified_name]

# Create a mapping of status codes to classes
STATUS_MAP = {}
for name, Klass in error.__dict__.items():
    if isinstance(Klass, type) and issubclass(Klass, error.AsanaError):
        STATUS_MAP[Klass().status] = Klass


class Client(object):
    """Asana client class"""

    DEFAULT_OPTIONS = {
        'base_url': 'https://app.asana.com/api/1.0',
        'item_limit': None,
        'page_size': 50,
        'poll_interval': 5,
        'max_retries': 5,
        'full_payload': False,
        'iterator_type': 'items'
    }

    RETRY_DELAY = 1.0
    RETRY_BACKOFF = 2.0

    CLIENT_OPTIONS = set(DEFAULT_OPTIONS.keys())
    QUERY_OPTIONS = {'limit', 'offset', 'sync'}
    REQUEST_OPTIONS = {'headers', 'params', 'data', 'files', 'verify',
                       'timeout'}
    API_OPTIONS = {'pretty', 'fields', 'expand', 'client_name'}

    LOG_ASANA_CHANGE_WARNINGS = True

    ALL_OPTIONS = (
        CLIENT_OPTIONS | QUERY_OPTIONS | REQUEST_OPTIONS | API_OPTIONS)

    def __init__(self, session=None, auth=None, **options):
        """A :class:`Client` object for interacting with Asana's API.

        A Client object with session, optional auth handler, and options.

        """
        self.session = session or requests.Session()
        self.auth = auth
        self.headers = options.pop('headers', {})
        # merge the provided options (if any) with the global DEFAULTS
        self.options = _merge(self.DEFAULT_OPTIONS, options)
        # intializes each resource, injecting this client object into the
        # constructor
        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(self))

    def request(self, method, path, **options):
        """Dispatches a request to the Asana HTTP API"""
        options = self._merge_options(options)
        url = options['base_url'] + path
        retry_count = 0
        request_options = self._parse_request_options(options)
        self._add_version_header(request_options)
        while True:
            try:
                response = getattr(self.session, method)(
                    url, auth=self.auth, **request_options)
                self._log_asana_change_header(request_options['headers'], response.headers)
                if response.status_code in STATUS_MAP:
                    raise STATUS_MAP[response.status_code](response)
                elif 500 <= response.status_code < 600:
                    # Any unhandled 500 is a server error.
                    raise error.ServerError(response)
                else:
                    if options['full_payload']:
                        return response.json()
                    else:
                        return response.json()['data']
            except error.RetryableAsanaError as e:
                if retry_count < options['max_retries']:
                    self._handle_retryable_error(e, retry_count)
                    retry_count += 1
                else:
                    raise e

    def _log_asana_change_header(self, req_headers, res_headers):
        if self.LOG_ASANA_CHANGE_WARNINGS:
            change_header_key = None

            for key in res_headers:
                if key.lower() == 'asana-change':
                    change_header_key = key

            if change_header_key is not None:
                accounted_for_flags = []

                # Grab the request's asana-enable flags
                for reqHeader in req_headers:
                    if reqHeader.lower() == 'asana-enable':
                        for flag in req_headers[reqHeader].split(','):
                            accounted_for_flags.append(flag)
                    elif reqHeader.lower() == 'asana-disable':
                        for flag in req_headers[reqHeader].split(','):
                            accounted_for_flags.append(flag)

                changes = res_headers[change_header_key].split(',')

                for unsplit_change in changes:
                    change = unsplit_change.split(';')

                    name = None
                    info = None
                    affected = None

                    for unsplit_field in change:
                        field = unsplit_field.split('=')

                        field[0] = field[0].strip()
                        if field[0].strip() == 'name':
                            name = field[1].strip()
                        elif field[0].strip() == 'info':
                            info = field[1].strip()
                        elif field[0].strip() == 'affected':
                            affected = field[1].strip()

                    # Only show the error if the flag was not in the request's asana-enable header
                    if (name not in accounted_for_flags) & (affected == 'true'):
                        message = 'This request is affected by the "' + name + \
                        '" deprecation. Please visit this url for more info: ' + info + \
                        '\n' + 'Adding "' + name + '" to your "Asana-Enable" or ' + \
                        '"Asana-Disable" header will opt in/out to this deprecation ' + \
                        'and suppress this warning.'

                        warnings.warn(message)


    def _handle_retryable_error(self, e, retry_count):
        """Sleep based on the type of :class:`RetryableAsanaError`"""
        if isinstance(e, error.RateLimitEnforcedError):
            time.sleep(e.retry_after)
        else:
            time.sleep(self.RETRY_DELAY * (self.RETRY_BACKOFF ** retry_count))

    def get(self, path, query, **options):
        """Parses GET request options and dispatches a request."""
        api_options = self._parse_api_options(options, query_string=True)
        query_options = self._parse_query_options(options)
        parameter_options = self._parse_parameter_options(options)

        # options in the query takes precendence
        query = _merge(query_options, api_options, parameter_options, query)
        return self.request('get', path, params=query, **options)

    def get_collection(self, path, query, **options):
        """Get a collection from a collection endpoint.

        Parses GET request options for a collection endpoint and dispatches a
        request.

        """
        options = self._merge_options(options)
        if options['iterator_type'] == 'items':
            return CollectionPageIterator(self, path, query, options).items()
        if options['iterator_type'] is None:
            return self.get(path, query, **options)
        raise Exception('Unknown value for "iterator_type" option: {}'.format(
            str(options['iterator_type'])))

    def post(self, path, data, **options):
        """Parses POST request options and dispatches a request."""
        parameter_options = self._parse_parameter_options(options)
        body = {
            # values in the data body takes precendence
            'data': _merge(parameter_options, data),
            'options': self._parse_api_options(options)
        }
        headers = _merge(
            {'content-type': 'application/json'},
            options.pop('headers', {})
        )
        return self.request('post', path, data=body, headers=headers, **options)

    def put(self, path, data, **options):
        """Parses PUT request options and dispatches a request."""
        parameter_options = self._parse_parameter_options(options)
        body = {
            # values in the data body takes precendence
            'data': _merge(parameter_options, data),
            'options': self._parse_api_options(options)
        }
        headers = _merge(
            {'content-type': 'application/json'},
            options.pop('headers', {})
        )
        return self.request('put', path, data=body, headers=headers, **options)

    def delete(self, path, data, **options):
        """Dispatches a DELETE request."""
        return self.request('delete', path, **options)

    def _merge_options(self, *objects):
        """Merge option objects with the client's object.

        Merges one or more options objects with client's options and returns a
        new options object.

        """
        return _merge(self.options, *objects)

    def _parse_query_options(self, options):
        """Select query string options out of the provided options object"""
        return self._select_options(options, self.QUERY_OPTIONS)

    def _parse_parameter_options(self, options):
        """Select all unknown options.

        Select all unknown options (not query string, API, or request
        options)

        """
        return self._select_options(options, self.ALL_OPTIONS, invert=True)

    def _parse_api_options(self, options, query_string=False):
        """Select API options out of the provided options object.

        Selects API string options out of the provided options object and
        formats for either request body (default) or query string.

        """
        api_options = self._select_options(options, self.API_OPTIONS)
        if query_string:
            # Prefix all options with "opt_"
            query_api_options = {}
            for key in api_options:
                # Transform list/tuples into comma separated list
                if isinstance(api_options[key], (list, tuple)):
                    query_api_options[
                        'opt_' + key] = ','.join(api_options[key])
                else:
                    query_api_options[
                        'opt_' + key] = api_options[key]
            return query_api_options
        else:
            return api_options

    def _parse_request_options(self, options):
        """Select request options out of the provided options object.


        Select and formats options to be passed to the 'requests' library's
        request methods.

        """
        request_options = self._select_options(options, self.REQUEST_OPTIONS)
        if 'params' in request_options:
            params = request_options['params']
            for key in params:
                if isinstance(params[key], bool):
                    params[key] = json.dumps(params[key])
        if 'data' in request_options:
            # remove empty 'options':
            if 'options' in request_options['data'] and (
                    len(request_options['data']['options']) == 0):
                del request_options['data']['options']
            # serialize 'data' to JSON, requests doesn't do this automatically:
            request_options['data'] = json.dumps(request_options['data'])

        headers = self.headers.copy()
        headers.update(request_options.get('headers', {}))
        request_options['headers'] = headers
        return request_options

    def _select_options(self, options, keys, invert=False):
        """Select the provided keys out of an options object.


        Selects the provided keys (or everything except the provided keys) out
        of an options object.

        """
        options = self._merge_options(options)
        result = {}
        for key in options:
            if (invert and key not in keys) or (not invert and key in keys):
                result[key] = options[key]
        return result

    def _add_version_header(self, options):
        """Add the client lib version header to the request."""
        headers = options.setdefault('headers', {})
        headers['X-Asana-Client-Lib'] = self._version_header()

    _cached_version_header = None

    def _version_header(self):
        """Generate the client version header to send on each request."""
        if not self._cached_version_header:
            self._cached_version_header = urlparse.urlencode(
                self._version_values())
        return self._cached_version_header

    def _version_values(self):
        """Generate the values to go in the client version header."""
        return {
            'language': 'Python',
            'version': __version__,
            'language_version': platform.python_version(),
            'os': platform.system(),
            'os_version': platform.release()
        }

    @classmethod
    def basic_auth(Klass, apiKey):
        """DEPRECATED: this is only present for backwards-compatibility.

        This will be removed in the future; for new apps, prefer the
        `access_token` method.

        Construct an Asana Client using a Personal Access Token as if it
        were an old (removed) Asana API Key.
        """
        return Klass(auth=requests.auth.HTTPBasicAuth(apiKey, ''))

    @classmethod
    def access_token(Klass, accessToken):
        """Construct an Asana Client with a Personal Access Token"""
        return Klass(
            session.AsanaOAuth2Session(token={'access_token': accessToken}))

    @classmethod
    def oauth(Klass, **kwargs):
        """Construct an Asana Client with Oauth credentials.

        Construct an Asana Client with OAuth credentials ('client_id' and
        'client_secret' or 'token').

        """
        return Klass(session.AsanaOAuth2Session(**kwargs))


def _merge(*objects):
    """Merge one or more objects into a new object"""
    result = {}
    [result.update(obj) for obj in objects]
    return result
