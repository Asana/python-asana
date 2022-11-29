from .helpers import *

class TestClientTasks(ClientTestCase):

    def test_tasks_create_task(self):
        req = {
            "data": {
                "assignee": 1235,
                "followers": [5678],
                "name": "Hello, world.",
                "notes": "How are you today?",
                "workspace": 14916
            }
        }
        res = {
            "data": {
                "assignee": { "id": 1235, "name": "Tim Bizarro" },
                "assignee_status": "inbox",
                "completed": false,
                "completed_at": null,
                "created_at": "2012-02-22T02:06:58.158Z",
                "due_on": null,
                "followers": [{ "id": 5678, "name": "Greg Sanchez" } ],
                "id": 1001,
                "modified_at": "2012-02-22T02:06:58.158Z",
                "name": "Hello, world!",
                "notes": "How are you today?",
                "parent": null,
                "projects": [{ "id": 14641, "name": "Cat Stuff" }],
                "workspace": { "id": 14916, "name": "My Favorite Workspace" }
            }
        }
        responses.add(POST, 'http://app/tasks', status=201, body=json.dumps(res), match_querystring=True)

        self.assertEqual(self.client.tasks.create_task(req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_get_task(self):
        res = {
            "data": {
                "assignee": { "id": 1234, "name": "Tim Bizarro" },
                "created_at": "2012-02-22T02:06:58.158Z"
            }
        }
        responses.add(GET, 'http://app/tasks/1001', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.get_task('1001'), res['data'])

    def test_tasks_get_tasks_for_project(self):
        res = {
            "data": [
                { "id": 2001, "name": "Catnip" },
                { "id": 2002, "name": "Kitty litter" }
            ]
        }
        responses.add(GET, 'http://app/projects/1331/tasks', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.get_tasks_for_project('1331'), res['data'])

    def test_tasks_update_task(self):
        req = { "data": { "assignee": "me" } }
        res = {
            "data": {
                "assignee": { "id": 1234, "name": "Tim Bizarro" },
                "id": 1001
            }
        }
        responses.add(PUT, 'http://app/tasks/1001', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.update_task('1001', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_delete_task(self):
        res = { "data": {} }
        responses.add(DELETE, 'http://app/tasks/1001', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.delete_task('1001'), res['data'])

    def test_tasks_get_tasks(self):
        res = {
            "data": [
                { "id": 1248, "name": "Buy catnip" },
                { "id": 24816, "name": "Reflect on role of kittens in society" }
            ]
        }
        responses.add(GET, 'http://app/tasks?workspace=14916&assignee=me', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.get_tasks({ 'workspace': 14916, 'assignee': 'me' }), res['data'])

    def test_tasks_add_subtask(self):
        req = {
            "data": {
                "assignee": 1235,
                "followers": [5678],
                "name": "Tell Luke",
                "notes": "He's going to be upset."
            }
        }
        res = {
            "data": {
                "assignee": { "id": 1235, "name": "Darth Vader" },
                "assignee_status": "inbox",
                "completed": false,
                "completed_at": null,
                "created_at": "2012-02-22T02:06:58.158Z",
                "due_on": null,
                "followers": [{ "id": 5678, "name": "Emperor Palpatine" } ],
                "id": 1001,
                "modified_at": "2012-02-22T02:06:58.158Z",
                "name": "Tell Luke",
                "notes": "He's going to be upset.",
                "parent": { "id": 2272, "name": "Tell kids I am their father." },
                "projects": [],
                "workspace": { "id": 14916, "name": "Star Wars" }
            }
        }
        responses.add(POST, 'http://app/tasks/2272/subtasks', status=201, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.add_subtask('2272', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_subtasks(self):
        res = {
            "data": [
                { "id": 5005, "name": "Steal Underwear" },
                { "id": 6709, "name": "???" },
                { "id": 9812, "name": "Profit" }
            ]
        }
        responses.add(GET, 'http://app/tasks/7331/subtasks', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.subtasks(7331), res['data'])

    def test_tasks_set_parent(self):
        req = { "data": { "parent": 1331 } }
        res = {
            "data": {
                "id": 2272,
                "name": "Tell Luke",
                "parent": [{ "id": 1331, "name": "Tell kids I am their father" }]
            }
        }
        responses.add(POST, 'http://app/tasks/2272/setParent', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.set_parent('2272', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_projects(self):
        res = {
            "data": [
                { "id": 1331, "name": "Things To Buy" },
                { "id": 14641, "name": "Cat Stuff" }
            ]
        }
        responses.add(GET, 'http://app/tasks/1001/projects', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.projects('1001'), res['data'])

    def test_tasks_add_project(self):
        req = { "data": { "project": 14641 } }
        res = { "data": {} }
        responses.add(POST, 'http://app/tasks/1001/addProject', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.add_project('1001', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_remove_project(self):
        req = { "data": { "project": 14641 } }
        res = { "data": {} }
        responses.add(POST, 'http://app/tasks/1001/removeProject', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.remove_project('1001', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_tags(self):
        res = {
            "data": [
                { "id": 1331, "name": "orange" },
                { "id": 1771, "name": "fluffy" }
            ]
        }
        responses.add(GET, 'http://app/tasks/1001/tags', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.tags('1001'), res['data'])

    def test_tasks_1001_addTag(self):
        req = { "data": { "tag": 1771 } }
        res = { "data": {} }
        responses.add(POST, 'http://app/tasks/1001/addTag', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.add_tag('1001', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_removeTag(self):
        req = { "data": { "tag": 1771 } }
        res = { "data": {} }
        responses.add(POST, 'http://app/tasks/1001/removeTag', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.remove_tag('1001', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_add_followers(self):
        req = { "data": { "followers": [1235] } }
        res = {
            "data": {
                "followers": [{ "id": 1235, "name": "Darth Vader" }],
                "id": 1001
            }
        }
        responses.add(POST, 'http://app/tasks/1001/addFollowers', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.add_followers('1001', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_remove_followers(self):
        req = { "data": { "followers": [1235] } }
        res = { "data": { "followers": [], "id": 1001 } }
        responses.add(POST, 'http://app/tasks/1001/removeFollowers', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.remove_followers('1001', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_get_tasks_for_tag(self):
        res = {
            "data": [
                { "id": 2001, "name": "Catnip" },
                { "id": 2002, "name": "Kitty litter" }
            ]
        }
        responses.add(GET, 'http://app/tags/1331/tasks', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.get_tasks_for_tag('1331'), res['data'])

    def test_tasks_custom_field_data(self):
        res = {
            "data": {
                "id": 1001,
                "name": "Hello, world!",
                "completed": false,
                "custom_fields": [
                    {
                        "id": 124578,
                        "name": "Priority",
                        "type": "enum",
                        "enum_value": {
                          "id": 789,
                          "name": "Low",
                          "enabled": true,
                          "color": "blue"
                        }
                    }
                ]
            }
        }
        responses.add(GET, 'http://app/tasks/1001', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.get_task('1001'), res['data'])
