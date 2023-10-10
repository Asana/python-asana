from .helpers import *

class TestClientWorkspaces(ClientTestCase):

    def test_workspaces_get_workspaces(self):
        res = { "data": [{ "id": 1337, "name": "My Favorite Workspace" }]}
        responses.add(GET, 'http://app/workspaces', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.workspaces.get_workspaces(), res['data'])

    def test_workspaces_get_workspace(self):
        res = { "data": [{ "id": 1337, "name": "My Favorite Workspace" }]}
        responses.add(GET, 'http://app/workspaces/222', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.workspaces.get_workspace('222'), res['data'])

    def test_workspaces_update_workspace(self):
        req = { "data": { "name": "Everyone's Favorite Workspace" } }
        res = { "data": { "id": 1337, "name": "Everyone's Favorite Workspace" } }
        responses.add(PUT, 'http://app/workspaces/1337', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.workspaces.update_workspace('1337', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)
