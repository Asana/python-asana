# asana [![Build Status][travis-image]][travis-url] [![PyPi Version][pypi-image]][pypi-url]

Python client library for Asana.

Required: Security procedures for outdated OpenSSL versions
--------------

Older versions of OpenSSL can cause a problem when using `python-asana` In particular, at the time of this writing, at least **MacOS X 10.11 and below** ship with a very old version of OpenSSL:
    
    $ openssl version
    OpenSSL 0.9.8zh 14 Jan 2016

OpenSSL 0.9.8 was first released in 2005, and therefore only supports TLS (Transport Layer Security) version 1.0. Asana has deprecated and stopped accepting requests for clients which do not suport [TLS 1.0 and above](https://asa.na/tls), which unfortunately includes any software linked against this version of the library - this includes both the MacOS X provided Python interpreter and any homebrew installed Python that is not specifically configured to link against a newer version.

To see if your Python version is affected, run
   
    $ python -c "import ssl; print ssl.OPENSSL_VERSION"

If the version printed at the command line is older than `1.0.1`, when, in 2012, OpenSSL first supported TLS 1.1 and 1.2, you will not be able to use `python-asana` to connect to Asana. Specifically, you will recieve `400 Bad Request` responses with an error message in the response body about the lack of support for TLS 1.1 and above.

Fortunately, homebrew makes it easy to install both an updated OpenSSL and a Python interpreter that links to it. Run

    $ brew install openssl
      ...                                               # homebrew installs
    $ /usr/local/Cellar/openssl/*/bin/openssl version   # Just to verify...
    OpenSSL 1.0.2h  3 May 2016

Finally, you have to install the homebrew version of python which links against the newer OpenSSL

    $ brew install python --with-brewed-openssl
      ...                                                 # homebrew installs
    $ python -c "import ssl; print ssl.OPENSSL_VERSION"   # Verify inside Python
    OpenSSL 1.0.2h  3 May 2016

If you see the version of OpenSSL greater than OpenSSL 1.0.1, then you're all set to start using `python-asana`

Similarly, if you're not using a homebrew version of Python (e.g. using macports or manually compiling) you'll have to make sure that your installation of Python is using an up-to-date version of OpenSSL. **Note**: this does _not_ apply to using `virtualenv`; `virtualenv` manages Python packages, but uses the system python and its standard library packages, including OpenSSL.

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

The client's methods are divided into several resources: `attachments`, `events`, `projects`, `stories`, `tags`, `tasks`, `teams`, `users`, and `workspaces`.

Methods that return a single object return that object directly:

    me = client.users.me()
    print "Hello " + me['name']

    workspace_id = me['workspaces'][0]['id']
    project = client.projects.create_in_workspace(workspace_id, { 'name': 'new project' })
    print "Created project with id: " + project['id']

Methods that return multiple items (e.x. `find_all`) return a page iterator by default. See the "Collections" section.

#### See [the gen folder](asana/resources/gen) for methods available for each resource. 

Options
-------

Various options can be set globally on the `Client.DEFAULTS` object, per-client on `client.options`, or per-request as additional named arguments. For example:

    # global:
    asana.Client.DEFAULTS['page_size'] = 100

    # per-client:
    client.options['page_size'] = 100

    # per-request:
    client.tasks.find_all({ 'project': 1234 }, page_size=100)

### Available options

* `base_url` (default: "https://app.asana.com/api/1.0"): API endpoint base URL to connect to
* `max_retries` (default: 5): number to times to retry if API rate limit is reached or a server error occures. Rate limit retries delay until the rate limit expires, server errors exponentially backoff starting with a 1 second delay.
* `full_payload` (default: False): return the entire JSON response instead of the 'data' propery (default for collection methods and `events.get`)
* `fields` and `expand`: see [API documentation](https://asana.com/developers/documentation/getting-started/input-output-options)

Collections (methods returning an array as it's 'data' property):

* `iterator_type` (default: "items"): specifies which type of iterator (or not) to return. Valid values are "items" and `None`.
* `item_limit` (default: None): limits the number of items of a collection to return.
* `page_size` (default: 50): limits the number of items per page to fetch at a time.
* `offset`: offset token returned by previous calls to the same method (in `response['next_page']['offset']`)

Events:

* `poll_interval` (default: 5): polling interval for getting new events via `events.get_next` and `events.get_iterator`
* `sync`: sync token returned by previous calls to `events.get` (in `response['sync']`)

Collections
-----------

### Items Iterator

By default, methods that return a collection of objects return an item iterator:

    workspaces = client.workspaces.find_all(item_limit=1)
    print workspaces.next()
    print workspaces.next() # raises StopIteration if there are no more items

Or:

    for workspace in client.workspaces.find_all()
      print workspace

### Raw API

You can also use the raw API to fetch a page at a time:

    offset = None
    while True:
      page = client.workspaces.find_all(offset=offset, iterator_type=None)
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
generated code, hence they shouldn't be modified by hand. See the [asana-api-meta][meta] repo for details.

### Deployment

**Repo Owners Only.** Take the following steps to issue a new release of the library.

#### Automatic Deployment

Run `deploy.py [version]`. See `deploy.py -h` for additional info.

#### Manual Deployment

  1. Merge in the desired changes into the `master` branch and commit them.
  2. Clone the repo, work on master.
  3. Edit package version in `asana/__init__.py` to indicate the [semantic version](http://semver.org/) change.
  4. Commit the change
  5. Tag the commit with `v` plus the same version number you set in the file.
     `git tag v1.2.3`
  6. Push changes to origin, including tags:
     `git push origin master --tags`

Travis CI will automatically build and deploy the tagged release to `pypi`.

[travis-url]: http://travis-ci.org/Asana/python-asana
[travis-image]: https://api.travis-ci.org/Asana/python-asana.svg?style=flat-square&branch=master

[pypi-url]: https://pypi.python.org/pypi/asana/
[pypi-image]: https://img.shields.io/pypi/v/asana.svg?style=flat-square
