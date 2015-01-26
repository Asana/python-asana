import requests
import requests_oauthlib

class AsanaOAuth2Session(requests_oauthlib.OAuth2Session):
    authorize_url = 'https://app.asana.com/-/oauth_authorize'
    token_url = 'https://app.asana.com/-/oauth_token'

    def __init__(self, client_secret=None, **kwargs):
        super(AsanaOAuth2Session, self).__init__(**kwargs)
        self.client_secret = client_secret

    def fetch_token(self, **kwargs):
        return super(AsanaOAuth2Session, self).fetch_token(self.token_url, client_secret=self.client_secret, **kwargs)

    def authorization_url(self):
        return super(AsanaOAuth2Session, self).authorization_url(self.authorize_url)
