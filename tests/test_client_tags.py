from .helpers import *

class TestClientTags(ClientTestCase):
    def test_tags_create(self):
        req = { "data": { "name": "fluffy", "workspace": 14916 } }
        res = { "data": { "id": 1771, "name": "fluffy" } }
        responses.add(POST, 'http://app/tags', status=201, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tags.create(req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tags_find_by_id(self):
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy",
                "notes": "These are things we want to purchase."
            }
        }
        responses.add(GET, 'http://app/tags/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tags.find_by_id(1331), res['data'])

    def test_tags_update(self):
        req = { "data": { "name": "Things to Sell" } }
        res = { "data": { "id": 1331, "name": "Things to Sell" } }
        responses.add(PUT, 'http://app/tags/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tags.update(1331, req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tags_find_by_workspace(self):
        res = {
            "data": [
                { "id": 1331, "name": "Things to buy" },
                { "id": 14641, "name": "Cat Stuff" }
            ]
        }
        responses.add(GET, 'http://app/workspaces/14916/tags', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tags.find_by_workspace(14916), res['data'])
