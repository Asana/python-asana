from . import session
from . import resources
from . import error

from types import ModuleType
import requests
import json
import time

RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType) and name.capitalize() in module.__dict__:
        RESOURCE_CLASSES[name] = module.__dict__[name.capitalize()]

STATUS_MAP = {}
for name, Klass in error.__dict__.items():
    if isinstance(Klass, type) and issubclass(Klass, error.AsanaError):
        STATUS_MAP[Klass().status] = Klass

class Client:

    DEFAULT_LIMIT = 10

    DEFAULTS = {
        'base_url': 'https://app.asana.com/api/1.0',
        'limit': None,# DEFAULT_LIMIT,
        'poll_interval': 5,
        'rate_limit_retry': True,
        'full_payload': False
    }

    def __init__(self, session=None, auth=None, **options):
        self.session = session or requests.Session()
        self.auth = auth
        self.options = _merge(self.DEFAULTS, options)
        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(self))

    def request(self, method, path, **options):
        options = self._merge_options(options)
        url = options['base_url'] + path
        request_options = self._parse_request_options(options)
        while True:
            try:
                response = getattr(self.session, method)(url, auth=self.auth, **request_options)
                if response.status_code in STATUS_MAP:
                    raise STATUS_MAP[response.status_code](response)
                else:
                    if options['full_payload']:
                        return response.json()
                    else:
                        return response.json()['data']
            except error.RateLimitEnforcedError as e:
                if options['rate_limit_retry']:
                    time.sleep(e.retry_after)
                else:
                    raise e

    def get(self, path, query, **options):
        api_options = self._parse_api_options(options, query_string=True)
        query_options = self._parse_query_options(options)
        query = _merge(query_options, api_options, query) # options in the query takes precendence
        return self.request('get', path, params=query, **options)

    def post(self, path, data, **options):
        body = { 'data': data }
        api_options = self._parse_api_options(options)
        if len(api_options) > 0:
            body['options'] = api_options
        return self.request('post', path, data=json.dumps(body), headers={'content-type': 'application/json'}, **options)

    def put(self, path, data, **options):
        body = { 'data': data }
        api_options = self._parse_api_options(options)
        if len(api_options) > 0:
            body['options'] = api_options
        return self.request('put', path, data=json.dumps(body), headers={'content-type': 'application/json'}, **options)

    def delete(self, path, data, **options):
        return self.request('delete', path, **options)

    def get_iterator(self, path, query, **options):
        options = self._merge_options(options, { 'full_payload': True })
        limit = query.get('limit', options['limit'] or self.DEFAULT_LIMIT)
        query = _merge(query.copy(), { 'limit': limit })
        while True:
            result = self.get(path, query, **options)
            for item in result['data']:
                yield item
            next_page = result.get('next_page', None)
            if next_page is None:
                return
            else:
                options['offset'] = next_page['offset']

    def _merge_options(self, *objects):
        return _merge(self.options, *objects)

    def _parse_query_options(self, options):
        return self._select_options(options, ['limit', 'offset', 'sync'])

    def _parse_api_options(self, options, query_string=False):
        api_options = self._select_options(options, ['pretty', 'fields', 'expand'])
        if query_string:
            query_api_options = {}
            for key in api_options:
                if isinstance(api_options[key], (list, tuple)):
                    query_api_options['opt_'+key] = ','.join(api_options[key])
                else:
                    query_api_options['opt_'+key] = api_options[key]
            return query_api_options
        else:
            return api_options

    def _parse_request_options(self, options):
        request_options = self._select_options(options, ['headers', 'params', 'data'])
        if 'params' in request_options:
            params = request_options['params']
            for key in params:
                if isinstance(params[key], bool):
                    params[key] = json.dumps(params[key])
        return request_options

    def _select_options(self, options, keys):
        options = self._merge_options(options)
        return { key: options[key] for key in keys if key in options }

    @classmethod
    def basic_auth(Klass, apiKey):
        return Klass(auth=requests.auth.HTTPBasicAuth(apiKey, ''))

    @classmethod
    def oauth(Klass, **kwargs):
        return Klass(session.AsanaOAuth2Session(**kwargs))

def _merge(*objects):
    result = {}
    [result.update(obj) for obj in objects]
    return result
