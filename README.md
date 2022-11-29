# asana [![Build][github-actions-image]][github-actions-url] [![PyPi Version][pypi-image]][pypi-url]

Python client library for Asana.

Authentication
--------------

### Personal Access Token

Create a client using your Asana Personal Access Token:

    client = asana.Client.access_token('PERSONAL_ACCESS_TOKEN')

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

The client's methods are divided into several resources: `attachments`, `events`, `jobs`, `portfolios`, `portfolio_memberships`, `projects`, `project_memberships`, `stories`, `tags`, `tasks`, `teams`, `users`, `user_task_lists`, and `workspaces`.

Methods that return a single object return that object directly:

    me = client.users.get_user('me')
    print "Hello " + me['name']

    workspace_id = me['workspaces'][0]['gid']
    project = client.projects.create_in_workspace(workspace_id, { 'name': 'new project' })
    print "Created project with id: " + project['gid']

Methods that return multiple items (e.x. `get_tasks`, `get_projects`, `get_portfolios`, etc.) return a page iterator by default. See the "Collections" section.

#### See [the gen folder](asana/resources/gen) for methods available for each resource. 

Options
-------

Various options can be set globally on the `Client.DEFAULTS` object, per-client on `client.options`, or per-request as additional named arguments. For example:

    # global:
    asana.Client.DEFAULT_OPTIONS['page_size'] = 100

    # per-client:
    client.options['page_size'] = 100

    # per-request:
    client.tasks.get_tasks({ 'project': 1234 }, page_size=100)

### Available options

* `base_url` (default: "https://app.asana.com/api/1.0"): API endpoint base URL to connect to
* `max_retries` (default: 5): number to times to retry if API rate limit is reached or a server error occures. Rate limit retries delay until the rate limit expires, server errors exponentially backoff starting with a 1 second delay.
* `full_payload` (default: False): return the entire JSON response instead of the 'data' propery (default for collection methods and `events.get`)
* `fields` and `expand`: see [API documentation](https://asana.com/developers/documentation/getting-started/input-output-options)

Collections (methods returning an array as its 'data' property):

* `iterator_type` (default: "items"): specifies which type of iterator (or not) to return. Valid values are "items" and `None`.
* `item_limit` (default: None): limits the number of items of a collection to return.
* `page_size` (default: 50): limits the number of items per page to fetch at a time.
* `offset`: offset token returned by previous calls to the same method (in `response['next_page']['offset']`)

Events:

* `poll_interval` (default: 5): polling interval for getting new events via `events.get_next` and `events.get_iterator`
* `sync`: sync token returned by previous calls to `events.get` (in `response['sync']`)

### Asana Change Warnings

You will receive warning logs if performing requests that may be affected by a deprecation. The warning contains a link that explains the deprecation.

If you receive one of these warnings, you should:
* Read about the deprecation.
* Resolve sections of your code that would be affected by the deprecation.
* Add the deprecation flag to your "asana-enable" header.

You can place it on the client for all requests, or place it on a single request.

    client.headers={'asana-enable': 'string_ids'}
    or
    me = client.users.get_user('me', headers={'asana-enable': 'string_ids'})

If you would rather suppress these warnings, you can set

    client.LOG_ASANA_CHANGE_WARNINGS = False

Collections
-----------

### Items Iterator

By default, methods that return a collection of objects return an item iterator:

    workspaces = client.workspaces.get_workspaces(item_limit=1)
    print workspaces.next()
    print workspaces.next() # raises StopIteration if there are no more items

Or:

    for workspace in client.workspaces.get_workspaces()
      print workspace

### Raw API

You can also use the raw API to fetch a page at a time:

    offset = None
    while True:
      page = client.workspaces.get_workspaces(offset=offset, iterator_type=None)
      print page['data']
      if 'next_page' in page:
        offset = page['next_page']['offset']
      else:
        break

Contributing
------------

Feel free to fork and submit pull requests for the code! Please follow the
existing code as an example of style and make sure that all your code passes
lint and tests.

### Code generation

The specific Asana resource classes under `gen` (`_Tag`, `_Workspace`, `_Task`, etc) are
generated code, hence they shouldn't be modified by hand.

### Deployment

**Repo Owners Only.** Take the following steps to issue a new release of the library.

#### Automatic Deployment

Run `deploy.py [major|minor|patch]`. See `deploy.py -h` for additional info.

#### Manual Deployment

  1. Merge in the desired changes into the `master` branch and commit them.
  2. Clone the repo, work on master.
  3. Edit package version in `asana/__init__.py` and `./VERSION` to indicate the [semantic version](http://semver.org/) change.
  4. Commit the change
  5. Tag the commit with `v` plus the same version number you set in the file.
     `git tag v1.2.3`
  6. Push changes to origin, including tags:
     `git push origin master --tags`

GitHub Actions will automatically build and deploy the tagged release to [PyPI](https://pypi.org/).

[github-actions-url]: https://github.com/Asana/python-asana/actions
[github-actions-image]: https://github.com/Asana/python-asana/workflows/Build/badge.svg

[pypi-url]: https://pypi.python.org/pypi/asana/
[pypi-image]: https://img.shields.io/pypi/v/asana.svg?style=flat-square

[asana-docs]: https://developers.asana.com/docs
