from .helpers import *

class TestClientUsers(ClientTestCase):

    def test_users_me(self):
        res = {
            "data": { "email":"sanchez@...", "id": 999, "name":"Greg Sanchez" }
        }
        responses.add(GET, 'http://app/users/me', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.users.get_user('me'), res['data'])

    def test_users_get_user(self):
        res = {
            "data": {
                "email": "gsanchez@example.com",
                "id": 5678,
                "name": "Greg Sanchez",
                "workspaces": [{ "id": 1337, "name": "My Favorite Workspace" }]
            }
        }
        responses.add(GET, 'http://app/users/5678', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.users.get_user('5678'), res['data'])

    def test_users_get_users(self):
        res = {
            "data": [
                { "email": "tbizarro@example.com", "id": 1234, "name": "Tim Bizarro" },
                { "email": "gsanchez@example.com", "id": 5678, "name": "Greg Sanchez" }
            ]
        }
        # responses.add(GET, 'http://app/users?opt_fields=name,email', status=200, body=json.dumps(res), match_querystring=True)
        responses.add(GET, 'http://app/users', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.users.get_users(), res['data'])

    def test_users_get_users_for_workspace(self):
        res = {
            "data": [
                { "id": 5678, "name": "Greg Sanchez" }
            ]
        }
        responses.add(GET, 'http://app/workspaces/1337/users', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.users.get_users_for_workspace('1337'), res['data'])
