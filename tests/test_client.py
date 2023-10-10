import warnings
try:
    from mock import patch, call
except ImportError:
    from unittest.mock import patch, call

from .helpers import *

class TestClient(ClientTestCase):

    def test_version_values(self):
        values = self.client._version_values()
        self.assertEqual('Python', values['language'])
        self.assertRegex(values['version'], r'[0-9]+[.][0-9]+[.][0-9]+')
        self.assertSetEqual(
            {'language', 'version', 'language_version', 'os', 'os_version'},
            set(values.keys()))

    def test_version_header(self):
        self.assertRegex(
            self.client._version_header(), r'language=Python')

    def test_default_headers(self):
        self.client.headers['key'] = 'value'
        responses.add(GET, 'http://app/users/me', status=200, body='{"data":{}}')
        self.client.users.get_user('me')
        self.assertLessEqual(
            set({'key': 'value'}.items()),
            set(responses.calls[0].request.headers.items())
        )

    def test_request_headers(self):
        responses.add(GET, 'http://app/users/me', status=200, body='{"data":{}}')
        self.client.users.get_user('me', headers={'key': 'value'})
        self.assertLessEqual(
            set({'key': 'value'}.items()),
            set(responses.calls[0].request.headers.items())
        )

    def test_overriding_headers(self):
        self.client.headers['key'] = 'value'
        self.client.headers['key2'] = 'value2'
        responses.add(GET, 'http://app/users/me', status=200, body='{"data":{}}')
        self.client.users.get_user('me', headers={'key2': 'value3'})
        self.assertLessEqual(
            set({'key': 'value', 'key2': 'value3'}.items()),
            set(responses.calls[0].request.headers.items())
        )

    def test_content_type_headers(self):
        self.client.headers['key'] = 'value'
        responses.add(POST, 'http://app/tasks/123/addProject', status=200,
                      body='{"data":{}}')
        self.client.tasks.add_project(123, project=456, headers={'key2': 'value2'})
        self.assertLessEqual(
            set({'content-type': 'application/json'}.items()),
            set(responses.calls[0].request.headers.items())
        )

    def test_users_me_not_authorized(self):
        res = {
            "errors": [
                { "message": "Not Authorized" }
            ]
        }
        responses.add(GET, 'http://app/users/me', status=401, body=json.dumps(res), match_querystring=True)
        self.assertRaises(asana.error.NoAuthorizationError, self.client.users.get_user, 'me')

    def test_tasks_get_tasks_invalid_request(self):
        res = {
            "errors": [
                { "message": "workspace: Missing input" }
            ]
        }
        responses.add(GET, 'http://app/tasks', status=400, body=json.dumps(res), match_querystring=True)
        self.assertRaises(asana.error.InvalidRequestError, self.client.tasks.get_tasks)

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
        self.assertRaises(asana.error.ServerError, self.client.users.get_user, 'me', max_retries=0)

    def test_users_me_unfriendly_server_error(self):
        res = "Crappy Response"
        responses.add(GET, 'http://app/users/me', status=504, body=res, match_querystring=True)
        self.assertRaises(asana.error.ServerError, self.client.users.get_user, 'me', max_retries=0)

    def test_users_get_user_not_found(self):
        res = {
            "errors": [
                { "message": "user: Unknown object: 1234124312341" }
            ]
        }
        responses.add(GET, 'http://app/users/1234', status=404, body=json.dumps(res), match_querystring=True)
        self.assertRaises(asana.error.NotFoundError, self.client.users.get_user, ('1234'))

    def test_users_get_user_forbidden(self):
        res = {
            "errors": [
                { "message": "user: Forbidden" }
            ]
        }
        responses.add(GET, 'http://app/users/1234', status=403, body=json.dumps(res), match_querystring=True)
        self.assertRaises(asana.error.ForbiddenError, self.client.users.get_user, ('1234'))

    def test_option_pretty(self):
        res = {
            "data": { "email": "sanchez@...", "id": 999, "name": "Greg Sanchez" }
        }
        responses.add(GET, 'http://app/users/me?opt_pretty=true', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.users.get_user('me', pretty=True), res['data'])

    def test_option_fields(self):
        res = {
            "data": { "name": "Make a list", "notes": "Check it twice!", "id": 1224 }
        }
        responses.add(GET, 'http://app/tasks/1224?opt_fields=name%2Cnotes', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.tasks.get_task('1224', fields=['name','notes']), res['data'])

    def test_option_expand(self):
        req = {
            'data': { 'assignee': 1234 },
            'options': { 'expand' : ['projects'] }
        }
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
        self.assertEqual(self.client.tasks.update_task('1001', req['data'], expand=['projects']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

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
        responses.add(GET, 'http://app/projects/1337/tasks?limit=5&offset=eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9', status=200, body=json.dumps(res), match_querystring=True)

        self.assertEqual(self.client.tasks.get_tasks_for_project('1337', { 'limit': 5, 'offset': 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9'}), res['data'])

    @unittest.skip("iterator_type='pages' disabled")
    def test_page_iterator_item_limit_lt_items(self):
        responses.add(GET, 'http://app/projects/1337/tasks?limit=2', status=200, body=json.dumps({ 'data': ['a', 'b'], 'next_page': { 'offset': 'a', 'path': '/projects/1337/tasks?limit=2&offset=a' } }), match_querystring=True)
        responses.add(GET, 'http://app/projects/1337/tasks?limit=2&offset=a', status=200, body=json.dumps({ 'data': ['c'], 'next_page': null }), match_querystring=True)

        iterator = self.client.tasks.get_tasks_for_project('1337', item_limit=2, page_size=2, iterator_type='pages')
        self.assertEqual(next(iterator), ['a', 'b'])
        self.assertRaises(StopIteration, next, (iterator))

    @unittest.skip("iterator_type='pages' disabled")
    def test_page_iterator_item_limit_eq_items(self):
        responses.add(GET, 'http://app/projects/1337/tasks?limit=2', status=200, body=json.dumps({ 'data': ['a', 'b'], 'next_page': { 'offset': 'a', 'path': '/projects/1337/tasks?limit=2&offset=a' } }), match_querystring=True)
        responses.add(GET, 'http://app/projects/1337/tasks?limit=1&offset=a', status=200, body=json.dumps({ 'data': ['c'], 'next_page': null }), match_querystring=True)

        iterator = self.client.tasks.get_tasks_for_project('1337', item_limit=3, page_size=2, iterator_type='pages')
        self.assertEqual(next(iterator), ['a', 'b'])
        self.assertEqual(next(iterator), ['c'])
        self.assertRaises(StopIteration, next, (iterator))

    @unittest.skip("iterator_type='pages' disabled")
    def test_page_iterator_item_limit_gt_items(self):
        responses.add(GET, 'http://app/projects/1337/tasks?limit=2', status=200, body=json.dumps({ 'data': ['a', 'b'], 'next_page': { 'offset': 'a', 'path': '/projects/1337/tasks?limit=2&offset=a' } }), match_querystring=True)
        responses.add(GET, 'http://app/projects/1337/tasks?limit=2&offset=a', status=200, body=json.dumps({ 'data': ['c'], 'next_page': null }), match_querystring=True)

        iterator = self.client.tasks.get_tasks_for_project('1337', item_limit=4, page_size=2, iterator_type='pages')
        self.assertEqual(next(iterator), ['a', 'b'])
        self.assertEqual(next(iterator), ['c'])
        self.assertRaises(StopIteration, next, (iterator))

    def test_item_iterator_item_limit_lt_items(self):
        responses.add(GET, 'http://app/projects/1337/tasks?limit=2', status=200, body=json.dumps({ 'data': ['a', 'b'], 'next_page': { 'offset': 'a', 'path': '/projects/1337/tasks?limit=2&offset=a' } }), match_querystring=True)

        iterator = self.client.tasks.get_tasks_for_project('1337', item_limit=2, page_size=2, iterator_type='items')
        self.assertEqual(next(iterator), 'a')
        self.assertEqual(next(iterator), 'b')
        self.assertRaises(StopIteration, next, (iterator))

    def test_item_iterator_item_limit_eq_items(self):
        responses.add(GET, 'http://app/projects/1337/tasks?limit=2', status=200, body=json.dumps({ 'data': ['a', 'b'], 'next_page': { 'offset': 'a', 'path': '/projects/1337/tasks?limit=2&offset=a' } }), match_querystring=True)
        responses.add(GET, 'http://app/projects/1337/tasks?limit=1&offset=a', status=200, body=json.dumps({ 'data': ['c'], 'next_page': null }), match_querystring=True)

        iterator = self.client.tasks.get_tasks_for_project('1337', item_limit=3, page_size=2, iterator_type='items')
        self.assertEqual(next(iterator), 'a')
        self.assertEqual(next(iterator), 'b')
        self.assertEqual(next(iterator), 'c')
        self.assertRaises(StopIteration, next, (iterator))

    def test_item_iterator_item_limit_gt_items(self):
        responses.add(GET, 'http://app/projects/1337/tasks?limit=2', status=200, body=json.dumps({ 'data': ['a', 'b'], 'next_page': { 'offset': 'a', 'path': '/projects/1337/tasks?limit=2&offset=a' } }), match_querystring=True)
        responses.add(GET, 'http://app/projects/1337/tasks?limit=2&offset=a', status=200, body=json.dumps({ 'data': ['c'], 'next_page': null }), match_querystring=True)

        iterator = self.client.tasks.get_tasks_for_project('1337', item_limit=4, page_size=2, iterator_type='items')
        self.assertEqual(next(iterator), 'a')
        self.assertEqual(next(iterator), 'b')
        self.assertEqual(next(iterator), 'c')
        self.assertRaises(StopIteration, next, (iterator))

    def test_item_iterator_preserve_opt_fields(self):
        responses.add(GET, 'http://app/projects/1337/tasks?limit=2&opt_fields=foo', status=200, body=json.dumps({ 'data': ['a', 'b'], 'next_page': { 'offset': 'a', 'path': '/projects/1337/tasks?limit=2&offset=a' } }), match_querystring=True)
        responses.add(GET, 'http://app/projects/1337/tasks?limit=1&opt_fields=foo&offset=a', status=200, body=json.dumps({ 'data': ['c'], 'next_page': null }), match_querystring=True)

        iterator = self.client.tasks.get_tasks_for_project('1337', item_limit=3, page_size=2, fields=['foo'], iterator_type='items')
        self.assertEqual(next(iterator), 'a')
        self.assertEqual(next(iterator), 'b')
        self.assertEqual(next(iterator), 'c')
        self.assertRaises(StopIteration, next, (iterator))

    @patch('time.sleep')
    def test_rate_limiting(self, time_sleep):
        res = [
            (429, { 'Retry-After': '10' }, '{}'),
            (200, {}, json.dumps({ 'data': 'me' }))
        ]
        responses.add_callback(responses.GET, 'http://app/users/me', callback=lambda r: res.pop(0), content_type='application/json')

        self.assertEqual(self.client.users.get_user('me'), 'me')
        self.assertEqual(len(responses.calls), 2)
        self.assertEqual(time_sleep.mock_calls, [call(10.0)])

    @patch('time.sleep')
    def test_rate_limited_twice(self, time_sleep):
        res = [
            (429, { 'Retry-After': '10' }, '{}'),
            (429, { 'Retry-After': '1' }, '{}'),
            (200, {}, json.dumps({ 'data': 'me' }))
        ]
        responses.add_callback(responses.GET, 'http://app/users/me', callback=lambda r: res.pop(0), content_type='application/json')

        self.assertEqual(self.client.users.get_user('me'), 'me')
        self.assertEqual(len(responses.calls), 3)
        self.assertEqual(time_sleep.mock_calls, [call(10.0), call(1.0)])

    @patch('time.sleep')
    def test_server_error_retry(self, time_sleep):
        res = [
            (500, {}, '{}'),
            (500, {}, '{}'),
            (500, {}, '{}'),
            (200, {}, json.dumps({ 'data': 'me' }))
        ]
        responses.add_callback(responses.GET, 'http://app/users/me', callback=lambda r: res.pop(0), content_type='application/json')

        self.assertRaises(asana.error.ServerError, self.client.users.get_user, 'me', max_retries=2)
        self.assertEqual(time_sleep.mock_calls, [call(1.0), call(2.0)])

    @patch('time.sleep')
    def test_server_error_retry_backoff(self, time_sleep):
        res = [
            (500, {}, '{}'),
            (500, {}, '{}'),
            (500, {}, '{}'),
            (200, {}, json.dumps({ 'data': 'me' }))
        ]
        responses.add_callback(responses.GET, 'http://app/users/me', callback=lambda r: res.pop(0), content_type='application/json')

        self.assertEqual(self.client.users.get_user('me'), 'me')
        self.assertEqual(time_sleep.mock_calls, [call(1.0), call(2.0), call(4.0)])


    def test_get_named_parameters(self):
        responses.add(GET, 'http://app/tasks?workspace=14916&assignee=me', status=200, body=json.dumps({ 'data': 'dummy data' }), match_querystring=True)

        self.assertEqual(self.client.tasks.get_tasks(workspace=14916, assignee="me"), 'dummy data')

    def test_post_named_parameters(self):
        responses.add(POST, 'http://app/tasks', status=201, body='{ "data": "dummy data" }', match_querystring=True)

        self.assertEqual(self.client.tasks.create_task(assignee=1235, followers=[5678], name="Hello, world."), 'dummy data')
        self.assertEqual(json.loads(responses.calls[0].request.body), {
            "data": {
                "assignee": 1235,
                "followers": [5678],
                "name": "Hello, world."
            }
        })

    def test_put_named_parameters(self):
        responses.add(PUT, 'http://app/tasks/1001', status=200, body='{ "data": "dummy data" }', match_querystring=True)

        self.assertEqual(self.client.tasks.update_task('1001', assignee=1235, followers=[5678], name="Hello, world."), 'dummy data')
        self.assertEqual(json.loads(responses.calls[0].request.body), {
            "data": {
                "assignee": 1235,
                "followers": [5678],
                "name": "Hello, world."
            }
        })

    def test_asana_change_header_logging(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            requestHeaders = {}
            responseHeaders = {
                'asana-change': 'name=string_ids;info=something;affected=true'
            }
            self.client._log_asana_change_header(requestHeaders, responseHeaders)

            assert len(w) == 1

    def test_asana_change_header_logging_turned_off(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            requestHeaders = {}
            responseHeaders = {
                'asana-change': 'name=string_ids;info=something;affected=true'
            }
            self.client.LOG_ASANA_CHANGE_WARNINGS = false
            self.client._log_asana_change_header(requestHeaders, responseHeaders)

            assert len(w) == 0

    def test_asana_change_header_ignore_case(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            requestHeaders = {}
            responseHeaders = {
                'asANa-chANge': 'name=string_ids;info=something;affected=true'
            }
            self.client._log_asana_change_header(requestHeaders, responseHeaders)

            assert len(w) == 1

    def test_asana_change_header_enable(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            requestHeaders = {
                'asana-enable': 'string_ids'
            }
            responseHeaders = {
                'asana-change': 'name=string_ids;info=something;affected=true'
            }
            self.client._log_asana_change_header(requestHeaders, responseHeaders)

            assert len(w) == 0

    def test_asana_change_header_disable(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            requestHeaders = {
                'asana-disable': 'string_ids'
            }
            responseHeaders = {
                'asana-change': 'name=string_ids;info=something;affected=true'
            }
            self.client._log_asana_change_header(requestHeaders, responseHeaders)

            assert len(w) == 0

    def test_asana_change_header_multiple(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            requestHeaders = {}
            responseHeaders = {
                'asana-change': 'name=string_ids;info=something;affected=true,name=new_sections;info=something;affected=true'
            }
            self.client._log_asana_change_header(requestHeaders, responseHeaders)

            assert len(w) == 2

    def test_asana_change_header_multiple_disable(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            requestHeaders = {
                'asana-disable': 'string_ids,new_sections'
            }
            responseHeaders = {
                'asana-change': 'name=string_ids;info=something;affected=true,name=new_sections;info=something;affected=true'
            }
            self.client._log_asana_change_header(requestHeaders, responseHeaders)

            assert len(w) == 0
