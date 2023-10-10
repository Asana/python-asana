from .helpers import *

class TestClientCustomFieldSettings(ClientTestCase):
    def test_custom_field_settings_get_custom_field_settings_for_project(self):
        res = {
            "data": [
                {
                    "id": 258147,
                    "custom_field": [
                        {
                            "id": 124578,
                            "name": "Priority",
                            "type": "enum"
                            }
                        ],
                    "project": [
                        {
                            "id": 1331,
                            "name": "Things to buy"
                            }
                        ]
                },
                {
                    "id": 369852,
                    "custom_field": [
                        {
                            "id": 235689,
                            "name": "Cost",
                            "type": "enum"
                            }
                        ],
                    "project": [
                        {
                            "id": 1331,
                            "name": "Things to buy"
                            }
                        ]
                },
            ]
        }
        responses.add(GET, 'http://app/projects/1331/custom_field_settings', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.custom_field_settings.get_custom_field_settings_for_project('1331'), res['data'])

