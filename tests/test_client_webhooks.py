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

    def test_webhooks_create_webhook(self):
        req = { "resource": 111, "target": "https://foo/123" }
        res = { "data": self.webhook_data }
        responses.add(POST, 'http://app/webhooks', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.webhooks.create_webhook(req), self.webhook_data)

    def test_webhooks_get_webhooks(self):
        req = { "workspace": 1337 }
        res = { "data": [self.webhook_data] }
        responses.add(GET, 'http://app/webhooks?workspace=1337', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.webhooks.get_webhooks(req), [self.webhook_data])

    def test_webhooks_get_webhook(self):
        res = { "data": self.webhook_data }
        responses.add(GET, 'http://app/webhooks/222', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.webhooks.get_webhook('222'), self.webhook_data)

    def test_webhooks_delete_webhook(self):
        res = { "data": {} }
        responses.add(DELETE, 'http://app/webhooks/222', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.webhooks.delete_webhook('222'), {})
