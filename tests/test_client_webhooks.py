from .helpers import *


class TestClientWebhooks(ClientTestCase):

    def setUp(self):
        ClientTestCase.setUp(self)
        self.webhook_data = {
            "id": 222,
            "resource": {
                "id": 111,
                "name": "the resource"
            },
            "target": "https://foo/123",
            "active": true
        }

    def test_webhooks_create(self):
        req = { "resource": 111, "target": "https://foo/123" }
        res = { "data": self.webhook_data }
        responses.add(POST, 'http://app/webhooks', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.webhooks.create(req), self.webhook_data)

    def test_webhooks_get_all(self):
        req = { "workspace": 1337 }
        res = { "data": [self.webhook_data] }
        responses.add(GET, 'http://app/webhooks?workspace=1337', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.webhooks.get_all(req), [self.webhook_data])

    def test_webhooks_get_by_id(self):
        res = { "data": self.webhook_data }
        responses.add(GET, 'http://app/webhooks/222', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.webhooks.get_by_id(222), self.webhook_data)

    def test_delete_by_id(self):
        res = { "data": {} }
        responses.add(DELETE, 'http://app/webhooks/222', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.webhooks.delete_by_id(222), {})
