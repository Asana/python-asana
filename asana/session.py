import requests
import requests_oauthlib

class AsanaOAuth2Session(requests_oauthlib.OAuth2Session):
    """Session class for making OAuth authenticated requests to Asana's API"""

    authorize_url = 'https://app.asana.com/-/oauth_authorize'
    token_url = 'https://app.asana.com/-/oauth_token'

    def __init__(self, client_secret=None, **kwargs):
        super(AsanaOAuth2Session, self).__init__(**kwargs)
        self.client_secret = client_secret

    def authorization_url(self):
        """Get a URL (and 'state' token) to redirect the user to for authentication"""
        return super(AsanaOAuth2Session, self).authorization_url(self.authorize_url)

    def fetch_token(self, **kwargs):
        """Exchange a code (and 'state' token) for a bearer token"""
        return super(AsanaOAuth2Session, self).fetch_token(self.token_url, client_secret=self.client_secret, **kwargs)
