import json

import responses

from .helpers import ClientTestCase, GET, DELETE, POST, PUT


class TestClientOrganizationExports(ClientTestCase):
    def test_organization_exports_find_by_id(self):
        resp = {
            "data": {
                "id": 1234,
                "created_at": '2012-02-22T02:06:58.147Z',
                "download_url":
                    'https://asana-export.s3.amazonaws.com/export-1.json.gz',
                "state": "pending",
                "organization": {
                    "id": 14916, "name": "My Workspace"
                }
            }
        }

        responses.add(
            GET, 'http://app/organization_exports/1234', status=200,
            body=json.dumps(resp), match_querystring=True)
        self.assertEqual(
            self.client.organization_exports.find_by_id(1234), resp['data'])

    def test_organization_exports_create(self):
        resp = {
            "data": {
                "organization": 14916
            }
        }

        responses.add(
            POST, 'http://app/organization_exports', status=200,
            body=json.dumps(resp), match_querystring=True)
        self.assertEqual(
            self.client.organization_exports.create(), resp['data'])
