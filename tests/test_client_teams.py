from .helpers import *

class TestClientTeams(ClientTestCase):

    def test_teams_find_by_organization(self):
        res = {
            "data": [
                { "id": 5832, "name": "Atlanta Braves" },
                { "id": 15923, "name": "New York Yankees" }
            ]
        }
        responses.add(GET, 'http://app/organizations/13523/teams', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.teams.find_by_organization(13523), res['data'])
