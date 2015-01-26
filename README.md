asana
=====

Python client library for Asana.

Authentication
--------------

### Basic Auth

Create a client using your Asana API key:

    client = asana.Client.basic_auth('ASANA_API_KEY')

### OAuth 2

Asana supports OAuth 2. `asana` handles some of the details of the OAuth flow for you.

Create a client using your OAuth Client ID and secret:

    client = asana.Client.oauth(
      client_id='ASANA_CLIENT_ID',
      client_secret='ASANA_CLIENT_SECRET',
      redirect_uri='https://yourapp.com/auth/asana/callback'
    )

Redirect the user to the authorization URL obtained from the client's `session` object:

    (url, state) = client.session.authorization_url()

When the user is redirected back to your callback, check the `state` URL parameter matches, then pass the `code` parameter to obtain a bearer token:

    if request.params['state'] == state:
      token = client.session.fetch_token(code=request.params['code'])
      # ...
    else:
      # error! possible CSRF attack

Note: if you're writing a non-browser-based application (e.x. a command line tool) you can use the special redirect URI `urn:ietf:wg:oauth:2.0:oob` to prompt the user to copy and paste the code into the application.

Usage
-----

The client's methods are divided into several resources: `attachments`, `events`, `projects`, `stories`, `tags`, `tasks`, `teams`, `users`, and `workspaces`.

Methods that return a single object return that object directly:

    me = client.users.me()
    print "Hello " + me['name']

    workspace_id = me['workspaces'][0]['id']
    project = client.projects.create_in_workspace(workspace_id, { 'name': 'new project' })
    print "Created project with id: " + project['id']

Methods that return multiple items (e.x. `find_all`) return a page iterator by default. See the "Collections" section

Options
-------

Various options can be set globally on the `Client.DEFAULTS` object, per-client on `client.options`, or per-request as additional named arguments. For example:

    # global:
    asana.Client.DEFAULTS['limit'] = 1000

    # per-client:
    client.options['limit'] = 1000

    # per-request:
    client.tasks.find_all({ 'project': 1234 }, limit=1000)

### Available options

* `base_url` (default: "https://app.asana.com/api/1.0"): API endpoint base URL to connect to
* `max_retries` (default: 5): number to times to retry if API rate limit is reached or a server error occures. Rate limit retries delay until the rate limit expires, server errors exponentially backoff starting with a 1 second delay.
* `full_payload` (default: False): return the entire JSON response instead of the 'data' propery (default for collection methods and `events.get`)
* `fields` and `expand`: see [API documentation](http://developer.asana.com/documentation/#Options)

Collections (methods returning an array as it's 'data' property):

* `iterator_type` (default: "pages"): specifies which type of iterator (or not) to return. Valid values are "pages", "items", and `None`.
* `limit` (default: 100): limits the number of items of a collection to return (`None` can be provided)
* `offset`: offset token returned by previous calls to the same method (in `response['next_page']['offset']`)

Events:

* `poll_interval` (default: 5): polling interval for getting new events via `events.get_next` and `events.get_iterator`
* `sync`: sync token returned by previous calls to `events.get` (in `response['sync']`)

Collections
-----------

### Page Iterator

By default, methods that return a collection of objects return a page iterator with a page size of 100.

    page_iterator = client.workspaces.find_all(limit=1)
    print page_iterator.next() # a list of items in the page
    print page_iterator.next() # raises StopIteration if there are no more pages

Or:

    for page_items in client.workspaces.find_all()
      print page_items

You can also get the next page's offset token from the iterator, then later provide that token to resume at the next page:

    page_iterator = client.workspaces.find_all(limit=1)
    page_iterator.next()
    offset = page_iterator.next_page['offset']
    # ...
    for page_items in client.workspaces.find_all(limit=1, offset=offset):
        print page_items

### Items Iterator

If you pass the "iterator_type" option equal to "items" the method will return an iterator for individual items in the collection rather than pages. Internally it fetches one page at a time according to the "limit" option (default: 100).

    for item in client.workspaces.find_all()
      print item

