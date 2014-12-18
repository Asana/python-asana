import requests

class Dispatcher:

    def __init__(self, auth):
        self.session = requests.Session()
        self.rootURL = 'https://app.asana.com/api/1.0'
        self.auth = auth
        return

    def url(self, path):
        return self.rootURL + path

    def dispatch(self, method, path, options={}):
        options['auth'] = self.auth
        response = getattr(self.session, method)(self.url(path), **options)
        return response.json()['data']

    def get(self, path, query):
        return self.dispatch('get', path, { 'params': query })

    def post(self, path, data):
        return self.dispatch('post', path, { 'data': json.dumps(data), 'headers': {'content-type': 'application/json'}})

    def put(self, path, data):
        return self.dispatch('put', path, { 'data': json.dumps(data), 'headers': {'content-type': 'application/json'}})

    def delete(self, path):
        return self.dispatch('delete', path)
