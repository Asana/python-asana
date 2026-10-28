import json
import unittest
from unittest.mock import Mock

from asana.pagination.event_iterator import EventIterator
from asana.rest import ApiException


class TestEventIterator(unittest.TestCase):
    def make_iterator(self, responses, sync=None):
        iterator = EventIterator(None, {'query_params': {'sync': sync}})
        requested_tokens = []
        responses = iter(responses)

        def call_api():
            requested_tokens.append(iterator.api_request_data['query_params']['sync'])
            response = next(responses)
            if isinstance(response, Exception):
                raise response
            return response

        iterator.call_api = Mock(side_effect=call_api)
        return iterator, requested_tokens

    def test_advances_sync_after_each_page(self):
        iterator, requested_tokens = self.make_iterator([
            {'data': [1], 'sync': 'second', 'has_more': True},
            {'data': [2], 'sync': 'third', 'has_more': True},
            {'data': [3], 'sync': 'final', 'has_more': False},
        ], sync='first')

        self.assertEqual(list(iterator.items()), [1, 2, 3])
        self.assertEqual(requested_tokens, ['first', 'second', 'third'])
        self.assertEqual(iterator.sync, 'final')

    def test_advances_sync_after_handshake(self):
        handshake = ApiException(status=412)
        handshake.body = json.dumps({'sync': 'initial'}).encode('utf-8')
        iterator, requested_tokens = self.make_iterator([
            handshake,
            {'data': [1], 'sync': 'second', 'has_more': True},
            {'data': [], 'sync': 'final', 'has_more': False},
        ])

        self.assertEqual(list(iterator.items()), [1])
        self.assertEqual(requested_tokens, [None, 'initial', 'second'])
        self.assertEqual(iterator.sync, 'final')

    def test_propagates_other_errors(self):
        error = ApiException(status=500)
        iterator, requested_tokens = self.make_iterator([error], sync='first')
        with self.assertRaises(ApiException) as caught:
            next(iterator)
        self.assertIs(caught.exception, error)
        self.assertEqual(requested_tokens, ['first'])
