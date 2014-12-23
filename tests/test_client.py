
import unittest
import asana

import requests
import requests_mock

FAKE_USER = {
    "id": 5678,
    "name": "Greg Sanchez"
}

FAKE_USER_FULL = {
    "email": "gsanchez@example.com",
    "id": 5678,
    "name": "Greg Sanchez",
    "workspaces": [{
        "id": 1337,
        "name": "My Favorite Workspace"
    }]
}

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = asana.Client()
        self.adapter = requests_mock.Adapter()
        self.client.ROOT_URL = 'mock://app'
        # self.client.ROOT_URL = 'http://localhost:8081'
        self.client.session.mount('mock', self.adapter)

    def test_users_me(self):
        self.adapter.register_uri('GET', 'mock://app/users/me', status_code=200, json={ 'data': FAKE_USER_FULL })
        self.assertEqual(self.client.users.me(), FAKE_USER_FULL)

    def test_users_find_by_id(self):
        self.adapter.register_uri('GET', 'mock://app/users/1', status_code=200, json={ 'data': FAKE_USER_FULL })
        self.assertEqual(self.client.users.find_by_id(1), FAKE_USER_FULL)

    def test_users_find_all(self):
        self.adapter.register_uri('GET', 'mock://app/users', status_code=200, json={ 'data': [FAKE_USER] })
        self.assertEqual(self.client.users.find_all(), [FAKE_USER])

    def test_users_find_by_workspace(self):
        self.adapter.register_uri('GET', 'mock://app/workspaces/1/users', status_code=200, json={ 'data': [FAKE_USER] })
        self.assertEqual(self.client.users.find_by_workspace(1), [FAKE_USER])

    def test_users_not_found(self):
        self.adapter.register_uri('GET', 'mock://app/users/2', status_code=404, json={ "errors":[{"message":"user: Unknown object: 2"}]} )
        self.assertRaises(asana.error.NotFoundError, self.client.users.find_by_id, (2))

    def test_events(self):
        # TODO: query string matching isn't working: 'mock://app/events?resource=14321&sync=de4774f6915eae04714ca93bb2f5ee81%3A3'
        self.adapter.register_uri('GET', 'mock://app/events', json={
            "data": [{ "action": "changed" }],
            "sync": "edfc0896b370b7a479886d316131bf5c:0"
        })
        self.assertEqual(self.client.events.get({ 'resource': 14321, 'sync': 'de4774f6915eae04714ca93bb2f5ee81:3' }), {
            "data": [{ "action": "changed" }],
            "sync": "edfc0896b370b7a479886d316131bf5c:0"
        })
