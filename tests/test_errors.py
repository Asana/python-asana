import json

import responses

from .helpers import asana, ClientTestCase


class TestErrors(ClientTestCase):
    def test_premium_only_402(self):
        resp_json = {
            "errors": [
                {
                    "message": (
                        "Custom Fields are not available for free "
                        "users or guests.")
                }
            ]
        }
        responses.add(
            responses.GET,
            'http://app/workspaces/12345/custom_fields', status=402,
            body=json.dumps(resp_json), match_querystring=True)
        with self.assertRaises(asana.error.PremiumOnlyError):
            self.client.custom_fields.get_custom_fields_for_workspace('12345')
