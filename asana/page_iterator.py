import abc
import time

from asana.error import InvalidTokenError
from asana.helpers import merge_dicts


class PageIterator(object, metaclass=abc.ABCMeta):
    """Generic page iterator class, used for collections and events"""

    CONTINUATION_KEY = ''

    def __init__(self, client, path, query, options):
        self.client = client
        self.path = path
        self.query = query
        self.options = merge_dicts(client.options, options, {'full_payload': True})

        self.item_limit = float('inf') if self.options.get('item_limit') is None else self.options['item_limit']
        self.page_size = self.options['page_size']
        self.count = 0

        self._started = False
        self._continuation_data = None

    def __getattr__(self, name):
        """Getter for the custom named 'continuation' object."""
        if name == self.CONTINUATION_KEY:
            return self._continuation_data
        raise AttributeError("%r object has no attribute %r" % (self.__class__, name))

    def __iter__(self):
        """Iterator interface, self is an iterator"""
        return self

    def __next__(self):
        """Iterator interface, returns the next 'page'"""

        self._update_limit_option()
        if not self._has_next_page():
            raise StopIteration
        # First call to __next__
        if not self._started:
            self._started = True
            result = self._get_initial_page()
        # Subsequent calls to __next__
        else:
            result = self._get_next_page()
        self._process_continuation(result)
        data = result.get('data')
        self._process_data(data)
        return data

    def _update_limit_option(self):
        """ Compute the limit from the page size, and remaining item limit """
        self.options['limit'] = min(self.page_size, self.item_limit - self.count)

    def _has_next_page(self):
        """ Returns a bool predicate for next page exists """
        if self.options['limit'] == 0:
            return False
        if not self._started:
            return True
        return self._continuation_data is not None

    def _process_continuation(self, result):
        """ Extract the continuation data from the response """
        self._continuation_data = result.get(self.CONTINUATION_KEY, None)

    def _process_data(self, data):
        """ Process data : update count"""
        if data is not None:
            self.count += len(data)

    def next(self):
        """Alias for __next__"""
        return self.__next__()

    def items(self):
        """Returns an iterator for each item in each page"""
        for page in self:
            for item in page:
                yield item

    @abc.abstractmethod
    def _get_initial_page(self):
        raise NotImplementedError

    @abc.abstractmethod
    def _get_next_page(self):
        raise NotImplementedError


class CollectionPageIterator(PageIterator):
    """Iterator that returns one page of a collection at a time"""

    CONTINUATION_KEY = 'next_page'

    def _get_initial_page(self):
        return self.client.get(self.path, self.query, **self.options)

    def _get_next_page(self):
        self.options['offset'] = self._continuation_data['offset']
        return self.client.get(self.path, self.query, **self.options)


class EventsPageIterator(PageIterator):
    """Iterator that returns the next page of events, polls until a non-empty page is returned"""

    CONTINUATION_KEY = 'sync'

    def _get_initial_page(self):
        # If no sync token was provided, make a request to get one
        if 'sync' not in self.query:
            try:
                self.client.events.get(self.query, **self.options)
            except InvalidTokenError as e:
                # InvalidTokenError is expected to be thrown since we didn't provide a sync token
                self.continuation = e.sync
        else:
            self.continuation = self.query['sync']
        return self._get_next_page()

    def _get_next_page(self):
        self.query['sync'] = self.continuation
        return self.client.events.get(self.query, **self.options)

    def __next__(self):
        # Override __next__ to continue polling until a non-empty page of events is returned
        while True:
            results = super(EventsPageIterator, self).__next__()
            if len(results) > 0:
                return results
            else:
                time.sleep(self.options['poll_interval'])


class AuditLogAPIIterator(CollectionPageIterator):
    """Iterator that returns the next page of audit_log_api"""

    def _process_data(self, data):
        """ Process data: raise StopIteration if data is absent, update count otherwise"""
        if not data:
            raise StopIteration
        else:
            self.count += len(data)

