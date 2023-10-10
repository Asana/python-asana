
from .error import InvalidTokenError
import time

class PageIterator(object):
    """Generic page iterator class, used for collections and events"""

    def __init__(self, client, path, query, options):
        self.client = client
        self.path = path
        self.query = query
        self.options = client._merge_options(options, { 'full_payload': True })

        self.item_limit = float('inf') if self.options.get('item_limit', None) == None else self.options['item_limit']
        self.page_size = self.options['page_size']
        self.count = 0

        self.continuation = False

    def __getattr__(self, name):
        """Getter for the custom named 'continuation' object."""
        if name == self.CONTINUATION_KEY:
            return self.continuation
        raise AttributeError("%r object has no attribute %r" % (self.__class__, attr))

    def __iter__(self):
        """Iterator interface, self is an iterator"""
        return self

    def __next__(self):
        """Iterator interface, returns the next 'page'"""

        # Compute the limit from the page size, and remaining item limit
        self.options['limit'] = min(self.page_size, self.item_limit - self.count)
        # If there is no continuation value or computed limit is 0, we're done
        if self.continuation == None or self.options['limit'] == 0:
            raise StopIteration
        # First call to __next__
        elif self.continuation == False:
            result = self.get_initial()
        # Subsequent calls to __next__
        else:
            result = self.get_next()
        # Extract the continuation from the response
        self.continuation = result.get(self.CONTINUATION_KEY, None)
        # Get the data, update the count, return the data
        data = result.get('data', None)
        if data != None:
            self.count += len(data)
        return data

    def next(self):
        """Alias for __next__"""
        return self.__next__()

    def items(self):
        """Returns an iterator for each item in each page"""
        for page in self:
            for item in page:
                yield item


class CollectionPageIterator(PageIterator):
    """Iterator that returns one page of a collection at a time"""

    CONTINUATION_KEY = 'next_page'

    def get_initial(self):
        return self.client.get(self.path, self.query, **self.options)

    def get_next(self):
        self.options['offset'] = self.continuation['offset']
        return self.client.get(self.path, self.query, **self.options)


class EventsPageIterator(PageIterator):
    """Iterator that returns the next page of events, polls until a non-empty page is returned"""

    CONTINUATION_KEY = 'sync'

    def get_initial(self):
        # If no sync token was provided, make a request to get one
        if 'sync' not in self.query:
            try:
                self.client.events.get(self.query, **self.options)
            except InvalidTokenError as e:
                # InvalidTokenError is expected to be thrown since we didn't provide a sync token
                self.continuation = e.sync
        else:
            self.continuation = self.query['sync']
        return self.get_next()

    def get_next(self):
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

    def __next__(self):
        """Override __next__ to stop when there is no more data"""

        # Compute the limit from the page size, and remaining item limit
        self.options['limit'] = min(
            self.page_size, self.item_limit - self.count)
        # If there is no continuation value or computed limit is 0, we're done
        if self.continuation == None or self.options['limit'] == 0:
            raise StopIteration
        # First call to __next__
        elif self.continuation == False:
            result = self.get_initial()
        # Subsequent calls to __next__
        else:
            result = self.get_next()
        # Extract the continuation from the response
        self.continuation = result.get(self.CONTINUATION_KEY, None)
        # Get the data
        data = result.get('data', None)
        # If there is no more data we're done. Otherwise, we update the count and return the data
        if not data:
            raise StopIteration
        else:
            self.count += len(data)
        return data
