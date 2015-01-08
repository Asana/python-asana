from .helpers import *

class TestClientProjects(ClientTestCase):
    def test_projects_create(self):
        req = {
            "data": {
                "name": "Things to Buy",
                "notes": "These are things we want to purchase.",
                "workspace": 14916
            }
        }
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy",
                "notes": "These are things we want to purchase."
            }
        }
        responses.add(POST, 'http://app/projects', status=201, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.create(req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_projects_find_by_id(self):
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy",
                "notes": "These are things we want to purchase."
            }
        }
        responses.add(GET, 'http://app/projects/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.find_by_id(1331), res['data'])

    def test_projects_update(self):
        req = {
            "data": {
                "notes": "These are things we NEED to purchase."
            }
        }
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy",
                "notes": "These are things we NEED to purchase."
            }
        }
        responses.add(PUT, 'http://app/projects/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.update(1331, req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_projects_delete(self):
        res = { "data": {} }
        responses.add(DELETE, 'http://app/projects/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.delete(1331), res['data'])

    def test_projects_find_by_workspace(self):
        res = {
            "data": [
                { "id": 1331, "name": "Things to buy" },
                { "id": 14641, "name": "Cat Stuff" }
            ]
        }
        responses.add(GET, 'http://app/workspaces/14916/projects', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.find_by_workspace(14916), res['data'])

    def test_projects_find_all(self):
        res = {
            "data": [
                { "id": 1331, "name": "Things to buy" },
                { "id": 14641, "name": "Cat Stuff" }
            ]
        }
        responses.add(GET, 'http://app/projects', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.find_all(), res['data'])
