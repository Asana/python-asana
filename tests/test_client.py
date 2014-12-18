
import unittest
import asana

import requests
import requests_mock

class TestClient(unittest.TestCase):

    def setUp(self):
        self.dispatcher = asana.Dispatcher(None)
        self.client = asana.Client(self.dispatcher)

        self.adapter = requests_mock.Adapter()
        self.dispatcher.rootURL = 'mock://app'
        self.dispatcher.session.mount('mock', self.adapter)

    def test_hello_world(self):
        self.assertEqual(1,1)

    def test_users_me(self):
        self.adapter.register_uri('GET', 'mock://app/users/me', json={ 'data': { 'foo': 'bar' }})
        me = self.client.users.me()
        self.assertEqual(me['foo'], 'bar')
