from .helpers import *

class TestClientCustomFields(ClientTestCase):
    def test_custom_fields_get_custom_field_text(self):
        res = {
            "data": [
                {
                    "id": 134679,
                    "created_at": "2016-07-11T14:29:23.249Z",
                    "name": "Owner",
                    "type": "text"
                }
            ]
        }
        responses.add(GET, 'http://app/custom_fields/134679', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.custom_fields.get_custom_field('134679'), res['data'])

    def test_custom_fields_get_custom_field_enum(self):
        res = {
            "data": [
                {
                    "id": 124578,
                    "created_at": "2016-07-11T14:29:23.249Z",
                    "name": "Priority",
                    "type": "enum",
                    "enum_options": [
                        {
                            "id": 789,
                            "name": "Low",
                            "enabled": true,
                            "color": "blue"
                        },
                        {
                            "id": 208,
                            "name": "Medium",
                            "enabled": false,
                            "color": "yellow"
                        },
                        {
                            "id": 439,
                            "name": "High",
                            "enabled": true,
                            "color": "red"
                        }
                    ]
                }
            ]
        }
        responses.add(GET, 'http://app/custom_fields/124578', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.custom_fields.get_custom_field('124578'), res['data'])

    def test_custom_fields_get_custom_field_number(self):
        res = {
            "data": [
                {
                    "id": 938271,
                    "created_at": "2016-07-11T14:29:23.249Z",
                    "name": "Price",
                    "type": "number",
                    "precision": 2
                }
            ]
        }
        responses.add(GET, 'http://app/custom_fields/938271', status=200, body=json.dumps(res), match_querystring=True)
        self.assertEqual(self.client.custom_fields.get_custom_field('938271'), res['data'])
