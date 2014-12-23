from . import session
from . import resources
from . import error

from types import ModuleType, ClassType
import requests
import json

RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType) and name.capitalize() in module.__dict__:
        RESOURCE_CLASSES[name] = module.__dict__[name.capitalize()]

STATUS_MAP = {}
for name, Klass in error.__dict__.items():
    if isinstance(Klass, (type, ClassType)) and issubclass(Klass, error.AsanaError):
        STATUS_MAP[Klass().status] = Klass

class Client:

    ROOT_URL = 'https://app.asana.com/api/1.0'

    def __init__(self, session=None, auth=None):
        self.session = session or requests.Session()
        self.auth = auth
        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(self))

    def url(self, path):
        return self.ROOT_URL + path

    def request(self, method, path, dispatch_options={}, **kwargs):
        response = getattr(self.session, method)(self.url(path), auth=self.auth, **kwargs)
        if response.status_code in STATUS_MAP:
            raise STATUS_MAP[response.status_code](response.json())
        else:
            if dispatch_options.get('fullPayload', False):
                return response.json()
            else:
                return response.json()['data']

    def get(self, path, query, dispatch_options={}):
        return self.request('get', path, params=query, dispatch_options=dispatch_options)

    def post(self, path, data, dispatch_options={}):
        return self.request('post', path, data=json.dumps(data), headers={'content-type': 'application/json'}, dispatch_options=dispatch_options)

    def put(self, path, data, dispatch_options={}):
        return self.request('put', path, data=json.dumps(data), headers={'content-type': 'application/json'}, dispatch_options=dispatch_options)

    def delete(self, path, dispatch_options={}):
        return self.request('delete', path, dispatch_options=dispatch_options)


    @classmethod
    def basic_auth(Klass, apiKey):
        return Klass(auth=requests.auth.HTTPBasicAuth(apiKey, ''))

    @classmethod
    def oauth(Klass, **kwargs):
        return Klass(session.AsanaOAuth2Session(**kwargs))
