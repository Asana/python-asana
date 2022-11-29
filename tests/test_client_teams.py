from .helpers import *

class TestClientTeams(ClientTestCase):

    def test_teams_get_teams_for_workspace(self):
        res = {
            "data": [
                { "id": 5832, "name": "Atlanta Braves" },
                { "id": 15923, "name": "New York Yankees" }
            ]
        }
        responses.add(GET, 'http://app/workspaces/13523/teams', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.teams.get_teams_for_workspace('13523'), res['data'])
