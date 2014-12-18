from . import dispatcher
from . import resources

from types import ModuleType

resourceClasses = {}
for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType):
        resourceClasses[name] = module.__dict__[name.capitalize()]

class Client:

    def __init__(self, dispatcher=None):
        self.dispatcher = dispatcher
        for name, Klass in resourceClasses.items():
            setattr(self, name, Klass(dispatcher))

    @classmethod
    def basic_auth(Klass, apiKey):
        return Klass(dispatcher.Dispatcher((apiKey, '')))
