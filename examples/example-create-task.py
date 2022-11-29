import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import asana
from six import print_

# Instructions
#
# 1. Set your ASANA_ACCESS_TOKEN environment variable to a Personal Access Token obtained in your Asana Account Settings
#
# This simple script asks the user to choose from their available Workspaces and then the first page (if more than a
# single page exists) of available projects in order to create a task in that project.
#

def user_select_option(message, options):
    option_lst = list(options)
    print_(message)
    for i, val in enumerate(option_lst):
        print_(i, ': ' + val['name'])
    index = int(input("Enter choice (default 0): ") or 0)
    return option_lst[index]


if 'ASANA_ACCESS_TOKEN' in os.environ:
    # create a client with a Personal Access Token
    client = asana.Client.access_token(os.environ['ASANA_ACCESS_TOKEN'])
    workspaces = client.workspaces.get_workspaces()

    workspace = user_select_option("Please choose a workspace", workspaces)

    projects = client.projects.get_projects({'workspace': workspace['gid']})

    project = user_select_option("Please choose a project", projects)

    result = client.tasks.create_task(
        workspace['gid'],
        {
            'name': 'Learn to use Nunchucks',
            'notes': 'Note: This is a test task created with the python-asana client.',
            'projects': [project['gid']]
        }
    )

    print_(json.dumps(result, indent=4))
