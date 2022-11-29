from .helpers import *

class TestClientProjects(ClientTestCase):
    def test_projects_create_project(self):
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
        self.assertEqual(self.client.projects.create_project(req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_projects_get_project(self):
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy",
                "notes": "These are things we want to purchase."
            }
        }
        responses.add(GET, 'http://app/projects/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.get_project('1331'), res['data'])

    def test_projects_update_project(self):
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
        self.assertEqual(self.client.projects.update_project('1331', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_projects_delete_project(self):
        res = { "data": {} }
        responses.add(DELETE, 'http://app/projects/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.delete_project('1331'), res['data'])

    def test_projects_get_projects_for_workspace(self):
        res = {
            "data": [
                { "id": 1331, "name": "Things to buy" },
                { "id": 14641, "name": "Cat Stuff" }
            ]
        }
        responses.add(GET, 'http://app/workspaces/14916/projects', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.get_projects_for_workspace('14916'), res['data'])

    def test_projects_get_projects(self):
        res = {
            "data": [
                { "id": 1331, "name": "Things to buy" },
                { "id": 14641, "name": "Cat Stuff" }
            ]
        }
        responses.add(GET, 'http://app/projects', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.get_projects(), res['data'])

    def test_projects_add_custom_field_setting_for_project(self):
        req = {
            "data": {
                "custom_field":124578,
                "is_important": true
            }
        }
        res = {
            "data": {}
        }

        responses.add(POST, 'http://app/projects/1331/addCustomFieldSetting', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.add_custom_field_setting_for_project('1331', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)


    def test_projects_remove_custom_field_setting_for_project(self):
        req = {
            "data": {
                "custom_field":124578,
            }
        }
        res = {
            "data": {}
        }

        responses.add(POST, 'http://app/projects/1331/removeCustomFieldSetting', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.remove_custom_field_setting_for_project('1331', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)
