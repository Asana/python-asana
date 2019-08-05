from .helpers import *

class TestClientPortfolioMemberships(ClientTestCase):
    def test_portfolio_memberships_find_by_id(self):
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy"
            }
        }
        responses.add(GET, 'http://app/portfolio_memberships/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.portfolio_memberships.find_by_id(1331), res['data'])

    def test_portfolio_memberships_find_by_portfolio(self):
        res = {
            "data": [
                {
                    "id": 1331,
                    "name": "Things to Buy"
                }
            ]
        }
        responses.add(GET, 'http://app/portfolios/1331/portfolio_memberships', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.portfolio_memberships.find_by_portfolio(1331), res['data'])

    def test_portfolio_memberships_find_all(self):
        res = {
            "data": [
                { "id": 1331, "name": "Things to buy" },
                { "id": 14641, "name": "Cat Stuff" }
            ]
        }
        responses.add(GET, 'http://app/portfolio_memberships', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.portfolio_memberships.find_all(), res['data'])

