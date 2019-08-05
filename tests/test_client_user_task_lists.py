from .helpers import *

class TestClientUserTaskLists(ClientTestCase):
    def test_user_task_lists_find_by_id(self):
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy"
            }
        }
        responses.add(GET, 'http://app/user_task_lists/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.user_task_lists.find_by_id(1331), res['data'])

    def test_user_task_lists_find_by_user(self):
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy"
            }
        }
        responses.add(GET, 'http://app/users/1331/user_task_list', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.user_task_lists.find_by_user(1331), res['data'])

    def test_user_task_lists_tasks(self):
        res = {
            "data": [
                { "id": 1331, "name": "Things to buy" },
                { "id": 14641, "name": "Cat Stuff" }
            ]
        }
        responses.add(GET, 'http://app/user_task_lists/1335/tasks', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.user_task_lists.tasks(1335), res['data'])

