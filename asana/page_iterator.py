
from .error import InvalidTokenError
import time

class PageIterator(object):
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
        if name == self.CONTINUATION_KEY:
            return self.continuation
        raise AttributeError("%r object has no attribute %r" % (self.__class__, attr))

    def __iter__(self):
        return self

    def __next__(self):
        self.options['limit'] = min(self.page_size, self.item_limit - self.count)

        if self.continuation == None or self.options['limit'] == 0:
            raise StopIteration
        elif self.continuation == False:
            result = self.get_initial()
        else:
            result = self.get_next()
        self.continuation = result.get(self.CONTINUATION_KEY, None)
        data = result.get('data', None)
        if data != None:
            self.count += len(data)
        return data

    def next(self):
        return self.__next__()

    def items(self):
        for page in self:
            for item in page:
                yield item
        raise StopIteration


class CollectionPageIterator(PageIterator):
    CONTINUATION_KEY = 'next_page'

    def get_initial(self):
        return self.client.get(self.path, self.query, **self.options)

    def get_next(self):
        self.options['offset'] = self.continuation['offset']
        return self.client.get(self.path, self.query, **self.options)


class EventsPageIterator(PageIterator):
    CONTINUATION_KEY = 'sync'

    def get_initial(self):
        if 'sync' not in self.query:
            try:
                self.client.events.get(self.query, **self.options)
            except InvalidTokenError as e:
                self.continuation = e.sync
        else:
            self.continuation = self.query['sync']
        return self.get_next()

    def get_next(self):
        self.query['sync'] = self.continuation
        return self.client.events.get(self.query, **self.options)

    def __next__(self):
        while True:
            results = super(EventsPageIterator, self).__next__()
            if len(results) > 0:
                return results
            else:
                time.sleep(self.options['poll_interval'])
