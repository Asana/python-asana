
from .gen.events import _Events
from ..error import InvalidTokenError
from ..page_iterator import EventsPageIterator

class Events(_Events):
    """Events resource"""

    def get(self, params, **options):
        """Dispatches a GET request to /events of the API to get a set of recent changes to a resource."""
        options = self.client._merge_options({ 'full_payload': True })
        return self.client.get('/events', params, **options)

    def get_next(self, query, **options):
        """Returns a tuple containing the next page of events and a sync token for the given query (and optional 'sync' token)"""
        iterator = EventsPageIterator(self.client, '/events', query, options)
        result = iterator.next()
        return (result, iterator.sync)

    def get_iterator(self, query, **options):
        """Returns an event iterator for the given query (and optional 'sync' token)"""
        return EventsPageIterator(self.client, '/events', query, options).items()
