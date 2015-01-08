from .helpers import *

class TestClientStories(ClientTestCase):

    def test_stories_find_by_task(self):
        res = {
            "data": [
                {
                    "created_at": "2011-12-21T23:23:01.259Z",
                    "created_by": { "id": 5678, "name": "Greg Sanchez" },
                    "id": 2001,
                    "text": "added to Things To Buy",
                    "type": "system"
                },
                {
                    "created_at": "2012-01-02T21:32:40.112Z",
                    "created_by": { "id": 1234, "name": "Tim Bizarro" },
                    "id": 2002,
                    "text": "Again? Wow, we really go through this stuff fast.",
                    "type": "comment"
                }
            ]
        }
        responses.add(GET, 'http://app/tasks/1001/stories', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.stories.find_by_task(1001), res['data'])

    def test_stories_find_by_id(self):
        res = {
            "data": {
                "created_at": "2012-02-22T02:06:58.147Z",
                "created_by": { "id": 1123, "name": "Mittens" },
                "id": 2001,
                "source": "web",
                "target": { "id": 1234, "name": "Buy catnip" },
                "text": "Yes, please!",
                "type": "comment"
            }
        }
        responses.add(GET, 'http://app/stories/2001', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.stories.find_by_id(2001), res['data'])

    def test_stories_create_on_task(self):
        req = { "data": { "text": "This is a very nice comment." } }
        res = {
            "data": {
                "created_at": "2011-12-21T23:23:01.259Z",
                "created_by": { "id": 5678, "name": "Greg Sanchez" },
                "id": 2001,
                "source": "api",
                "target": { "id": 1001, "name": "Buy catnip" },
                "text": "This is a very nice comment.",
                "type": "comment"
            }
        }
        responses.add(POST, 'http://app/tasks/1001/stories', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.stories.create_on_task(1001, req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)
