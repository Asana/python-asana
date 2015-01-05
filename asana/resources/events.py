
from ._events import _Events
from ..error import InvalidTokenError

import time

class Events(_Events):
    POLL_INTERVAL = 1000

    def get_next(self, params):
        params = params.copy()
        if 'sync' not in params:
            try:
                self.get(params)
            except InvalidTokenError as e:
                params['sync'] = e.value['sync']
        while True:
            result = self.get(params)
            if 'data' in result and len(result['data']) > 0:
                return (result['data'], result['sync'])
            else:
                params['sync'] = result['sync']
                time.sleep(self.POLL_INTERVAL / 1000.0)

    def get_iterator(self, params):
        params = params.copy()
        while True:
            items, sync = self.get_next(params)
            for item in items:
                yield item
            params['sync'] = sync
