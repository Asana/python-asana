
import asana
import requests
import responses
import unittest
import json

from six import next
from responses import GET, PUT, POST, DELETE

# Define JSON primitives so we can just copy in JSON:
false = False
true = True
null = None

# From https://github.com/dropbox/responses/issues/31#issuecomment-63165210
from inspect import getmembers, isfunction, ismethod
def decallmethods(decorator, prefix='test_'):
    def dectheclass(cls):
        for name, m in getmembers(cls, predicate=lambda x: isfunction(x) or ismethod(x)):
            if name.startswith(prefix):
                setattr(cls, name, decorator(m))
        return cls
    return dectheclass

# TestCase subclass that automatically decorates test methods with responses.activate and sets up a client instance
class ClientTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        decallmethods(responses.activate)(cls)

    def setUp(self):
        self.client = asana.Client(
            base_url='http://app',
            poll_interval=0, # no delay when polling to speed up tests
            iterator_type=None, # disable iterator and limit to match existing tests for now
        )
