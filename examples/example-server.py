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

app = Flask(__name__)

def Client(**kwargs):
    return asana.Client.oauth(
        client_id=os.environ['ASANA_CLIENT_ID'],
        client_secret=os.environ['ASANA_CLIENT_SECRET'],
        redirect_uri='http://localhost:5000/auth/asana/callback',
        **kwargs
    )

@app.route("/")
def main():
    token = session.get('token', False)
    if token:
        me = Client(token=token).users.me()
        return render_template_string('''
<img src="{{ image_url }}">
<p>Hello {{ name }}.</p>
<p><pre>{{ dump }}</pre></p>
<p><a href="/logout">Logout</a></p>''',
            name=me['name'],
            image_url=me['photo']['image_60x60'],
            dump=json.dumps(me, indent=2)
        )
    else:
        (auth_url, state) = Client().session.authorization_url()
        session['state'] = state
        return render_template_string('''
<p><a href="{{ auth_url }}"><img src="http://developer.asana.com/api/asana-oauth-button-blue.png"></a></p>''',
            auth_url=auth_url
        )

@app.route("/logout")
def logout():
    del session['token']
    return redirect('/')

@app.route("/auth/asana/callback")
def auth_callback():
    if request.args.get('state') == session['state']:
        del session['state']
        session['token'] = Client().session.fetch_token(code=request.args.get('code'))
        return redirect('/')
    else:
        return "state doesn't match!"

app.secret_key = 'set this to something secret'

if __name__ == "__main__":
    app.run(debug=True)
