from .helpers import *

class TestClientWorkspaces(ClientTestCase):

    def test_workspaces_find_all(self):
        res = { "data": [{ "id": 1337, "name": "My Favorite Workspace" }]}
        responses.add(GET, 'http://app/workspaces', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.workspaces.find_all(), res['data'])

    def test_workspaces_update(self):
        req = { "data": { "name": "Everyone's Favorite Workspace" } }
        res = { "data": { "id": 1337, "name": "Everyone's Favorite Workspace" } }
        responses.add(PUT, 'http://app/workspaces/1337', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.workspaces.update(1337, req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_workspaces_typeahead(self):
        req = { "data": { "type": "user", "query": "Greg" }}
        res = { "data": [{ "id": 999, "name": "Greg Sanchez" }]}
        responses.add(GET, 'http://app/workspaces/1337/typeahead?type=user&query=Greg', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.workspaces.typeahead(1337, req['data']), res['data'])
