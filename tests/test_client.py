
import unittest
import asana

import requests
import requests_mock

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = asana.Client()

        self.adapter = requests_mock.Adapter()
        self.client.ROOT_URL = 'mock://app'
        self.client.session.mount('mock', self.adapter)

    def test_users_me(self):
        self.adapter.register_uri('GET', 'mock://app/users/me', json={ 'data': { 'foo': 'bar' }})
        me = self.client.users.me()
        self.assertEqual(me['foo'], 'bar')

    def test_users_not_found(self):
        self.adapter.register_uri('GET', 'mock://app/users/1234', status_code=404, json={ 'data': { 'foo': 'bar' }})
        self.assertRaises(asana.error.NotFoundError, self.client.users.find_by_id, (1234))
