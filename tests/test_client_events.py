from .helpers import *

class TestClientEvents(ClientTestCase):

    def test_events_get(self):
        res = {
            "data": [
                {
                    "action": "changed",
                    "created_at": "2013-08-21T18:20:37.972Z",
                    "parent": null,
                    "resource": { "id": 1337, "name": "My Task" },
                    "type": "task",
                    "user": { "id": 1123, "name": "Tom Bizarro" }
                },
                {
                    "action": "changed",
                    "created_at": "2013-08-21T18:22:45.421Z",
                    "parent": null,
                    "resource": { "id": 1338, "name": "My Other Task" },
                    "type": "task",
                    "user": { "id": 1428, "name": "Greg Sanchez" }
                }
            ],
            "sync": "edfc0896b370b7a479886d316131bf5c:0"
        }
        responses.add(GET, 'http://app/events?resource=14321&sync=de4774f6915eae04714ca93bb2f5ee81%3A3', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.events.get({ 'resource': 14321, 'sync': 'de4774f6915eae04714ca93bb2f5ee81:3' }), res)

    def test_project_events_get_invalid_token(self):
        res = {
            "message": "Sync token invalid or too old. If you are attemping to keep resources in sync, you must re-fetch the full dataset for this query now.",
            "sync": "edfc0896b370b7a479886d316131bf5c:0"
        }
        responses.add(GET, 'http://app/events?resource=3214312&sync=de4774f6915eae04714ca93bb2f5ee81%3A3', status=412, body=json.dumps(res), match_querystring=True)
        # responses.add(GET, 'http://app/project/3214312/events?sync=de4774f6915eae04714ca93bb2f5ee81%3A3', status=412, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.events.get({ 'resource': 3214312, 'sync': 'de4774f6915eae04714ca93bb2f5ee81:3' }), res)
