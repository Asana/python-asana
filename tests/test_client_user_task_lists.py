from .helpers import *

class TestClientUserTaskLists(ClientTestCase):
    def test_user_task_lists_get_user_task_list(self):
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy"
            }
        }
        responses.add(GET, 'http://app/user_task_lists/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.user_task_lists.get_user_task_list('1331'), res['data'])

    def test_user_task_lists_get_user_task_list_for_user(self):
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy"
            }
        }
        responses.add(GET, 'http://app/users/1331/user_task_list', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.user_task_lists.get_user_task_list_for_user('1331'), res['data'])

    def test_task_get_tasks_for_user_task_list(self):
        res = {
            "data": [
                { "id": 1331, "name": "Things to buy" },
                { "id": 14641, "name": "Cat Stuff" }
            ]
        }
        responses.add(GET, 'http://app/user_task_lists/1335/tasks', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.get_tasks_for_user_task_list('1335'), res['data'])

