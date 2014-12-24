
import asana
import requests
import responses
import unittest
import json
from responses import GET, PUT, POST, DELETE

# From https://github.com/dropbox/responses/issues/31#issuecomment-63165210
from inspect import getmembers, isfunction, ismethod
def decallmethods(decorator, prefix='test_'):
    def dectheclass(cls):
        for name, m in getmembers(cls, predicate=lambda x: isfunction(x) or ismethod(x)):
            if name.startswith(prefix):
                setattr(cls, name, decorator(m))
        return cls
    return dectheclass

FAKE_USER = {
    "id": 5678,
    "name": "Greg Sanchez"
}

FAKE_USER_FULL = {
    "email": "gsanchez@example.com",
    "id": 5678,
    "name": "Greg Sanchez",
    "workspaces": [{
        "id": 1337,
        "name": "My Favorite Workspace"
    }]
}

# Define JSON primitives so we can just copy in JSON:
false = False
true = True
null = None

@decallmethods(responses.activate)
class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = asana.Client()
        self.client.ROOT_URL = 'http://app'

    def test_users_me_not_authorized(self):
        res = {
            "errors": [
                { "message": "Not Authorized" }
            ]
        }
        responses.add(GET, 'http://app/users/me', status=401, body=json.dumps(res), match_querystring=True)
        self.assertRaises(asana.error.NoAuthorizationError, self.client.users.me)

    def test_tasks_find_all_invalid_request(self):
        res = {
            "errors": [
                { "message": "workspace: Missing input" }
            ]
        }
        responses.add(GET, 'http://app/tasks', status=400, body=json.dumps(res), match_querystring=True)
        self.assertRaises(asana.error.InvalidRequestError, self.client.tasks.find_all)

    def test_users_me_server_error(self):
        res = {
            "errors": [
                {
                    "message": "Server Error",
                    "phrase": "6 sad squid snuggle softly"
                }
            ]
        }
        responses.add(GET, 'http://app/users/me', status=500, body=json.dumps(res), match_querystring=True)
        self.assertRaises(asana.error.ServerError, self.client.users.me)

    def test_users_find_by_id_not_found(self):
        res = {
            "errors": [
                { "message": "user: Unknown object: 1234124312341" }
            ]
        }
        responses.add(GET, 'http://app/users/1234', status=404, body=json.dumps(res), match_querystring=True)
        self.assertRaises(asana.error.NotFoundError, self.client.users.find_by_id, (1234))

    def test_users_find_by_id_forbidden(self):
        res = {
            "errors": [
                { "message": "user: Forbidden" }
            ]
        }
        responses.add(GET, 'http://app/users/1234', status=403, body=json.dumps(res), match_querystring=True)
        self.assertRaises(asana.error.ForbiddenError, self.client.users.find_by_id, (1234))

    def test_users_me(self):
        res = {
            "data": { "email":"sanchez@...", "id": 999, "name":"Greg Sanchez" }
        }
        responses.add(GET, 'http://app/users/me', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.users.me(), res['data'])

    @unittest.skip("pretty option not yet implemented")
    def test_option_pretty(self):
        res = {
            "data": { "email": "sanchez@...", "id": 999, "name": "Greg Sanchez" }
        }
        responses.add(GET, 'http://app/users/me?opt_pretty', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.users.me(pretty=True), res['data'])

    @unittest.skip("fields option not yet implemented")
    def test_option_fields(self):
        res = {
            "data": { "name": "Make a list", "notes": "Check it twice!", "id": 1224 }
        }
        responses.add(GET, 'http://app/tasks/1224?opt_fields=name,notes', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.tasks.find_by_id.me(fields=('name','notes')), res['data'])

    @unittest.skip("expand option not yet implemented")
    def test_option_expand(self):
        res = {
            "data": {
                "id": 1001,
                "projects": [
                    {
                        "archived": false,
                        "created_at": "",
                        "followers": [],
                        "modified_at": "",
                        "notes": "",
                        "id": 1331,
                        "name": "Things to buy"
                    }
                ]
                # ...
            }
        }
        responses.add(PUT, 'http://app/tasks/1001', status=200, body=json.dumps(res), match_querystring=True)
        # -d "assignee=1234" \
        # -d "options.expand=%2Aprojects%2A"

    @unittest.skip("pagination not yet implemented")
    def test_pagination(self):
        res = {
            "data": [
                { "id": 1000, "name": "Task 1" }
            ],
            "next_page": {
                "offset": "yJ0eXAiOiJKV1QiLCJhbGciOiJIRzI1NiJ9",
                "path": "/tasks?project=1337&limit=5&offset=yJ0eXAiOiJKV1QiLCJhbGciOiJIRzI1NiJ9",
                "uri": "https://app.asana.com/api/1.0/tasks?project=1337&limit=5&offset=yJ0eXAiOiJKV1QiLCJhbGciOiJIRzI1NiJ9"
            }
        }
        responses.add(GET, 'http://app/tasks?project=1337&limit=5&offset=eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9', status=200, body=json.dumps(res), match_querystring=True)

    def test_users_find_by_id(self):
        res = {
            "data": {
                "email": "gsanchez@example.com",
                "id": 5678,
                "name": "Greg Sanchez",
                "workspaces": [{ "id": 1337, "name": "My Favorite Workspace" }]
            }
        }
        responses.add(GET, 'http://app/users/5678', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.users.find_by_id(5678), res['data'])

    def test_users_find_all(self):
        res = {
            "data": [
                { "email": "tbizarro@example.com", "id": 1234, "name": "Tim Bizarro" },
                { "email": "gsanchez@example.com", "id": 5678, "name": "Greg Sanchez" }
            ]
        }
        # responses.add(GET, 'http://app/users?opt_fields=name,email', status=200, body=json.dumps(res), match_querystring=True)
        responses.add(GET, 'http://app/users', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.users.find_all(), res['data'])

    def test_users_find_by_workspace(self):
        res = {
            "data": [
                { "id": 5678, "name": "Greg Sanchez" }
            ]
        }
        responses.add(GET, 'http://app/workspaces/1337/users', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.users.find_by_workspace(1337), res['data'])

    def test_tasks_create(self):
        req = {
            "assignee": 1235,
            "followers": [5678],
            "name": "Hello, world.",
            "notes": "How are you today?",
            "workspace": 14916
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

        self.assertEqual(self.client.tasks.create(req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_find_by_id(self):
        res = {
            "data": {
                "assignee": { "id": 1234, "name": "Tim Bizarro" },
                "created_at": "2012-02-22T02:06:58.158Z"
            }
        }
        responses.add(GET, 'http://app/tasks/1001', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.find_by_id(1001), res['data'])

    def test_tasks_update(self):
        req = { "assignee": "me" }
        res = {
            "data": {
                "assignee": { "id": 1234, "name": "Tim Bizarro" },
                "id": 1001
            }
        }
        responses.add(PUT, 'http://app/tasks/1001', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.update(1001, req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_delete(self):
        res = { "data": {} }
        responses.add(DELETE, 'http://app/tasks/1001', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.delete(1001), res['data'])

    def test_tasks_find_all(self):
        res = {
            "data": [
                { "id": 1248, "name": "Buy catnip" },
                { "id": 24816, "name": "Reflect on role of kittens in society" }
            ]
        }
        responses.add(GET, 'http://app/tasks?workspace=14916&assignee=me', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.find_all({ 'workspace': 14916, 'assignee': 'me' }), res['data'])

    def test_tasks_add_subtask(self):
        req = {
            "assignee": 1235,
            "followers": [5678],
            "name": "Tell Luke",
            "notes": "He's going to be upset."
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
        self.assertEqual(self.client.tasks.add_subtask(2272, req), res['data'])
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
        req = { "parent": 1331 }
        res = {
            "data": {
                "id": 2272,
                "name": "Tell Luke",
                "parent": [{ "id": 1331, "name": "Tell kids I am their father" }]
            }
        }
        responses.add(POST, 'http://app/tasks/2272/setParent', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.set_parent(2272, req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_projects(self):
        res = {
            "data": [
                { "id": 1331, "name": "Things To Buy" },
                { "id": 14641, "name": "Cat Stuff" }
            ]
        }
        responses.add(GET, 'http://app/tasks/1001/projects', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.projects(1001), res['data'])

    def test_tasks_add_project(self):
        req = { "project": 14641 }
        res = { "data": {} }
        responses.add(POST, 'http://app/tasks/1001/addProject', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.add_project(1001, req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_remove_project(self):
        req = { "project": 14641 }
        res = { "data": {} }
        responses.add(POST, 'http://app/tasks/1001/removeProject', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.remove_project(1001, req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_tags(self):
        res = {
            "data": [
                { "id": 1331, "name": "orange" },
                { "id": 1771, "name": "fluffy" }
            ]
        }
        responses.add(GET, 'http://app/tasks/1001/tags', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.tags(1001), res['data'])

    def test_tasks_1001_addTag(self):
        req = { "tag": 1771 }
        res = { "data": {} }
        responses.add(POST, 'http://app/tasks/1001/addTag', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.add_tag(1001, req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_removeTag(self):
        req = { "tag": 1771 }
        res = { "data": {} }
        responses.add(POST, 'http://app/tasks/1001/removeTag', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.remove_tag(1001, req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_add_followers(self):
        req = { "followers": [1235] }
        res = {
            "data": {
                "followers": [{ "id": 1235, "name": "Darth Vader" }],
                "id": 1001
            }
        }
        responses.add(POST, 'http://app/tasks/1001/addFollowers', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.add_followers(1001, req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tasks_remove_followers(self):
        req = { "followers": [1235] }
        res = { "data": { "followers": [], "id": 1001 } }
        responses.add(POST, 'http://app/tasks/1001/removeFollowers', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.remove_followers(1001, req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_projects_create(self):
        req = {
            "name": "Things to Buy",
            "notes": "These are things we want to purchase.",
            "workspace": 14916
        }
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy",
                "notes": "These are things we want to purchase."
            }
        }
        responses.add(POST, 'http://app/projects', status=201, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.create(req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_projects_find_by_id(self):
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy",
                "notes": "These are things we want to purchase."
            }
        }
        responses.add(GET, 'http://app/projects/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.find_by_id(1331), res['data'])

    def test_projects_update(self):
        req = {
            "notes": "These are things we NEED to purchase."
        }
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy",
                "notes": "These are things we NEED to purchase."
            }
        }
        responses.add(PUT, 'http://app/projects/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.update(1331, req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_projects_delete(self):
        res = { "data": {} }
        responses.add(DELETE, 'http://app/projects/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.delete(1331), res['data'])

    def test_projects_tasks(self):
        res = {
            "data": [
                { "id": 2001, "name": "Catnip" },
                { "id": 2002, "name": "Kitty litter" }
            ]
        }
        responses.add(GET, 'http://app/projects/1331/tasks', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.find_by_project(1331), res['data'])

    def test_projects_find_by_workspace(self):
        res = {
            "data": [
                { "id": 1331, "name": "Things to buy" },
                { "id": 14641, "name": "Cat Stuff" }
            ]
        }
        responses.add(GET, 'http://app/workspaces/14916/projects', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.projects.find_by_workspace(14916), res['data'])

    def test_tags_create(self):
        req = { "name": "fluffy", "workspace": 14916 }
        res = { "data": { "id": 1771, "name": "fluffy" } }
        responses.add(POST, 'http://app/tags', status=201, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tags.create(req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_tags_find_by_id(self):
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy",
                "notes": "These are things we want to purchase."
            }
        }
        responses.add(GET, 'http://app/tags/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tags.find_by_id(1331), res['data'])

    def test_tags_update(self):
        req = { "name": "Things to Sell" }
        res = { "data": { "id": 1331, "name": "Things to Sell" } }
        responses.add(PUT, 'http://app/tags/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tags.update(1331, req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    @unittest.skip("tasks.find_by_tag not yet implemented")
    def test_tasks_find_by_tag(self):
        res = {
            "data": [
                { "id": 2001, "name": "Catnip" },
                { "id": 2002, "name": "Kitty litter" }
            ]
        }
        responses.add(GET, 'http://app/tags/1331/tasks', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.find_by_tag(1331), res['data'])

    def test_tags_find_by_workspace(self):
        res = {
            "data": [
                { "id": 1331, "name": "Things to buy" },
                { "id": 14641, "name": "Cat Stuff" }
            ]
        }
        responses.add(GET, 'http://app/workspaces/14916/tags', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tags.find_by_workspace(14916), res['data'])

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
        req = { "text": "This is a very nice comment." }
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
        self.assertEqual(self.client.stories.create_on_task(1001, req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_workspaces_find_all(self):
        res = { "data": [{ "id": 1337, "name": "My Favorite Workspace" }]}
        responses.add(GET, 'http://app/workspaces', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.workspaces.find_all(), res['data'])

    def test_workspaces_update(self):
        req = { "name": "Everyone's Favorite Workspace" }
        res = { "data": { "id": 1337, "name": "Everyone's Favorite Workspace" } }
        responses.add(PUT, 'http://app/workspaces/1337', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.workspaces.update(1337, req), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_teams_find_by_organization(self):
        res = {
            "data": [
                { "id": 5832, "name": "Atlanta Braves" },
                { "id": 15923, "name": "New York Yankees" }
            ]
        }
        responses.add(GET, 'http://app/organizations/13523/teams', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.teams.find_by_organization(13523), res['data'])

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

    def test_workspaces_typeahead(self):
        req = { "type": "user", "query": "Greg" }
        res = { "data": [{ "id": 999, "name": "Greg Sanchez" }]}
        responses.add(GET, 'http://app/workspaces/1337/typeahead?type=user&query=Greg', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.workspaces.typeahead(1337, req), res['data'])

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
