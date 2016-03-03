from types import ModuleType
import json
import platform
import time

import requests

from . import error, resources, session, __version__
from .page_iterator import CollectionPageIterator

try:
    import urllib.parse as urlparse
except ImportError:
    import urllib as urlparse

# Create a dict of resource classes
RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType) and name.capitalize() in module.__dict__:
        RESOURCE_CLASSES[name] = module.__dict__[name.capitalize()]

# Create a mapping of status codes to classes
STATUS_MAP = {}
for name, Klass in error.__dict__.items():
    if isinstance(Klass, type) and issubclass(Klass, error.AsanaError):
        STATUS_MAP[Klass().status] = Klass


class Client:
    """Asana client class"""

    DEFAULTS = {
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

    CLIENT_OPTIONS = set(DEFAULTS.keys())
    QUERY_OPTIONS = set(['limit', 'offset', 'sync'])
    REQUEST_OPTIONS = set(['headers', 'params', 'data', 'files', 'verify'])
    API_OPTIONS = set(['pretty', 'fields', 'expand'])

    ALL_OPTIONS = CLIENT_OPTIONS | QUERY_OPTIONS | REQUEST_OPTIONS | API_OPTIONS

    def __init__(self, session=None, auth=None, **options):
        """Initialize a Client object with session, optional auth handler, and options"""
        self.session = session or requests.Session()
        self.auth = auth
        # merge the provided options (if any) with the global DEFAULTS
        self.options = _merge(self.DEFAULTS, options)
        # intializes each resource, injecting this client object into the constructor
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
                response = getattr(self.session, method)(url, auth=self.auth, **request_options)
                if response.status_code in STATUS_MAP:
                    raise STATUS_MAP[response.status_code](response)
                elif response.status_code >= 500 and response.status_code < 600:
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

    def _handle_retryable_error(self, e, retry_count):
        """Determines how long to sleep before retrying based on the type of RetryableAsanaError."""
        if isinstance(e, error.RateLimitEnforcedError):
            time.sleep(e.retry_after)
        else:
            time.sleep(self.RETRY_DELAY * (self.RETRY_BACKOFF ** retry_count))

    def get(self, path, query, **options):
        """Parses GET request options and dispatches a request."""
        api_options = self._parse_api_options(options, query_string=True)
        query_options = self._parse_query_options(options)
        parameter_options = self._parse_parameter_options(options)
        query = _merge(query_options, api_options, parameter_options, query)  # options in the query takes precendence
        return self.request('get', path, params=query, **options)

    def get_collection(self, path, query, **options):
        """Parses GET request options for a collection endpoint and dispatches a request."""
        options = self._merge_options(options)
        if options['iterator_type'] == 'items':
            return CollectionPageIterator(self, path, query, options).items()
        if options['iterator_type'] is None:
            return self.get(path, query, **options)
        raise Exception('Unknown value for "iterator_type" option: ' + str(options['iterator_type']))

    def post(self, path, data, **options):
        """Parses POST request options and dispatches a request."""
        parameter_options = self._parse_parameter_options(options)
        body = {
            'data': _merge(parameter_options, data),  # values in the data body takes precendence
            'options': self._parse_api_options(options)
        }
        return self.request('post', path, data=body, headers={'content-type': 'application/json'}, **options)

    def put(self, path, data, **options):
        """Parses PUT request options and dispatches a request."""
        parameter_options = self._parse_parameter_options(options)
        body = {
            'data': _merge(parameter_options, data),  # values in the data body takes precendence
            'options': self._parse_api_options(options)
        }
        return self.request('put', path, data=body, headers={'content-type': 'application/json'}, **options)

    def delete(self, path, data, **options):
        """Dispatches a DELETE request."""
        return self.request('delete', path, **options)

    def _merge_options(self, *objects):
        """Merges one or more options objects with client's options and returns a new options object"""
        return _merge(self.options, *objects)

    def _parse_query_options(self, options):
        """Selects query string options out of the provided options object"""
        return self._select_options(options, self.QUERY_OPTIONS)

    def _parse_parameter_options(self, options):
        """Selects all unknown options (not query string, API, or request options)"""
        return self._select_options(options, self.ALL_OPTIONS, invert=True)

    def _parse_api_options(self, options, query_string=False):
        """Selects API string options out of the provided options object and formats for either request body (default) or query string."""
        api_options = self._select_options(options, self.API_OPTIONS)
        if query_string:
            # Prefix all options with "opt_"
            query_api_options = {}
            for key in api_options:
                # Transform list/tuples into comma separated list
                if isinstance(api_options[key], (list, tuple)):
                    query_api_options['opt_' + key] = ','.join(api_options[key])
                else:
                    query_api_options['opt_' + key] = api_options[key]
            return query_api_options
        else:
            return api_options

    def _parse_request_options(self, options):
        """Select and formats options to be passed to the 'requests' library's request methods"""
        request_options = self._select_options(options, self.REQUEST_OPTIONS)
        if 'params' in request_options:
            params = request_options['params']
            for key in params:
                if isinstance(params[key], bool):
                    params[key] = json.dumps(params[key])
        if 'data' in request_options:
            # remove empty 'options':
            if 'options' in request_options['data'] and len(request_options['data']['options']) == 0:
                del request_options['data']['options']
            # serialize 'data' to JSON, requests doesn't do this automatically:
            request_options['data'] = json.dumps(request_options['data'])
        return request_options

    def _select_options(self, options, keys, invert=False):
        """Selects the provided keys (or everything except the provided keys) out of an options object"""
        options = self._merge_options(options)
        result = {}
        for key in options:
            if (invert and key not in keys) or (not invert and key in keys):
                result[key] = options[key]
        return result

    def _add_version_header(self, options):
        """Add the client lib version header to the request."""
        headers = options.setdefault('headers', {})
        headers['X-Asana-Client-Lib'] = self._versionHeader()

    _cached_version_header = None

    def _versionHeader(self):
        """Generate the client version header to send on each request."""
        if not self._cached_version_header:
            self._cached_version_header = urlparse.urlencode(
                self._versionValues())
        return self._cached_version_header

    def _versionValues(self):
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
        """Construct an Asana Client with a Basic Auth API key"""
        return Klass(auth=requests.auth.HTTPBasicAuth(apiKey, ''))

    @classmethod
    def access_token(Klass, accessToken):
        """Construct an Asana Client with a Personal Access Token"""
        return Klass(session.AsanaOAuth2Session(token={'access_token': accessToken}))

    @classmethod
    def oauth(Klass, **kwargs):
        """Construct an Asana Client with OAuth credentials ('client_id' and 'client_secret' or 'token')"""
        return Klass(session.AsanaOAuth2Session(**kwargs))


def _merge(*objects):
    """Merge one or more objects into a new object"""
    result = {}
    [result.update(obj) for obj in objects]
    return result
