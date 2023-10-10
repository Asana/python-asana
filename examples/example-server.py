import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, request, session, redirect, render_template_string
import asana
import json

# OAuth Instructions:
#
# 1. create a new application in your Asana Account Settings ("App" panel)
# 2. set the redirect URL to "http://localhost:5000/auth/asana/callback" (or whichever port you choose)
# 3. set your ASANA_CLIENT_ID and ASANA_CLIENT_SECRET environment variables

# convience method to create a client with your credentials, and optionally a 'token'
def Client(**kwargs):
    return asana.Client.oauth(
        client_id=os.environ['ASANA_CLIENT_ID'],
        client_secret=os.environ['ASANA_CLIENT_SECRET'],
        redirect_uri='http://localhost:5000/auth/asana/callback',
        **kwargs
    )

app = Flask(__name__)

# main page (http://localhost:5000/)
@app.route("/")
def main():
    token = session.get('token', False)
    # if the user has a token they're logged in
    if token:
        # example request gets information about logged in user
        me = Client(token=token).users.get_user('me')
        return render_template_string('''
<script>
    window.opener.postMessage("success", "https://app.asana.com");
</script>
<p>Hello {{ name }}.</p>
<p><pre>{{ dump }}</pre></p>
<p><a href="/logout">Logout</a></p>''',
            name=me['name'],
            dump=json.dumps(me, indent=2)
        )
    # if we don't have a token show a "Sign in with Asana" button
    else:
        # get an authorization URL and anti-forgery "state" token
        (auth_url, state) = Client().session.authorization_url()
        # persist the state token in the user's session
        session['state'] = state
        # link the button to the authorization URL
        return render_template_string('''
<p><a href="{{ auth_url }}"><img src="https://luna1.co/7df202.png"></a></p>''',
            auth_url=auth_url
        )

# logout endpoint
@app.route("/logout")
def logout():
    # delete the session token and redirect back to the main page
    del session['token']
    return redirect('/')

# OAuth callback endpoint
@app.route("/auth/asana/callback")
def auth_callback():
    # verify the state token matches to prevent CSRF attacks
    if request.args.get('state') == session['state']:
        del session['state']
        # exchange the code for a bearer token and persist it in the user's session or database
        session['token'] = Client().session.fetch_token(code=request.args.get('code'))
        return redirect('/')
    else:
        return "state doesn't match!"

app.secret_key = 'set this to something secret'

if __name__ == "__main__":
    app.run(debug=True)
