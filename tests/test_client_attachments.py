import io
import cgi

from .helpers import *


class TestClientAttachments(ClientTestCase):

    def test_attachments_get_attachment(self):
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
        self.assertEqual(self.client.attachments.get_attachment('5678'), res['data'])

    def test_attachments_find_by_task(self):
        res = {
            "data": [
                { "id": 5678, "name": "Background.png" },
                { "id": 9012, "name": "New Design Draft.pdf" }
            ]
        }
        responses.add(GET, 'http://app/tasks/1234/attachments', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.attachments.find_by_task('1234'), res['data'])

    def test_attachments_create_on_task(self):
        res = { "data": { "id": 5678, "name": "file.txt" } }
        responses.add(POST, 'http://app/tasks/1337/attachments', status=200, body=json.dumps(res), match_querystring=True)

        self.assertEqual(self.client.attachments.create_on_task('1337', 'file content', 'file name', 'file content-type'), res['data'])

        request_content_type, pdict = cgi.parse_header(responses.calls[0].request.headers['Content-Type'])
        self.assertEqual(request_content_type, 'multipart/form-data')

        content_file = io.BytesIO(responses.calls[0].request.body)
        multipart = cgi.parse_multipart(content_file, { 'boundary':  bytes(pdict['boundary'], "UTF-8") })
        self.assertEqual(multipart['file'][0], bytes('file content', 'UTF-8'))
        # TODO: verify filename and content-type, possibly using a different multipart decoder
