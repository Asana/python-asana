from .helpers import *

class TestClientAttachments(ClientTestCase):

    def test_attachments_find_by_id(self):
        res = {
            "data": {
                "created_at": "",
                "download_url": "https://www.dropbox.com/s/1234567890abcdef/Screenshot.png?dl=1",
                "host": "dropbox",
                "id": 5678,
                "name": "Screenshot.png",
                "parent": { "id": 1337, "name": "My Task" },
                "view_url": "https://www.dropbox.com/s/1234567890abcdef/Screenshot.png"
            }
        }
        responses.add(GET, 'http://app/attachments/5678', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.attachments.find_by_id(5678), res['data'])

    def test_attachments_find_by_task(self):
        res = {
            "data": [
                { "id": 5678, "name": "Background.png" },
                { "id": 9012, "name": "New Design Draft.pdf" }
            ]
        }
        responses.add(GET, 'http://app/tasks/1234/attachments', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.attachments.find_by_task(1234), res['data'])

    @unittest.skip("attachments.upload not yet implemented")
    def test_attachments_upload(self):
        res = { "data": { "id": 5678, "name": "file.txt" } }
        responses.add(GET, 'http://app/tasks/1337/attachments', status=200, body=json.dumps(res), match_querystring=True)
