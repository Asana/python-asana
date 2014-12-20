import asana
import os
import urlparse
import sys
import json

if 'ASANA_API_KEY' in os.environ:
    client = asana.Client.basic_auth(os.environ['ASANA_API_KEY'])
    print client.users.me()

if 'ASANA_CLIENT_ID' in os.environ:
    client = asana.Client.oauth(
        client_id=os.environ['ASANA_CLIENT_ID'],
        client_secret=os.environ['ASANA_CLIENT_SECRET'],
        redirect_uri='http://localhost:5000/auth/asana/callback'
    )
    print "authorized=", client.session.authorized

    (url, state) = client.session.authorization_url()
    print "state=", state
    print "Open the following URL in a browser to authorize:"
    print url

    print "Paste the redirected URL and press enter:"
    redirected_url = sys.stdin.readline().strip()
    print redirected_url
    code = urlparse.parse_qs(urlparse.urlparse(redirected_url).query)['code'][0]

    token = client.session.fetch_token(code=code)

    print "token=", json.dumps(token)
    print "authorized=", client.session.authorized
    print "me=", client.users.me()

    os.environ['ASANA_TOKEN'] = json.dumps(token) # (see below)

if 'ASANA_TOKEN' in os.environ:
    client = asana.Client.oauth(
        client_id=os.environ['ASANA_CLIENT_ID'],
        token=json.loads(os.environ['ASANA_TOKEN'])
    )
    print "authorized=", client.session.authorized
    print "me=", client.users.me()
