
from .error import InvalidTokenError
import time

class PageIterator(object):
    def __init__(self, client, path, query, options):
        self.client = client
        self.path = path
        self.query = query
        self.options = client._merge_options(options, { 'full_payload': True })

        self.continuation = False

    def __getattr__(self, name):
        if name == self.CONTINUATION_KEY:
            return self.continuation
        raise AttributeError("%r object has no attribute %r" % (self.__class__, attr))

    def __iter__(self):
        return self

    def __next__(self):
        if self.continuation == None:
            raise StopIteration
        elif self.continuation == False:
            result = self.get_initial()
        else:
            result = self.get_next()
        self.continuation = result.get(self.CONTINUATION_KEY, None)
        return result.get('data', None)

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
        self.options.pop('offset', None) # if offset was set delete it because it will conflict
        return self.client.get(self.continuation['path'], {}, **self.options)


class EventsPageIterator(PageIterator):
    CONTINUATION_KEY = 'sync'

    def get_initial(self):
        if 'sync' not in self.query:
            try:
                self.client.events.get(self.query)
            except InvalidTokenError as e:
                self.continuation = e.sync
        else:
            self.continuation = self.query['sync']
        return self.get_next()

    def get_next(self):
        self.query['sync'] = self.continuation
        return self.client.events.get(self.query)

    def __next__(self):
        while True:
            results = super(EventsPageIterator, self).__next__()
            if len(results) > 0:
                return results
            else:
                time.sleep(self.options['poll_interval'])
