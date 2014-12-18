import asana
import os

client = asana.Client.basic_auth(os.environ['ASANA_API_KEY'])

print client.users.me()
