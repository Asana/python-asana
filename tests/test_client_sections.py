import json

import responses

from .helpers import ClientTestCase, GET, DELETE, POST, PUT


class TestClientSections(ClientTestCase):

    def test_sections_create_section_for_project(self):
        resp = {
            "data": {
                "id": 2001,
                "name": "High Priority:",
                "created_at": "2017-01-17T22:06:39.249Z",
                "project": {
                    "id": 1331,
                    "name": "Things to buy"
                }
            }
        }

        responses.add(
            POST, 'http://app/projects/1331/sections', status=200,
            body=json.dumps(resp), match_querystring=True)
        self.assertEqual(
            self.client.sections.create_section_for_project('1331'), resp['data'])

    def test_sections_get_sections_for_project(self):
        resp = {
            "data": [
                {
                    "id": 2001,
                    "name": "High Priority:"
                },
                {
                    "id": 2002,
                    "name": "Low Priority:"
                },
            ]
        }

        responses.add(
            GET, 'http://app/projects/1331/sections', status=200,
            body=json.dumps(resp), match_querystring=True)
        self.assertEqual(
            self.client.sections.get_sections_for_project('1331'), resp['data'])

    def test_sections_get_section(self):
        resp = {
            "data": {
                "id": 2001,
                "name": "High Priority:",
                "created_at": "2017-01-17T22:06:39.249Z",
                "project": {
                    "id": 1331,
                    "name": "Things to buy"
                }
            }
        }

        responses.add(
            GET, 'http://app/sections/2001', status=200,
            body=json.dumps(resp), match_querystring=True)
        self.assertEqual(
            self.client.sections.get_section('2001'), resp['data'])

    def test_sections_update_section(self):
        req = {
            "name": "High Priority, renamed:"
        }
        resp = {
            "data": {
                "id": 2001,
                "name": "High Priority, renamed:",
                "created_at": "2017-01-17T22:06:39.249Z",
                "project": {
                    "id": 1331,
                    "name": "Things to buy"
                }
            }
        }

        responses.add(
            PUT, 'http://app/sections/2001', status=200,
            body=json.dumps(resp), match_querystring=True)
        self.assertEqual(
            self.client.sections.update_section('2001', req), resp['data'])

    def test_sections_delete_section(self):
        resp = {
            "data": {}
        }

        responses.add(
            DELETE, 'http://app/sections/2001', status=200,
            body=json.dumps(resp), match_querystring=True)
        self.assertEqual(
            self.client.sections.delete_section('2001'), resp['data'])

    def test_sections_insert_section_for_project(self):
        resp = {
            "data": {
                "section": 2001,
                "project": 1331,
                "before_section": 1330
            }
        }

        responses.add(
            POST, 'http://app/projects/1331/sections/insert', status=200,
            body=json.dumps(resp), match_querystring=True)
        self.assertEqual(
            self.client.sections.insert_section_for_project('1331'), resp['data'])
