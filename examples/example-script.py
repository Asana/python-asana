import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import asana
import json
from six import print_

# API Key Instructions:
#
# 1. set your ASANA_API_KEY environment variable to the API key found in Asana Account Settings
#
# OAuth Instructions:
#
# 1. create a new application in your Asana Account Settings ("App" panel)
# 2. set the redirect URL to "urn:ietf:wg:oauth:2.0:oob"
# 3. set your ASANA_CLIENT_ID and ASANA_CLIENT_SECRET environment variables

if 'ASANA_CLIENT_ID' in os.environ:
    # create a client with the OAuth credentials:
    client = asana.Client.oauth(
        client_id=os.environ['ASANA_CLIENT_ID'],
        client_secret=os.environ['ASANA_CLIENT_SECRET'],
        # this special redirect URI will prompt the user to copy/paste the code.
        # useful for command line scripts and other non-web apps
        redirect_uri='urn:ietf:wg:oauth:2.0:oob'
    )
    print_("authorized=", client.session.authorized)

    # get an authorization URL:
    (url, state) = client.session.authorization_url()
    try:
        # in a web app you'd redirect the user to this URL when they take action to
        # login with Asana or connect their account to Asana
        import webbrowser
        webbrowser.open(url)
    except Exception as e:
        print_("Open the following URL in a browser to authorize:")
        print_(url)

    print_("Copy and paste the returned code from the browser and press enter:")

    code = sys.stdin.readline().strip()
    # exchange the code for a bearer token
    token = client.session.fetch_token(code=code)

    print_("token=", json.dumps(token))
    print_("authorized=", client.session.authorized)
    print_("me=", client.users.me())

    # normally you'd persist this token somewhere
    os.environ['ASANA_TOKEN'] = json.dumps(token) # (see below)

if 'ASANA_TOKEN' in os.environ:
    # create a client with your OAuth client ID and a previously obtained bearer token
    client = asana.Client.oauth(
        client_id=os.environ['ASANA_CLIENT_ID'],
        token=json.loads(os.environ['ASANA_TOKEN'])
    )
    print_("authorized=", client.session.authorized)
    print_("me=", client.users.me())

if 'ASANA_API_KEY' in os.environ:
    # create a client with your Asana API key
    client = asana.Client.basic_auth(os.environ['ASANA_API_KEY'])
    me = client.users.me()
    print_("me=" + json.dumps(me, indent=2))

    # find your "Personal Projects" project
    personal_projects = next(workspace for workspace in me['workspaces'] if workspace['name'] == 'Personal Projects')
    projects = client.projects.find_by_workspace(personal_projects['id'], iterator_type=None)
    print_("personal projects=" + json.dumps(projects, indent=2))

    # create a "demo project" if it doesn't exist
    try:
        project = next(project for project in projects if project['name'] == 'demo project')
    except Exception, e:
        print_("creating 'demo project'")
        project = client.projects.create_in_workspace(personal_projects['id'], { 'name': 'demo project' })
    print_("project=", project)

    # start streaming modifications to the demo project.
    # make some changes in Asana to see this working
    print_("starting streaming events for " + project['name'])
    for event in client.events.get_iterator({ 'resource': project['id'] }):
        print_("event", event)
