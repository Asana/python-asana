from .helpers import *


class TestClientAuditLogAPI(ClientTestCase):

    def test_get_audit_log_events(self):
        res = {
            "data": [
                {
                    "actor": {
                        "actor_type": "user",
                        "email": "gregsanchez@example.com",
                        "gid": "1111",
                        "name": "Greg Sanchez"
                    },
                    "context": {
                        "api_authentication_method": "cookie",
                        "client_ip_address": "1.1.1.1",
                        "context_type": "web",
                        "oauth_app_name": "string",
                        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
                    },
                    "created_at": "2021-01-01T00:00:00.000Z",
                    "details": {},
                    "event_category": "deletion",
                    "event_type": "task_deleted",
                    "gid": "12345",
                    "resource": {
                        "email": "string",
                        "gid": "1111",
                        "name": "Example Task",
                        "resource_subtype": "milestone",
                        "resource_type": "task"
                    }
                }
            ],
            "next_page": {
                "offset": "a",
                "path": "/workspaces/1337/audit_log_events?offset=a",
                "uri": "https://app.asana.com/api/1.0/workspaces/1337/audit_log_events?offset=a"
            }
        }
        responses.add(GET, 'http://app/workspaces/1337/audit_log_events?',
                      status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(
            self.client.audit_log_api.get_audit_log_events("1337"), res['data'])

    def test_get_audit_log_events_iterator(self):
        res1 = {
            "data": [
                {
                    "actor": {
                        "actor_type": "user",
                        "email": "gregsanchez@example.com",
                        "gid": "1111",
                        "name": "Greg Sanchez"
                    },
                    "context": {
                        "api_authentication_method": "cookie",
                        "client_ip_address": "1.1.1.1",
                        "context_type": "web",
                        "oauth_app_name": "string",
                        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
                    },
                    "created_at": "2021-01-01T00:00:00.000Z",
                    "details": {},
                    "event_category": "deletion",
                    "event_type": "task_deleted",
                    "gid": "12345",
                    "resource": {
                        "email": "string",
                        "gid": "1111",
                        "name": "Example Task",
                        "resource_subtype": "milestone",
                        "resource_type": "task"
                    }
                }
            ],
            "next_page": {
                "offset": "a",
                "path": "/workspaces/1337/audit_log_events?limit=1&offset=a",
                "uri": "https://app.asana.com/api/1.0/workspaces/1337/audit_log_events?limit=1&offset=a"
            }
        }
        res2 = {
            "data": [
                {
                    "actor": {
                        "actor_type": "user",
                        "email": "tbizarro@example.com",
                        "gid": "1234",
                        "name": "Tim Bizarro"
                    },
                    "context": {
                        "api_authentication_method": "cookie",
                        "client_ip_address": "1.1.1.1",
                        "context_type": "web",
                        "oauth_app_name": "string",
                        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
                    },
                    "created_at": "2021-01-01T00:00:00.000Z",
                    "details": {},
                    "event_category": "deletion",
                    "event_type": "task_deleted",
                    "gid": "12345",
                    "resource": {
                        "email": "string",
                        "gid": "1111",
                        "name": "Example Task",
                        "resource_subtype": "milestone",
                        "resource_type": "task"
                    }
                }
            ],
            "next_page": {
                "offset": "b",
                "path": "/workspaces/1337/audit_log_events?limit=1&offset=b",
                "uri": "https://app.asana.com/api/1.0/workspaces/1337/audit_log_events?limit=1&offset=b"
            }
        }
        res3 = {
            "data": [],
            "next_page": {
                "offset": "c",
                "path": "/workspaces/1337/audit_log_events?limit=1&offset=c",
                "uri": "https://app.asana.com/api/1.0/workspaces/1337/audit_log_events?limit=1&offset=c"
            }
        }
        res4 = {
            "data": [],
            "next_page": {
                "offset": "d",
                "path": "/workspaces/1337/audit_log_events?limit=1&offset=d",
                "uri": "https://app.asana.com/api/1.0/workspaces/1337/audit_log_events?limit=1&offset=d"
            }
        }
        responses.add(GET, 'http://app/workspaces/1337/audit_log_events?limit=1',
                      status=200, body=json.dumps(res1), match_querystring=True)
        responses.add(GET, 'http://app/workspaces/1337/audit_log_events?limit=1&offset=a',
                      status=200, body=json.dumps(res2), match_querystring=True)
        responses.add(GET, 'http://app/workspaces/1337/audit_log_events?limit=1&offset=b',
                      status=200, body=json.dumps(res3), match_querystring=True)
        responses.add(GET, 'http://app/workspaces/1337/audit_log_events?limit=1&offset=c',
                      status=200, body=json.dumps(res4), match_querystring=True)
        # Set iterator_type to 'items' to return an iterator
        iterator = self.client.audit_log_api.get_audit_log_events(
            "1337", page_size=1, iterator_type='items'
        )
        # Iterator should stop on third call
        self.assertEqual(next(iterator), res1['data'][0])
        self.assertEqual(next(iterator), res2['data'][0])
        self.assertRaises(StopIteration, next, (iterator))
