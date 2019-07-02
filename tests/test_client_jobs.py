from .helpers import *

class TestClientJobs(ClientTestCase):
    def test_jobs_find_by_id(self):
        res = {
            "data": {
                "id": 1331,
                "name": "Things to Buy"
            }
        }
        responses.add(GET, 'http://app/jobs/1331', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.jobs.find_by_id(1331), res['data'])

