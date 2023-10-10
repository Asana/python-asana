import asana
import json
from datetime import date
import argparse
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def summarize(client, project_id, post_project):
    """
    Collect data from project_id, and create a summary task in the post_project.
    """
    # Get info on the project
    project = client.projects.get_project(project_id)

    # Loop through the tasks, collecting data
    all_tasks = 0
    tasks_completed = 0
    tasks = client.tasks.get_tasks_for_project(project_id, opt_fields=['completed'])
    for task in tasks:
        all_tasks += 1
        if task['completed']:
            tasks_completed += 1
        
    # Make the summary task
    summary_task_fields = {
        'projects': [post_project],
        'name': "{} Summary of \"{}\"".format(
            date.today().isoformat(), project['name']),
        'notes': "{} tasks\n{} ({:.0%}) tasks completed".format(
            all_tasks, tasks_completed, tasks_completed / all_tasks)
    }
    client.tasks.create_task(**summary_task_fields)

def main():
    """
    Parse arguments, authorize user, and summarize each given project.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("project_to_summarize",
        help="project id of project to summarize")
    parser.add_argument("summary_project",
        help="project id of summary project to post to")
    args = parser.parse_args()

    # Use OAuth
    # check if the user has an existing token stored.
    authorized = False
    client = None
    if 'ASANA_CLIENT_ID' in os.environ and 'ASANA_TOKEN' in os.environ:
        # create a client with your OAuth client ID and a previously obtained 
        # bearer token
        client = asana.Client.oauth(
            client_id=os.environ['ASANA_CLIENT_ID'],
            token=json.loads(os.environ['ASANA_TOKEN'])
        )
        print("authorized=", client.session.authorized)

        # try to get something to see if token has not expired.
        try:
            client.users.get_user('me')
            authorized = True
        except:
            print("token expired. please update ASANA_TOKEN")

    # check if the user has the secret
    if not authorized and 'ASANA_CLIENT_ID' in os.environ and 'ASANA_CLIENT_SECRET' in os.environ:
        # create a client with the OAuth credentials:
        client = asana.Client.oauth(
            client_id=os.environ['ASANA_CLIENT_ID'],
            client_secret=os.environ['ASANA_CLIENT_SECRET'],
            # this special redirect URI will prompt the user to copy/paste the code
            # useful for command line scripts and other non-web apps
            redirect_uri='urn:ietf:wg:oauth:2.0:oob'
        )

        # get an authorization URL:
        (url, state) = client.session.authorization_url()
        try:
            # in a web app you'd redirect the user to this URL when they take 
            # action to login with Asana or connect their account to Asana
            import webbrowser
            webbrowser.open(url)
        except Exception as e:
            print("Open the following URL in a browser to authorize:")
            print(url)

        print("Copy and paste the returned code from the browser and press enter:")

        code = sys.stdin.readline().strip()
        # exchange the code for a bearer token will fail on incorrect code
        token = client.session.fetch_token(code=code)

        print("token=", json.dumps(token))

        # normally you'd persist this token somewhere
        os.environ['ASANA_TOKEN'] = json.dumps(token) # (see below)

    if not client or not client.session.authorized:
        print("COULD NOT AUTHORIZE")
        exit(1)

    # Summarize the project.
    summarize(client, args.project_to_summarize, args.summary_project)

if __name__ == '__main__':
    main()
