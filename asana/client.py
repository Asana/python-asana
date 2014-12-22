from . import session
from . import resources
from . import error

from types import ModuleType, ClassType

import requests
import json

RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType):
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

    def request(self, method, path, **kwargs):
        response = getattr(self.session, method)(self.url(path), auth=self.auth, **kwargs)
        if response.status_code in STATUS_MAP:
            raise STATUS_MAP[response.status_code](response.json())
        else:
            return response.json()['data']

    def get(self, path, query):
        return self.request('get', path, params=query)

    def post(self, path, data):
        return self.request('post', path, data=json.dumps(data), headers={'content-type': 'application/json'})

    def put(self, path, data):
        return self.request('put', path, data=json.dumps(data), headers={'content-type': 'application/json'})

    def delete(self, path):
        return self.request('delete', path)


    @classmethod
    def basic_auth(Klass, apiKey):
        return Klass(auth=requests.auth.HTTPBasicAuth(apiKey, ''))

    @classmethod
    def oauth(Klass, **kwargs):
        return Klass(session.AsanaOAuth2Session(**kwargs))
