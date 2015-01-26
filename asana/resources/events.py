
from ._events import _Events
from ..error import InvalidTokenError
from ..page_iterator import EventsPageIterator

import time

class Events(_Events):

    def get_next(self, query, **options):
        iterator = EventsPageIterator(self.client, '/events', query, options)
        result = iterator.next()
        return (result, iterator.sync)

    def get_iterator(self, query, **options):
        return EventsPageIterator(self.client, '/events', query, options).items()
