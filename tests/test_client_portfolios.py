from .helpers import *

class TestClientPortfolios(ClientTestCase):
    def test_portfolios_create_portfolio(self):
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
        responses.add(POST, 'http://app/portfolios', status=201, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.portfolios.create_portfolio(req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_portfolios_get_portfolio(self):
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy",
                "notes": "These are things we want to purchase."
            }
        }
        responses.add(GET, 'http://app/portfolios/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.portfolios.get_portfolio('1331'), res['data'])

    def test_portfolios_update_portfolio(self):
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
        responses.add(PUT, 'http://app/portfolios/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.portfolios.update_portfolio('1331', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

    def test_portfolios_delete_portfolio(self):
        res = { "data": {} }
        responses.add(DELETE, 'http://app/portfolios/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.portfolios.delete_portfolio('1331'), res['data'])

    def test_portfolios_get_portfolios(self):
        res = {
            "data": [
                { "id": 1331, "name": "Things to buy" },
                { "id": 14641, "name": "Cat Stuff" }
            ]
        }
        responses.add(GET, 'http://app/portfolios', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.portfolios.get_portfolios(), res['data'])

    def test_portfolios_add_custom_field_settings(self):
        req = {
            "data": {
                "custom_field":124578,
                "is_important": true
            }
        }
        res = {
            "data": {}
        }

        responses.add(POST, 'http://app/portfolios/1331/addCustomFieldSetting', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.portfolios.add_custom_field_setting(1331, req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)


    def test_portfolios_remove_custom_field_settings(self):
        req = {
            "data": {
                "custom_field":124578,
            }
        }
        res = {
            "data": {}
        }

        responses.add(POST, 'http://app/portfolios/1331/addCustomFieldSetting', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.portfolios.add_custom_field_setting('1331', req['data']), res['data'])
        self.assertEqual(json.loads(responses.calls[0].request.body), req)

