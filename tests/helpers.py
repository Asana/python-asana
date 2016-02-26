import json
import unittest

import asana
import requests
import responses
from six import add_metaclass, next
from responses import GET, PUT, POST, DELETE

# Define JSON primitives so we can just copy in JSON:
false = False
true = True
null = None


def create_decorating_metaclass(decorators, prefix='test_'):
    class DecoratingMethodsMetaclass(type):
        def __new__(cls, name, bases, namespace):
            namespace_items = tuple(namespace.items())
            for key, val in namespace_items:
                if key.startswith(prefix) and callable(val):
                    for dec in decorators:
                        val = dec(val)
                    namespace[key] = val
            return type.__new__(cls, name, bases, dict(namespace))

    return DecoratingMethodsMetaclass


# TestCase subclass that automatically decorates test methods with
# responses.activate and sets up a client instance
@add_metaclass(create_decorating_metaclass((responses.activate,)))
class ClientTestCase(unittest.TestCase):

    def setUp(self):
        self.client = asana.Client(
            base_url='http://app',
            # no delay when polling to speed up tests
            poll_interval=0,
            # disable iterator and limit to match existing tests for now
            iterator_type=None,
        )
