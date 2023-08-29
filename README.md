# asana [![GitHub release][release-image]]() [![Build][github-actions-image]][github-actions-url] [![PyPi Version][pypi-image]][pypi-url]

Python client library for Asana

- API version: 1.0
- Package version: 4.0.9

## Requirements.

Python 3.4+

## Installation & Usage
### pip install from [PyPI](https://pypi.org/project/asana/)

```sh
pip install asana
```

Then import the package:
```python
import asana 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import asana
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
users_api_instance = asana.UsersApi(api_client)
user_gid = 'me' # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
opt_fields = ["email","name","photo","photo.image_1024x1024","photo.image_128x128","photo.image_21x21","photo.image_27x27","photo.image_36x36","photo.image_60x60","workspaces","workspaces.name"] # list[str] | Properties to include in the response. Set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a user
    api_response = users_api_instance.get_user(user_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Example: GET, POST, PUT, DELETE on tasks

#### GET - get multiple tasks
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tasks_api_instance = asana.TasksApi(api_client)
limit = 50
project = "<YOUR_PROJECT_GID>"
opt_fields = [
    "assignee_section",
    "due_at",
    "name",
    "completed_at",
    "completed_by",
    "tags",
    "dependents",
    "hearts",
    "liked",
    "projects",
    "completed",
    "num_hearts",
    "permalink_url",
    "parent",
    "assignee",
    "assignee_status",
    "num_subtasks",
    "start_on",
    "dependencies",
    "is_rendered_as_separator",
    "modified_at",
    "approval_status",
    "notes",
    "memberships",
    "workspace",
    "due_on",
    "hearted",
    "created_at",
    "likes",
    "num_likes",
    "custom_fields",
    "external",
    "html_notes",
    "followers",
    "start_at",
    "resource_subtype",
    "actual_time_minutes",
]

try:
    # GET - get multiple tasks
    api_response = tasks_api_instance.get_tasks(
        limit=limit, project=project, opt_fields=opt_fields
    )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

#### POST - create a task
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tasks_api_instance = asana.TasksApi(api_client)
body = asana.TasksBody(
    {
        "name": "New Task",
        "projects": ["<YOUR_PROJECT_GID>"],
    }
)

try:
    # POST - create a task
    api_response = tasks_api_instance.create_task(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->create_task: %s\n" % e)
```

#### PUT - update a task
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tasks_api_instance = asana.TasksApi(api_client)
task_gid = "<YOUR_TASK_GID>"
body = asana.TasksBody(
    {
        "name": "Updated Task",
    }
)

try:
    # PUT - update a task
    api_response = tasks_api_instance.update_task(body, task_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->update_task: %s\n" % e)
```

#### DELETE - delete a task
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tasks_api_instance = asana.TasksApi(api_client)
task_gid = "<YOUR_TASK_GID>"

try:
    # DELETE - delete a task
    api_response = tasks_api_instance.delete_task(task_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->delete_task: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://app.asana.com/api/1.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AttachmentsApi* | [**create_attachment_for_object**](docs/AttachmentsApi.md#create_attachment_for_object) | **POST** /attachments | Upload an attachment
*AttachmentsApi* | [**delete_attachment**](docs/AttachmentsApi.md#delete_attachment) | **DELETE** /attachments/{attachment_gid} | Delete an attachment
*AttachmentsApi* | [**get_attachment**](docs/AttachmentsApi.md#get_attachment) | **GET** /attachments/{attachment_gid} | Get an attachment
*AttachmentsApi* | [**get_attachments_for_object**](docs/AttachmentsApi.md#get_attachments_for_object) | **GET** /attachments | Get attachments from an object
*AuditLogAPIApi* | [**get_audit_log_events**](docs/AuditLogAPIApi.md#get_audit_log_events) | **GET** /workspaces/{workspace_gid}/audit_log_events | Get audit log events
*BatchAPIApi* | [**create_batch_request**](docs/BatchAPIApi.md#create_batch_request) | **POST** /batch | Submit parallel requests
*CustomFieldSettingsApi* | [**get_custom_field_settings_for_portfolio**](docs/CustomFieldSettingsApi.md#get_custom_field_settings_for_portfolio) | **GET** /portfolios/{portfolio_gid}/custom_field_settings | Get a portfolio&#x27;s custom fields
*CustomFieldSettingsApi* | [**get_custom_field_settings_for_project**](docs/CustomFieldSettingsApi.md#get_custom_field_settings_for_project) | **GET** /projects/{project_gid}/custom_field_settings | Get a project&#x27;s custom fields
*CustomFieldsApi* | [**create_custom_field**](docs/CustomFieldsApi.md#create_custom_field) | **POST** /custom_fields | Create a custom field
*CustomFieldsApi* | [**create_enum_option_for_custom_field**](docs/CustomFieldsApi.md#create_enum_option_for_custom_field) | **POST** /custom_fields/{custom_field_gid}/enum_options | Create an enum option
*CustomFieldsApi* | [**delete_custom_field**](docs/CustomFieldsApi.md#delete_custom_field) | **DELETE** /custom_fields/{custom_field_gid} | Delete a custom field
*CustomFieldsApi* | [**get_custom_field**](docs/CustomFieldsApi.md#get_custom_field) | **GET** /custom_fields/{custom_field_gid} | Get a custom field
*CustomFieldsApi* | [**get_custom_fields_for_workspace**](docs/CustomFieldsApi.md#get_custom_fields_for_workspace) | **GET** /workspaces/{workspace_gid}/custom_fields | Get a workspace&#x27;s custom fields
*CustomFieldsApi* | [**insert_enum_option_for_custom_field**](docs/CustomFieldsApi.md#insert_enum_option_for_custom_field) | **POST** /custom_fields/{custom_field_gid}/enum_options/insert | Reorder a custom field&#x27;s enum
*CustomFieldsApi* | [**update_custom_field**](docs/CustomFieldsApi.md#update_custom_field) | **PUT** /custom_fields/{custom_field_gid} | Update a custom field
*CustomFieldsApi* | [**update_enum_option**](docs/CustomFieldsApi.md#update_enum_option) | **PUT** /enum_options/{enum_option_gid} | Update an enum option
*EventsApi* | [**get_events**](docs/EventsApi.md#get_events) | **GET** /events | Get events on a resource
*GoalRelationshipsApi* | [**add_supporting_relationship**](docs/GoalRelationshipsApi.md#add_supporting_relationship) | **POST** /goals/{goal_gid}/addSupportingRelationship | Add a supporting goal relationship
*GoalRelationshipsApi* | [**get_goal_relationship**](docs/GoalRelationshipsApi.md#get_goal_relationship) | **GET** /goal_relationships/{goal_relationship_gid} | Get a goal relationship
*GoalRelationshipsApi* | [**get_goal_relationships**](docs/GoalRelationshipsApi.md#get_goal_relationships) | **GET** /goal_relationships | Get goal relationships
*GoalRelationshipsApi* | [**remove_supporting_relationship**](docs/GoalRelationshipsApi.md#remove_supporting_relationship) | **POST** /goals/{goal_gid}/removeSupportingRelationship | Removes a supporting goal relationship
*GoalRelationshipsApi* | [**update_goal_relationship**](docs/GoalRelationshipsApi.md#update_goal_relationship) | **PUT** /goal_relationships/{goal_relationship_gid} | Update a goal relationship
*GoalsApi* | [**add_followers**](docs/GoalsApi.md#add_followers) | **POST** /goals/{goal_gid}/addFollowers | Add a collaborator to a goal
*GoalsApi* | [**create_goal**](docs/GoalsApi.md#create_goal) | **POST** /goals | Create a goal
*GoalsApi* | [**create_goal_metric**](docs/GoalsApi.md#create_goal_metric) | **POST** /goals/{goal_gid}/setMetric | Create a goal metric
*GoalsApi* | [**delete_goal**](docs/GoalsApi.md#delete_goal) | **DELETE** /goals/{goal_gid} | Delete a goal
*GoalsApi* | [**get_goal**](docs/GoalsApi.md#get_goal) | **GET** /goals/{goal_gid} | Get a goal
*GoalsApi* | [**get_goals**](docs/GoalsApi.md#get_goals) | **GET** /goals | Get goals
*GoalsApi* | [**get_parent_goals_for_goal**](docs/GoalsApi.md#get_parent_goals_for_goal) | **GET** /goals/{goal_gid}/parentGoals | Get parent goals from a goal
*GoalsApi* | [**remove_followers**](docs/GoalsApi.md#remove_followers) | **POST** /goals/{goal_gid}/removeFollowers | Remove a collaborator from a goal
*GoalsApi* | [**update_goal**](docs/GoalsApi.md#update_goal) | **PUT** /goals/{goal_gid} | Update a goal
*GoalsApi* | [**update_goal_metric**](docs/GoalsApi.md#update_goal_metric) | **POST** /goals/{goal_gid}/setMetricCurrentValue | Update a goal metric
*JobsApi* | [**get_job**](docs/JobsApi.md#get_job) | **GET** /jobs/{job_gid} | Get a job by id
*MembershipsApi* | [**create_membership**](docs/MembershipsApi.md#create_membership) | **POST** /memberships | Create a membership
*MembershipsApi* | [**delete_membership**](docs/MembershipsApi.md#delete_membership) | **DELETE** /memberships/{membership_gid} | Delete a membership
*MembershipsApi* | [**get_membership**](docs/MembershipsApi.md#get_membership) | **GET** /memberships/{membership_gid} | Get a membership
*MembershipsApi* | [**get_memberships**](docs/MembershipsApi.md#get_memberships) | **GET** /memberships | Get multiple memberships
*OrganizationExportsApi* | [**create_organization_export**](docs/OrganizationExportsApi.md#create_organization_export) | **POST** /organization_exports | Create an organization export request
*OrganizationExportsApi* | [**get_organization_export**](docs/OrganizationExportsApi.md#get_organization_export) | **GET** /organization_exports/{organization_export_gid} | Get details on an org export request
*PortfolioMembershipsApi* | [**get_portfolio_membership**](docs/PortfolioMembershipsApi.md#get_portfolio_membership) | **GET** /portfolio_memberships/{portfolio_membership_gid} | Get a portfolio membership
*PortfolioMembershipsApi* | [**get_portfolio_memberships**](docs/PortfolioMembershipsApi.md#get_portfolio_memberships) | **GET** /portfolio_memberships | Get multiple portfolio memberships
*PortfolioMembershipsApi* | [**get_portfolio_memberships_for_portfolio**](docs/PortfolioMembershipsApi.md#get_portfolio_memberships_for_portfolio) | **GET** /portfolios/{portfolio_gid}/portfolio_memberships | Get memberships from a portfolio
*PortfoliosApi* | [**add_custom_field_setting_for_portfolio**](docs/PortfoliosApi.md#add_custom_field_setting_for_portfolio) | **POST** /portfolios/{portfolio_gid}/addCustomFieldSetting | Add a custom field to a portfolio
*PortfoliosApi* | [**add_item_for_portfolio**](docs/PortfoliosApi.md#add_item_for_portfolio) | **POST** /portfolios/{portfolio_gid}/addItem | Add a portfolio item
*PortfoliosApi* | [**add_members_for_portfolio**](docs/PortfoliosApi.md#add_members_for_portfolio) | **POST** /portfolios/{portfolio_gid}/addMembers | Add users to a portfolio
*PortfoliosApi* | [**create_portfolio**](docs/PortfoliosApi.md#create_portfolio) | **POST** /portfolios | Create a portfolio
*PortfoliosApi* | [**delete_portfolio**](docs/PortfoliosApi.md#delete_portfolio) | **DELETE** /portfolios/{portfolio_gid} | Delete a portfolio
*PortfoliosApi* | [**get_items_for_portfolio**](docs/PortfoliosApi.md#get_items_for_portfolio) | **GET** /portfolios/{portfolio_gid}/items | Get portfolio items
*PortfoliosApi* | [**get_portfolio**](docs/PortfoliosApi.md#get_portfolio) | **GET** /portfolios/{portfolio_gid} | Get a portfolio
*PortfoliosApi* | [**get_portfolios**](docs/PortfoliosApi.md#get_portfolios) | **GET** /portfolios | Get multiple portfolios
*PortfoliosApi* | [**remove_custom_field_setting_for_portfolio**](docs/PortfoliosApi.md#remove_custom_field_setting_for_portfolio) | **POST** /portfolios/{portfolio_gid}/removeCustomFieldSetting | Remove a custom field from a portfolio
*PortfoliosApi* | [**remove_item_for_portfolio**](docs/PortfoliosApi.md#remove_item_for_portfolio) | **POST** /portfolios/{portfolio_gid}/removeItem | Remove a portfolio item
*PortfoliosApi* | [**remove_members_for_portfolio**](docs/PortfoliosApi.md#remove_members_for_portfolio) | **POST** /portfolios/{portfolio_gid}/removeMembers | Remove users from a portfolio
*PortfoliosApi* | [**update_portfolio**](docs/PortfoliosApi.md#update_portfolio) | **PUT** /portfolios/{portfolio_gid} | Update a portfolio
*ProjectBriefsApi* | [**create_project_brief**](docs/ProjectBriefsApi.md#create_project_brief) | **POST** /projects/{project_gid}/project_briefs | Create a project brief
*ProjectBriefsApi* | [**delete_project_brief**](docs/ProjectBriefsApi.md#delete_project_brief) | **DELETE** /project_briefs/{project_brief_gid} | Delete a project brief
*ProjectBriefsApi* | [**get_project_brief**](docs/ProjectBriefsApi.md#get_project_brief) | **GET** /project_briefs/{project_brief_gid} | Get a project brief
*ProjectBriefsApi* | [**update_project_brief**](docs/ProjectBriefsApi.md#update_project_brief) | **PUT** /project_briefs/{project_brief_gid} | Update a project brief
*ProjectMembershipsApi* | [**get_project_membership**](docs/ProjectMembershipsApi.md#get_project_membership) | **GET** /project_memberships/{project_membership_gid} | Get a project membership
*ProjectMembershipsApi* | [**get_project_memberships_for_project**](docs/ProjectMembershipsApi.md#get_project_memberships_for_project) | **GET** /projects/{project_gid}/project_memberships | Get memberships from a project
*ProjectStatusesApi* | [**create_project_status_for_project**](docs/ProjectStatusesApi.md#create_project_status_for_project) | **POST** /projects/{project_gid}/project_statuses | Create a project status
*ProjectStatusesApi* | [**delete_project_status**](docs/ProjectStatusesApi.md#delete_project_status) | **DELETE** /project_statuses/{project_status_gid} | Delete a project status
*ProjectStatusesApi* | [**get_project_status**](docs/ProjectStatusesApi.md#get_project_status) | **GET** /project_statuses/{project_status_gid} | Get a project status
*ProjectStatusesApi* | [**get_project_statuses_for_project**](docs/ProjectStatusesApi.md#get_project_statuses_for_project) | **GET** /projects/{project_gid}/project_statuses | Get statuses from a project
*ProjectTemplatesApi* | [**delete_project_template**](docs/ProjectTemplatesApi.md#delete_project_template) | **DELETE** /project_templates/{project_template_gid} | Delete a project template
*ProjectTemplatesApi* | [**get_project_template**](docs/ProjectTemplatesApi.md#get_project_template) | **GET** /project_templates/{project_template_gid} | Get a project template
*ProjectTemplatesApi* | [**get_project_templates**](docs/ProjectTemplatesApi.md#get_project_templates) | **GET** /project_templates | Get multiple project templates
*ProjectTemplatesApi* | [**get_project_templates_for_team**](docs/ProjectTemplatesApi.md#get_project_templates_for_team) | **GET** /teams/{team_gid}/project_templates | Get a team&#x27;s project templates
*ProjectTemplatesApi* | [**instantiate_project**](docs/ProjectTemplatesApi.md#instantiate_project) | **POST** /project_templates/{project_template_gid}/instantiateProject | Instantiate a project from a project template
*ProjectsApi* | [**add_custom_field_setting_for_project**](docs/ProjectsApi.md#add_custom_field_setting_for_project) | **POST** /projects/{project_gid}/addCustomFieldSetting | Add a custom field to a project
*ProjectsApi* | [**add_followers_for_project**](docs/ProjectsApi.md#add_followers_for_project) | **POST** /projects/{project_gid}/addFollowers | Add followers to a project
*ProjectsApi* | [**add_members_for_project**](docs/ProjectsApi.md#add_members_for_project) | **POST** /projects/{project_gid}/addMembers | Add users to a project
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /projects | Create a project
*ProjectsApi* | [**create_project_for_team**](docs/ProjectsApi.md#create_project_for_team) | **POST** /teams/{team_gid}/projects | Create a project in a team
*ProjectsApi* | [**create_project_for_workspace**](docs/ProjectsApi.md#create_project_for_workspace) | **POST** /workspaces/{workspace_gid}/projects | Create a project in a workspace
*ProjectsApi* | [**delete_project**](docs/ProjectsApi.md#delete_project) | **DELETE** /projects/{project_gid} | Delete a project
*ProjectsApi* | [**duplicate_project**](docs/ProjectsApi.md#duplicate_project) | **POST** /projects/{project_gid}/duplicate | Duplicate a project
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /projects/{project_gid} | Get a project
*ProjectsApi* | [**get_projects**](docs/ProjectsApi.md#get_projects) | **GET** /projects | Get multiple projects
*ProjectsApi* | [**get_projects_for_task**](docs/ProjectsApi.md#get_projects_for_task) | **GET** /tasks/{task_gid}/projects | Get projects a task is in
*ProjectsApi* | [**get_projects_for_team**](docs/ProjectsApi.md#get_projects_for_team) | **GET** /teams/{team_gid}/projects | Get a team&#x27;s projects
*ProjectsApi* | [**get_projects_for_workspace**](docs/ProjectsApi.md#get_projects_for_workspace) | **GET** /workspaces/{workspace_gid}/projects | Get all projects in a workspace
*ProjectsApi* | [**get_task_counts_for_project**](docs/ProjectsApi.md#get_task_counts_for_project) | **GET** /projects/{project_gid}/task_counts | Get task count of a project
*ProjectsApi* | [**project_save_as_template**](docs/ProjectsApi.md#project_save_as_template) | **POST** /projects/{project_gid}/saveAsTemplate | Create a project template from a project
*ProjectsApi* | [**remove_custom_field_setting_for_project**](docs/ProjectsApi.md#remove_custom_field_setting_for_project) | **POST** /projects/{project_gid}/removeCustomFieldSetting | Remove a custom field from a project
*ProjectsApi* | [**remove_followers_for_project**](docs/ProjectsApi.md#remove_followers_for_project) | **POST** /projects/{project_gid}/removeFollowers | Remove followers from a project
*ProjectsApi* | [**remove_members_for_project**](docs/ProjectsApi.md#remove_members_for_project) | **POST** /projects/{project_gid}/removeMembers | Remove users from a project
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /projects/{project_gid} | Update a project
*RulesApi* | [**trigger_rule**](docs/RulesApi.md#trigger_rule) | **POST** /rule_triggers/{rule_trigger_gid}/run | Trigger a rule
*SectionsApi* | [**add_task_for_section**](docs/SectionsApi.md#add_task_for_section) | **POST** /sections/{section_gid}/addTask | Add task to section
*SectionsApi* | [**create_section_for_project**](docs/SectionsApi.md#create_section_for_project) | **POST** /projects/{project_gid}/sections | Create a section in a project
*SectionsApi* | [**delete_section**](docs/SectionsApi.md#delete_section) | **DELETE** /sections/{section_gid} | Delete a section
*SectionsApi* | [**get_section**](docs/SectionsApi.md#get_section) | **GET** /sections/{section_gid} | Get a section
*SectionsApi* | [**get_sections_for_project**](docs/SectionsApi.md#get_sections_for_project) | **GET** /projects/{project_gid}/sections | Get sections in a project
*SectionsApi* | [**insert_section_for_project**](docs/SectionsApi.md#insert_section_for_project) | **POST** /projects/{project_gid}/sections/insert | Move or Insert sections
*SectionsApi* | [**update_section**](docs/SectionsApi.md#update_section) | **PUT** /sections/{section_gid} | Update a section
*StatusUpdatesApi* | [**create_status_for_object**](docs/StatusUpdatesApi.md#create_status_for_object) | **POST** /status_updates | Create a status update
*StatusUpdatesApi* | [**delete_status**](docs/StatusUpdatesApi.md#delete_status) | **DELETE** /status_updates/{status_update_gid} | Delete a status update
*StatusUpdatesApi* | [**get_status**](docs/StatusUpdatesApi.md#get_status) | **GET** /status_updates/{status_update_gid} | Get a status update
*StatusUpdatesApi* | [**get_statuses_for_object**](docs/StatusUpdatesApi.md#get_statuses_for_object) | **GET** /status_updates | Get status updates from an object
*StoriesApi* | [**create_story_for_task**](docs/StoriesApi.md#create_story_for_task) | **POST** /tasks/{task_gid}/stories | Create a story on a task
*StoriesApi* | [**delete_story**](docs/StoriesApi.md#delete_story) | **DELETE** /stories/{story_gid} | Delete a story
*StoriesApi* | [**get_stories_for_task**](docs/StoriesApi.md#get_stories_for_task) | **GET** /tasks/{task_gid}/stories | Get stories from a task
*StoriesApi* | [**get_story**](docs/StoriesApi.md#get_story) | **GET** /stories/{story_gid} | Get a story
*StoriesApi* | [**update_story**](docs/StoriesApi.md#update_story) | **PUT** /stories/{story_gid} | Update a story
*TagsApi* | [**create_tag**](docs/TagsApi.md#create_tag) | **POST** /tags | Create a tag
*TagsApi* | [**create_tag_for_workspace**](docs/TagsApi.md#create_tag_for_workspace) | **POST** /workspaces/{workspace_gid}/tags | Create a tag in a workspace
*TagsApi* | [**delete_tag**](docs/TagsApi.md#delete_tag) | **DELETE** /tags/{tag_gid} | Delete a tag
*TagsApi* | [**get_tag**](docs/TagsApi.md#get_tag) | **GET** /tags/{tag_gid} | Get a tag
*TagsApi* | [**get_tags**](docs/TagsApi.md#get_tags) | **GET** /tags | Get multiple tags
*TagsApi* | [**get_tags_for_task**](docs/TagsApi.md#get_tags_for_task) | **GET** /tasks/{task_gid}/tags | Get a task&#x27;s tags
*TagsApi* | [**get_tags_for_workspace**](docs/TagsApi.md#get_tags_for_workspace) | **GET** /workspaces/{workspace_gid}/tags | Get tags in a workspace
*TagsApi* | [**update_tag**](docs/TagsApi.md#update_tag) | **PUT** /tags/{tag_gid} | Update a tag
*TasksApi* | [**add_dependencies_for_task**](docs/TasksApi.md#add_dependencies_for_task) | **POST** /tasks/{task_gid}/addDependencies | Set dependencies for a task
*TasksApi* | [**add_dependents_for_task**](docs/TasksApi.md#add_dependents_for_task) | **POST** /tasks/{task_gid}/addDependents | Set dependents for a task
*TasksApi* | [**add_followers_for_task**](docs/TasksApi.md#add_followers_for_task) | **POST** /tasks/{task_gid}/addFollowers | Add followers to a task
*TasksApi* | [**add_project_for_task**](docs/TasksApi.md#add_project_for_task) | **POST** /tasks/{task_gid}/addProject | Add a project to a task
*TasksApi* | [**add_tag_for_task**](docs/TasksApi.md#add_tag_for_task) | **POST** /tasks/{task_gid}/addTag | Add a tag to a task
*TasksApi* | [**create_subtask_for_task**](docs/TasksApi.md#create_subtask_for_task) | **POST** /tasks/{task_gid}/subtasks | Create a subtask
*TasksApi* | [**create_task**](docs/TasksApi.md#create_task) | **POST** /tasks | Create a task
*TasksApi* | [**delete_task**](docs/TasksApi.md#delete_task) | **DELETE** /tasks/{task_gid} | Delete a task
*TasksApi* | [**duplicate_task**](docs/TasksApi.md#duplicate_task) | **POST** /tasks/{task_gid}/duplicate | Duplicate a task
*TasksApi* | [**get_dependencies_for_task**](docs/TasksApi.md#get_dependencies_for_task) | **GET** /tasks/{task_gid}/dependencies | Get dependencies from a task
*TasksApi* | [**get_dependents_for_task**](docs/TasksApi.md#get_dependents_for_task) | **GET** /tasks/{task_gid}/dependents | Get dependents from a task
*TasksApi* | [**get_subtasks_for_task**](docs/TasksApi.md#get_subtasks_for_task) | **GET** /tasks/{task_gid}/subtasks | Get subtasks from a task
*TasksApi* | [**get_task**](docs/TasksApi.md#get_task) | **GET** /tasks/{task_gid} | Get a task
*TasksApi* | [**get_tasks**](docs/TasksApi.md#get_tasks) | **GET** /tasks | Get multiple tasks
*TasksApi* | [**get_tasks_for_project**](docs/TasksApi.md#get_tasks_for_project) | **GET** /projects/{project_gid}/tasks | Get tasks from a project
*TasksApi* | [**get_tasks_for_section**](docs/TasksApi.md#get_tasks_for_section) | **GET** /sections/{section_gid}/tasks | Get tasks from a section
*TasksApi* | [**get_tasks_for_tag**](docs/TasksApi.md#get_tasks_for_tag) | **GET** /tags/{tag_gid}/tasks | Get tasks from a tag
*TasksApi* | [**get_tasks_for_user_task_list**](docs/TasksApi.md#get_tasks_for_user_task_list) | **GET** /user_task_lists/{user_task_list_gid}/tasks | Get tasks from a user task list
*TasksApi* | [**remove_dependencies_for_task**](docs/TasksApi.md#remove_dependencies_for_task) | **POST** /tasks/{task_gid}/removeDependencies | Unlink dependencies from a task
*TasksApi* | [**remove_dependents_for_task**](docs/TasksApi.md#remove_dependents_for_task) | **POST** /tasks/{task_gid}/removeDependents | Unlink dependents from a task
*TasksApi* | [**remove_follower_for_task**](docs/TasksApi.md#remove_follower_for_task) | **POST** /tasks/{task_gid}/removeFollowers | Remove followers from a task
*TasksApi* | [**remove_project_for_task**](docs/TasksApi.md#remove_project_for_task) | **POST** /tasks/{task_gid}/removeProject | Remove a project from a task
*TasksApi* | [**remove_tag_for_task**](docs/TasksApi.md#remove_tag_for_task) | **POST** /tasks/{task_gid}/removeTag | Remove a tag from a task
*TasksApi* | [**search_tasks_for_workspace**](docs/TasksApi.md#search_tasks_for_workspace) | **GET** /workspaces/{workspace_gid}/tasks/search | Search tasks in a workspace
*TasksApi* | [**set_parent_for_task**](docs/TasksApi.md#set_parent_for_task) | **POST** /tasks/{task_gid}/setParent | Set the parent of a task
*TasksApi* | [**update_task**](docs/TasksApi.md#update_task) | **PUT** /tasks/{task_gid} | Update a task
*TeamMembershipsApi* | [**get_team_membership**](docs/TeamMembershipsApi.md#get_team_membership) | **GET** /team_memberships/{team_membership_gid} | Get a team membership
*TeamMembershipsApi* | [**get_team_memberships**](docs/TeamMembershipsApi.md#get_team_memberships) | **GET** /team_memberships | Get team memberships
*TeamMembershipsApi* | [**get_team_memberships_for_team**](docs/TeamMembershipsApi.md#get_team_memberships_for_team) | **GET** /teams/{team_gid}/team_memberships | Get memberships from a team
*TeamMembershipsApi* | [**get_team_memberships_for_user**](docs/TeamMembershipsApi.md#get_team_memberships_for_user) | **GET** /users/{user_gid}/team_memberships | Get memberships from a user
*TeamsApi* | [**add_user_for_team**](docs/TeamsApi.md#add_user_for_team) | **POST** /teams/{team_gid}/addUser | Add a user to a team
*TeamsApi* | [**create_team**](docs/TeamsApi.md#create_team) | **POST** /teams | Create a team
*TeamsApi* | [**get_team**](docs/TeamsApi.md#get_team) | **GET** /teams/{team_gid} | Get a team
*TeamsApi* | [**get_teams_for_user**](docs/TeamsApi.md#get_teams_for_user) | **GET** /users/{user_gid}/teams | Get teams for a user
*TeamsApi* | [**get_teams_for_workspace**](docs/TeamsApi.md#get_teams_for_workspace) | **GET** /workspaces/{workspace_gid}/teams | Get teams in a workspace
*TeamsApi* | [**remove_user_for_team**](docs/TeamsApi.md#remove_user_for_team) | **POST** /teams/{team_gid}/removeUser | Remove a user from a team
*TeamsApi* | [**update_team**](docs/TeamsApi.md#update_team) | **PUT** /teams/{team_gid} | Update a team
*TimePeriodsApi* | [**get_time_period**](docs/TimePeriodsApi.md#get_time_period) | **GET** /time_periods/{time_period_gid} | Get a time period
*TimePeriodsApi* | [**get_time_periods**](docs/TimePeriodsApi.md#get_time_periods) | **GET** /time_periods | Get time periods
*TimeTrackingEntriesApi* | [**create_time_tracking_entry**](docs/TimeTrackingEntriesApi.md#create_time_tracking_entry) | **POST** /tasks/{task_gid}/time_tracking_entries | Create a time tracking entry
*TimeTrackingEntriesApi* | [**delete_time_tracking_entry**](docs/TimeTrackingEntriesApi.md#delete_time_tracking_entry) | **DELETE** /time_tracking_entries/{time_tracking_entry_gid} | Delete a time tracking entry
*TimeTrackingEntriesApi* | [**get_time_tracking_entries_for_task**](docs/TimeTrackingEntriesApi.md#get_time_tracking_entries_for_task) | **GET** /tasks/{task_gid}/time_tracking_entries | Get time tracking entries for a task
*TimeTrackingEntriesApi* | [**get_time_tracking_entry**](docs/TimeTrackingEntriesApi.md#get_time_tracking_entry) | **GET** /time_tracking_entries/{time_tracking_entry_gid} | Get a time tracking entry
*TimeTrackingEntriesApi* | [**update_time_tracking_entry**](docs/TimeTrackingEntriesApi.md#update_time_tracking_entry) | **PUT** /time_tracking_entries/{time_tracking_entry_gid} | Update a time tracking entry
*TypeaheadApi* | [**typeahead_for_workspace**](docs/TypeaheadApi.md#typeahead_for_workspace) | **GET** /workspaces/{workspace_gid}/typeahead | Get objects via typeahead
*UserTaskListsApi* | [**get_user_task_list**](docs/UserTaskListsApi.md#get_user_task_list) | **GET** /user_task_lists/{user_task_list_gid} | Get a user task list
*UserTaskListsApi* | [**get_user_task_list_for_user**](docs/UserTaskListsApi.md#get_user_task_list_for_user) | **GET** /users/{user_gid}/user_task_list | Get a user&#x27;s task list
*UsersApi* | [**get_favorites_for_user**](docs/UsersApi.md#get_favorites_for_user) | **GET** /users/{user_gid}/favorites | Get a user&#x27;s favorites
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /users/{user_gid} | Get a user
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /users | Get multiple users
*UsersApi* | [**get_users_for_team**](docs/UsersApi.md#get_users_for_team) | **GET** /teams/{team_gid}/users | Get users in a team
*UsersApi* | [**get_users_for_workspace**](docs/UsersApi.md#get_users_for_workspace) | **GET** /workspaces/{workspace_gid}/users | Get users in a workspace or organization
*WebhooksApi* | [**create_webhook**](docs/WebhooksApi.md#create_webhook) | **POST** /webhooks | Establish a webhook
*WebhooksApi* | [**delete_webhook**](docs/WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{webhook_gid} | Delete a webhook
*WebhooksApi* | [**get_webhook**](docs/WebhooksApi.md#get_webhook) | **GET** /webhooks/{webhook_gid} | Get a webhook
*WebhooksApi* | [**get_webhooks**](docs/WebhooksApi.md#get_webhooks) | **GET** /webhooks | Get multiple webhooks
*WebhooksApi* | [**update_webhook**](docs/WebhooksApi.md#update_webhook) | **PUT** /webhooks/{webhook_gid} | Update a webhook
*WorkspaceMembershipsApi* | [**get_workspace_membership**](docs/WorkspaceMembershipsApi.md#get_workspace_membership) | **GET** /workspace_memberships/{workspace_membership_gid} | Get a workspace membership
*WorkspaceMembershipsApi* | [**get_workspace_memberships_for_user**](docs/WorkspaceMembershipsApi.md#get_workspace_memberships_for_user) | **GET** /users/{user_gid}/workspace_memberships | Get workspace memberships for a user
*WorkspaceMembershipsApi* | [**get_workspace_memberships_for_workspace**](docs/WorkspaceMembershipsApi.md#get_workspace_memberships_for_workspace) | **GET** /workspaces/{workspace_gid}/workspace_memberships | Get the workspace memberships for a workspace
*WorkspacesApi* | [**add_user_for_workspace**](docs/WorkspacesApi.md#add_user_for_workspace) | **POST** /workspaces/{workspace_gid}/addUser | Add a user to a workspace or organization
*WorkspacesApi* | [**get_workspace**](docs/WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspace_gid} | Get a workspace
*WorkspacesApi* | [**get_workspaces**](docs/WorkspacesApi.md#get_workspaces) | **GET** /workspaces | Get multiple workspaces
*WorkspacesApi* | [**remove_user_for_workspace**](docs/WorkspacesApi.md#remove_user_for_workspace) | **POST** /workspaces/{workspace_gid}/removeUser | Remove a user from a workspace or organization
*WorkspacesApi* | [**update_workspace**](docs/WorkspacesApi.md#update_workspace) | **PUT** /workspaces/{workspace_gid} | Update a workspace

## Documentation For Models

 - [AddCustomFieldSettingRequest](docs/AddCustomFieldSettingRequest.md)
 - [AddFollowersRequest](docs/AddFollowersRequest.md)
 - [AddMembersRequest](docs/AddMembersRequest.md)
 - [AllOfProjectResponseOwner](docs/AllOfProjectResponseOwner.md)
 - [AllOfProjectTemplateBaseOwner](docs/AllOfProjectTemplateBaseOwner.md)
 - [AllOfProjectTemplateResponseOwner](docs/AllOfProjectTemplateResponseOwner.md)
 - [AllOfStoryResponseNewDateValue](docs/AllOfStoryResponseNewDateValue.md)
 - [AllOfStoryResponseOldDateValue](docs/AllOfStoryResponseOldDateValue.md)
 - [AllOfUserTaskListBaseOwner](docs/AllOfUserTaskListBaseOwner.md)
 - [AllOfUserTaskListBaseWorkspace](docs/AllOfUserTaskListBaseWorkspace.md)
 - [AllOfUserTaskListCompactOwner](docs/AllOfUserTaskListCompactOwner.md)
 - [AllOfUserTaskListCompactWorkspace](docs/AllOfUserTaskListCompactWorkspace.md)
 - [AllOfUserTaskListRequestOwner](docs/AllOfUserTaskListRequestOwner.md)
 - [AllOfUserTaskListRequestWorkspace](docs/AllOfUserTaskListRequestWorkspace.md)
 - [AllOfUserTaskListResponseOwner](docs/AllOfUserTaskListResponseOwner.md)
 - [AllOfUserTaskListResponseWorkspace](docs/AllOfUserTaskListResponseWorkspace.md)
 - [AllOfWorkspaceMembershipResponseUserTaskListOwner](docs/AllOfWorkspaceMembershipResponseUserTaskListOwner.md)
 - [AllOfWorkspaceMembershipResponseUserTaskListWorkspace](docs/AllOfWorkspaceMembershipResponseUserTaskListWorkspace.md)
 - [AsanaNamedResource](docs/AsanaNamedResource.md)
 - [AsanaNamedResourceArray](docs/AsanaNamedResourceArray.md)
 - [AsanaResource](docs/AsanaResource.md)
 - [AttachmentBase](docs/AttachmentBase.md)
 - [AttachmentCompact](docs/AttachmentCompact.md)
 - [AttachmentRequest](docs/AttachmentRequest.md)
 - [AttachmentResponse](docs/AttachmentResponse.md)
 - [AttachmentResponseArray](docs/AttachmentResponseArray.md)
 - [AttachmentResponseData](docs/AttachmentResponseData.md)
 - [AttachmentResponseParent](docs/AttachmentResponseParent.md)
 - [AttachmentResponseParentCreatedBy](docs/AttachmentResponseParentCreatedBy.md)
 - [AuditLogEvent](docs/AuditLogEvent.md)
 - [AuditLogEventActor](docs/AuditLogEventActor.md)
 - [AuditLogEventArray](docs/AuditLogEventArray.md)
 - [AuditLogEventContext](docs/AuditLogEventContext.md)
 - [AuditLogEventDetails](docs/AuditLogEventDetails.md)
 - [AuditLogEventResource](docs/AuditLogEventResource.md)
 - [BatchBody](docs/BatchBody.md)
 - [BatchRequest](docs/BatchRequest.md)
 - [BatchRequestAction](docs/BatchRequestAction.md)
 - [BatchRequestActions](docs/BatchRequestActions.md)
 - [BatchRequestOptions](docs/BatchRequestOptions.md)
 - [BatchResponse](docs/BatchResponse.md)
 - [BatchResponseArray](docs/BatchResponseArray.md)
 - [CreateMembershipRequest](docs/CreateMembershipRequest.md)
 - [CreateTimeTrackingEntryRequest](docs/CreateTimeTrackingEntryRequest.md)
 - [CustomFieldBase](docs/CustomFieldBase.md)
 - [CustomFieldBaseDateValue](docs/CustomFieldBaseDateValue.md)
 - [CustomFieldBaseEnumOptions](docs/CustomFieldBaseEnumOptions.md)
 - [CustomFieldBaseEnumValue](docs/CustomFieldBaseEnumValue.md)
 - [CustomFieldCompact](docs/CustomFieldCompact.md)
 - [CustomFieldGidEnumOptionsBody](docs/CustomFieldGidEnumOptionsBody.md)
 - [CustomFieldRequest](docs/CustomFieldRequest.md)
 - [CustomFieldResponse](docs/CustomFieldResponse.md)
 - [CustomFieldResponseArray](docs/CustomFieldResponseArray.md)
 - [CustomFieldResponseCreatedBy](docs/CustomFieldResponseCreatedBy.md)
 - [CustomFieldResponseData](docs/CustomFieldResponseData.md)
 - [CustomFieldResponsePeopleValue](docs/CustomFieldResponsePeopleValue.md)
 - [CustomFieldSettingBase](docs/CustomFieldSettingBase.md)
 - [CustomFieldSettingCompact](docs/CustomFieldSettingCompact.md)
 - [CustomFieldSettingResponse](docs/CustomFieldSettingResponse.md)
 - [CustomFieldSettingResponseArray](docs/CustomFieldSettingResponseArray.md)
 - [CustomFieldSettingResponseCustomField](docs/CustomFieldSettingResponseCustomField.md)
 - [CustomFieldSettingResponseData](docs/CustomFieldSettingResponseData.md)
 - [CustomFieldSettingResponseParent](docs/CustomFieldSettingResponseParent.md)
 - [CustomFieldSettingResponseProject](docs/CustomFieldSettingResponseProject.md)
 - [CustomFieldsBody](docs/CustomFieldsBody.md)
 - [CustomFieldsCustomFieldGidBody](docs/CustomFieldsCustomFieldGidBody.md)
 - [DateVariableCompact](docs/DateVariableCompact.md)
 - [DateVariableRequest](docs/DateVariableRequest.md)
 - [EmptyResponse](docs/EmptyResponse.md)
 - [EmptyResponseData](docs/EmptyResponseData.md)
 - [EnumOption](docs/EnumOption.md)
 - [EnumOptionBase](docs/EnumOptionBase.md)
 - [EnumOptionData](docs/EnumOptionData.md)
 - [EnumOptionInsertRequest](docs/EnumOptionInsertRequest.md)
 - [EnumOptionRequest](docs/EnumOptionRequest.md)
 - [EnumOptionsEnumOptionGidBody](docs/EnumOptionsEnumOptionGidBody.md)
 - [EnumOptionsInsertBody](docs/EnumOptionsInsertBody.md)
 - [Error](docs/Error.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ErrorResponseErrors](docs/ErrorResponseErrors.md)
 - [EventResponse](docs/EventResponse.md)
 - [EventResponseArray](docs/EventResponseArray.md)
 - [EventResponseChange](docs/EventResponseChange.md)
 - [EventResponseParent](docs/EventResponseParent.md)
 - [EventResponseResource](docs/EventResponseResource.md)
 - [EventResponseUser](docs/EventResponseUser.md)
 - [GoalAddSubgoalRequest](docs/GoalAddSubgoalRequest.md)
 - [GoalAddSupportingRelationshipRequest](docs/GoalAddSupportingRelationshipRequest.md)
 - [GoalAddSupportingWorkRequest](docs/GoalAddSupportingWorkRequest.md)
 - [GoalBase](docs/GoalBase.md)
 - [GoalCompact](docs/GoalCompact.md)
 - [GoalGidAddFollowersBody](docs/GoalGidAddFollowersBody.md)
 - [GoalGidAddSupportingRelationshipBody](docs/GoalGidAddSupportingRelationshipBody.md)
 - [GoalGidRemoveFollowersBody](docs/GoalGidRemoveFollowersBody.md)
 - [GoalGidRemoveSupportingRelationshipBody](docs/GoalGidRemoveSupportingRelationshipBody.md)
 - [GoalGidSetMetricBody](docs/GoalGidSetMetricBody.md)
 - [GoalGidSetMetricCurrentValueBody](docs/GoalGidSetMetricCurrentValueBody.md)
 - [GoalMembershipBase](docs/GoalMembershipBase.md)
 - [GoalMembershipCompact](docs/GoalMembershipCompact.md)
 - [GoalMembershipResponse](docs/GoalMembershipResponse.md)
 - [GoalMembershipResponseUser](docs/GoalMembershipResponseUser.md)
 - [GoalMembershipResponseWorkspace](docs/GoalMembershipResponseWorkspace.md)
 - [GoalMetricBase](docs/GoalMetricBase.md)
 - [GoalMetricCurrentValueRequest](docs/GoalMetricCurrentValueRequest.md)
 - [GoalMetricRequest](docs/GoalMetricRequest.md)
 - [GoalRelationshipBase](docs/GoalRelationshipBase.md)
 - [GoalRelationshipBaseSupportedGoal](docs/GoalRelationshipBaseSupportedGoal.md)
 - [GoalRelationshipBaseSupportingResource](docs/GoalRelationshipBaseSupportingResource.md)
 - [GoalRelationshipCompact](docs/GoalRelationshipCompact.md)
 - [GoalRelationshipRequest](docs/GoalRelationshipRequest.md)
 - [GoalRelationshipResponse](docs/GoalRelationshipResponse.md)
 - [GoalRelationshipResponseArray](docs/GoalRelationshipResponseArray.md)
 - [GoalRelationshipResponseData](docs/GoalRelationshipResponseData.md)
 - [GoalRelationshipsGoalRelationshipGidBody](docs/GoalRelationshipsGoalRelationshipGidBody.md)
 - [GoalRemoveSubgoalRequest](docs/GoalRemoveSubgoalRequest.md)
 - [GoalRemoveSupportingRelationshipRequest](docs/GoalRemoveSupportingRelationshipRequest.md)
 - [GoalRequest](docs/GoalRequest.md)
 - [GoalRequestBase](docs/GoalRequestBase.md)
 - [GoalResponse](docs/GoalResponse.md)
 - [GoalResponseArray](docs/GoalResponseArray.md)
 - [GoalResponseCurrentStatusUpdate](docs/GoalResponseCurrentStatusUpdate.md)
 - [GoalResponseData](docs/GoalResponseData.md)
 - [GoalResponseLikes](docs/GoalResponseLikes.md)
 - [GoalResponseMetric](docs/GoalResponseMetric.md)
 - [GoalResponseTeam](docs/GoalResponseTeam.md)
 - [GoalResponseTimePeriod](docs/GoalResponseTimePeriod.md)
 - [GoalResponseWorkspace](docs/GoalResponseWorkspace.md)
 - [GoalUpdateRequest](docs/GoalUpdateRequest.md)
 - [GoalsBody](docs/GoalsBody.md)
 - [GoalsGoalGidBody](docs/GoalsGoalGidBody.md)
 - [InlineResponse412](docs/InlineResponse412.md)
 - [InlineResponse412Errors](docs/InlineResponse412Errors.md)
 - [JobBase](docs/JobBase.md)
 - [JobBaseNewProject](docs/JobBaseNewProject.md)
 - [JobBaseNewProjectTemplate](docs/JobBaseNewProjectTemplate.md)
 - [JobBaseNewTask](docs/JobBaseNewTask.md)
 - [JobCompact](docs/JobCompact.md)
 - [JobResponse](docs/JobResponse.md)
 - [JobResponseData](docs/JobResponseData.md)
 - [Like](docs/Like.md)
 - [MemberCompact](docs/MemberCompact.md)
 - [MembershipCompact](docs/MembershipCompact.md)
 - [MembershipCompactGoal](docs/MembershipCompactGoal.md)
 - [MembershipCompactMember](docs/MembershipCompactMember.md)
 - [MembershipCompactParent](docs/MembershipCompactParent.md)
 - [MembershipRequest](docs/MembershipRequest.md)
 - [MembershipResponse](docs/MembershipResponse.md)
 - [MembershipResponseArray](docs/MembershipResponseArray.md)
 - [MembershipResponseData](docs/MembershipResponseData.md)
 - [MembershipsBody](docs/MembershipsBody.md)
 - [ModifyDependenciesRequest](docs/ModifyDependenciesRequest.md)
 - [ModifyDependentsRequest](docs/ModifyDependentsRequest.md)
 - [NextPage](docs/NextPage.md)
 - [OrganizationExportBase](docs/OrganizationExportBase.md)
 - [OrganizationExportCompact](docs/OrganizationExportCompact.md)
 - [OrganizationExportRequest](docs/OrganizationExportRequest.md)
 - [OrganizationExportResponse](docs/OrganizationExportResponse.md)
 - [OrganizationExportResponseData](docs/OrganizationExportResponseData.md)
 - [OrganizationExportsBody](docs/OrganizationExportsBody.md)
 - [PortfolioAddItemRequest](docs/PortfolioAddItemRequest.md)
 - [PortfolioBase](docs/PortfolioBase.md)
 - [PortfolioCompact](docs/PortfolioCompact.md)
 - [PortfolioGidAddCustomFieldSettingBody](docs/PortfolioGidAddCustomFieldSettingBody.md)
 - [PortfolioGidAddItemBody](docs/PortfolioGidAddItemBody.md)
 - [PortfolioGidAddMembersBody](docs/PortfolioGidAddMembersBody.md)
 - [PortfolioGidRemoveCustomFieldSettingBody](docs/PortfolioGidRemoveCustomFieldSettingBody.md)
 - [PortfolioGidRemoveItemBody](docs/PortfolioGidRemoveItemBody.md)
 - [PortfolioGidRemoveMembersBody](docs/PortfolioGidRemoveMembersBody.md)
 - [PortfolioMembershipBase](docs/PortfolioMembershipBase.md)
 - [PortfolioMembershipBasePortfolio](docs/PortfolioMembershipBasePortfolio.md)
 - [PortfolioMembershipCompact](docs/PortfolioMembershipCompact.md)
 - [PortfolioMembershipResponse](docs/PortfolioMembershipResponse.md)
 - [PortfolioMembershipResponseArray](docs/PortfolioMembershipResponseArray.md)
 - [PortfolioMembershipResponseData](docs/PortfolioMembershipResponseData.md)
 - [PortfolioRemoveItemRequest](docs/PortfolioRemoveItemRequest.md)
 - [PortfolioRequest](docs/PortfolioRequest.md)
 - [PortfolioResponse](docs/PortfolioResponse.md)
 - [PortfolioResponseArray](docs/PortfolioResponseArray.md)
 - [PortfolioResponseCurrentStatusUpdate](docs/PortfolioResponseCurrentStatusUpdate.md)
 - [PortfolioResponseCustomFieldSettings](docs/PortfolioResponseCustomFieldSettings.md)
 - [PortfolioResponseCustomFields](docs/PortfolioResponseCustomFields.md)
 - [PortfolioResponseData](docs/PortfolioResponseData.md)
 - [PortfolioResponseWorkspace](docs/PortfolioResponseWorkspace.md)
 - [PortfoliosBody](docs/PortfoliosBody.md)
 - [PortfoliosPortfolioGidBody](docs/PortfoliosPortfolioGidBody.md)
 - [Preview](docs/Preview.md)
 - [ProjectBase](docs/ProjectBase.md)
 - [ProjectBaseCurrentStatus](docs/ProjectBaseCurrentStatus.md)
 - [ProjectBaseCurrentStatusUpdate](docs/ProjectBaseCurrentStatusUpdate.md)
 - [ProjectBriefBase](docs/ProjectBriefBase.md)
 - [ProjectBriefCompact](docs/ProjectBriefCompact.md)
 - [ProjectBriefRequest](docs/ProjectBriefRequest.md)
 - [ProjectBriefResponse](docs/ProjectBriefResponse.md)
 - [ProjectBriefResponseData](docs/ProjectBriefResponseData.md)
 - [ProjectBriefResponseProject](docs/ProjectBriefResponseProject.md)
 - [ProjectBriefsProjectBriefGidBody](docs/ProjectBriefsProjectBriefGidBody.md)
 - [ProjectCompact](docs/ProjectCompact.md)
 - [ProjectDuplicateRequest](docs/ProjectDuplicateRequest.md)
 - [ProjectDuplicateRequestScheduleDates](docs/ProjectDuplicateRequestScheduleDates.md)
 - [ProjectGidAddCustomFieldSettingBody](docs/ProjectGidAddCustomFieldSettingBody.md)
 - [ProjectGidAddFollowersBody](docs/ProjectGidAddFollowersBody.md)
 - [ProjectGidAddMembersBody](docs/ProjectGidAddMembersBody.md)
 - [ProjectGidDuplicateBody](docs/ProjectGidDuplicateBody.md)
 - [ProjectGidProjectBriefsBody](docs/ProjectGidProjectBriefsBody.md)
 - [ProjectGidProjectStatusesBody](docs/ProjectGidProjectStatusesBody.md)
 - [ProjectGidRemoveCustomFieldSettingBody](docs/ProjectGidRemoveCustomFieldSettingBody.md)
 - [ProjectGidRemoveFollowersBody](docs/ProjectGidRemoveFollowersBody.md)
 - [ProjectGidRemoveMembersBody](docs/ProjectGidRemoveMembersBody.md)
 - [ProjectGidSaveAsTemplateBody](docs/ProjectGidSaveAsTemplateBody.md)
 - [ProjectGidSectionsBody](docs/ProjectGidSectionsBody.md)
 - [ProjectMembershipBase](docs/ProjectMembershipBase.md)
 - [ProjectMembershipCompact](docs/ProjectMembershipCompact.md)
 - [ProjectMembershipCompactArray](docs/ProjectMembershipCompactArray.md)
 - [ProjectMembershipCompactResponse](docs/ProjectMembershipCompactResponse.md)
 - [ProjectMembershipCompactResponseData](docs/ProjectMembershipCompactResponseData.md)
 - [ProjectMembershipNormalResponse](docs/ProjectMembershipNormalResponse.md)
 - [ProjectMembershipNormalResponseData](docs/ProjectMembershipNormalResponseData.md)
 - [ProjectRequest](docs/ProjectRequest.md)
 - [ProjectResponse](docs/ProjectResponse.md)
 - [ProjectResponseArray](docs/ProjectResponseArray.md)
 - [ProjectResponseCompletedBy](docs/ProjectResponseCompletedBy.md)
 - [ProjectResponseCreatedFromTemplate](docs/ProjectResponseCreatedFromTemplate.md)
 - [ProjectResponseData](docs/ProjectResponseData.md)
 - [ProjectResponseProjectBrief](docs/ProjectResponseProjectBrief.md)
 - [ProjectResponseTeam](docs/ProjectResponseTeam.md)
 - [ProjectResponseWorkspace](docs/ProjectResponseWorkspace.md)
 - [ProjectSaveAsTemplateRequest](docs/ProjectSaveAsTemplateRequest.md)
 - [ProjectSectionInsertRequest](docs/ProjectSectionInsertRequest.md)
 - [ProjectStatusBase](docs/ProjectStatusBase.md)
 - [ProjectStatusCompact](docs/ProjectStatusCompact.md)
 - [ProjectStatusRequest](docs/ProjectStatusRequest.md)
 - [ProjectStatusResponse](docs/ProjectStatusResponse.md)
 - [ProjectStatusResponseArray](docs/ProjectStatusResponseArray.md)
 - [ProjectStatusResponseData](docs/ProjectStatusResponseData.md)
 - [ProjectTemplateBase](docs/ProjectTemplateBase.md)
 - [ProjectTemplateBaseRequestedDates](docs/ProjectTemplateBaseRequestedDates.md)
 - [ProjectTemplateBaseRequestedRoles](docs/ProjectTemplateBaseRequestedRoles.md)
 - [ProjectTemplateBaseTeam](docs/ProjectTemplateBaseTeam.md)
 - [ProjectTemplateCompact](docs/ProjectTemplateCompact.md)
 - [ProjectTemplateGidInstantiateProjectBody](docs/ProjectTemplateGidInstantiateProjectBody.md)
 - [ProjectTemplateInstantiateProjectRequest](docs/ProjectTemplateInstantiateProjectRequest.md)
 - [ProjectTemplateInstantiateProjectRequestRequestedDates](docs/ProjectTemplateInstantiateProjectRequestRequestedDates.md)
 - [ProjectTemplateInstantiateProjectRequestRequestedRoles](docs/ProjectTemplateInstantiateProjectRequestRequestedRoles.md)
 - [ProjectTemplateResponse](docs/ProjectTemplateResponse.md)
 - [ProjectTemplateResponseArray](docs/ProjectTemplateResponseArray.md)
 - [ProjectTemplateResponseData](docs/ProjectTemplateResponseData.md)
 - [ProjectUpdateRequest](docs/ProjectUpdateRequest.md)
 - [ProjectsBody](docs/ProjectsBody.md)
 - [ProjectsProjectGidBody](docs/ProjectsProjectGidBody.md)
 - [RemoveCustomFieldSettingRequest](docs/RemoveCustomFieldSettingRequest.md)
 - [RemoveFollowersRequest](docs/RemoveFollowersRequest.md)
 - [RemoveMembersRequest](docs/RemoveMembersRequest.md)
 - [RequestedRoleRequest](docs/RequestedRoleRequest.md)
 - [RuleTriggerGidRunBody](docs/RuleTriggerGidRunBody.md)
 - [RuleTriggerRequest](docs/RuleTriggerRequest.md)
 - [RuleTriggerResponse](docs/RuleTriggerResponse.md)
 - [RuleTriggerResponseData](docs/RuleTriggerResponseData.md)
 - [SectionBase](docs/SectionBase.md)
 - [SectionCompact](docs/SectionCompact.md)
 - [SectionGidAddTaskBody](docs/SectionGidAddTaskBody.md)
 - [SectionRequest](docs/SectionRequest.md)
 - [SectionResponse](docs/SectionResponse.md)
 - [SectionResponseArray](docs/SectionResponseArray.md)
 - [SectionResponseData](docs/SectionResponseData.md)
 - [SectionTaskInsertRequest](docs/SectionTaskInsertRequest.md)
 - [SectionsInsertBody](docs/SectionsInsertBody.md)
 - [SectionsSectionGidBody](docs/SectionsSectionGidBody.md)
 - [StatusUpdateBase](docs/StatusUpdateBase.md)
 - [StatusUpdateCompact](docs/StatusUpdateCompact.md)
 - [StatusUpdateRequest](docs/StatusUpdateRequest.md)
 - [StatusUpdateResponse](docs/StatusUpdateResponse.md)
 - [StatusUpdateResponseArray](docs/StatusUpdateResponseArray.md)
 - [StatusUpdateResponseData](docs/StatusUpdateResponseData.md)
 - [StatusUpdateResponseParent](docs/StatusUpdateResponseParent.md)
 - [StatusUpdatesBody](docs/StatusUpdatesBody.md)
 - [StoriesStoryGidBody](docs/StoriesStoryGidBody.md)
 - [StoryBase](docs/StoryBase.md)
 - [StoryCompact](docs/StoryCompact.md)
 - [StoryRequest](docs/StoryRequest.md)
 - [StoryResponse](docs/StoryResponse.md)
 - [StoryResponseArray](docs/StoryResponseArray.md)
 - [StoryResponseAssignee](docs/StoryResponseAssignee.md)
 - [StoryResponseCustomField](docs/StoryResponseCustomField.md)
 - [StoryResponseData](docs/StoryResponseData.md)
 - [StoryResponseDates](docs/StoryResponseDates.md)
 - [StoryResponseOldDates](docs/StoryResponseOldDates.md)
 - [StoryResponseOldEnumValue](docs/StoryResponseOldEnumValue.md)
 - [StoryResponseOldSection](docs/StoryResponseOldSection.md)
 - [StoryResponsePreviews](docs/StoryResponsePreviews.md)
 - [StoryResponseProject](docs/StoryResponseProject.md)
 - [StoryResponseStory](docs/StoryResponseStory.md)
 - [StoryResponseTag](docs/StoryResponseTag.md)
 - [StoryResponseTarget](docs/StoryResponseTarget.md)
 - [StoryResponseTask](docs/StoryResponseTask.md)
 - [TagBase](docs/TagBase.md)
 - [TagCompact](docs/TagCompact.md)
 - [TagRequest](docs/TagRequest.md)
 - [TagResponse](docs/TagResponse.md)
 - [TagResponseArray](docs/TagResponseArray.md)
 - [TagResponseData](docs/TagResponseData.md)
 - [TagsBody](docs/TagsBody.md)
 - [TaskAddFollowersRequest](docs/TaskAddFollowersRequest.md)
 - [TaskAddProjectRequest](docs/TaskAddProjectRequest.md)
 - [TaskAddTagRequest](docs/TaskAddTagRequest.md)
 - [TaskBase](docs/TaskBase.md)
 - [TaskBaseCompletedBy](docs/TaskBaseCompletedBy.md)
 - [TaskBaseDependencies](docs/TaskBaseDependencies.md)
 - [TaskBaseExternal](docs/TaskBaseExternal.md)
 - [TaskBaseMemberships](docs/TaskBaseMemberships.md)
 - [TaskBaseSection](docs/TaskBaseSection.md)
 - [TaskCompact](docs/TaskCompact.md)
 - [TaskCountResponse](docs/TaskCountResponse.md)
 - [TaskCountResponseData](docs/TaskCountResponseData.md)
 - [TaskDuplicateRequest](docs/TaskDuplicateRequest.md)
 - [TaskGidAddDependenciesBody](docs/TaskGidAddDependenciesBody.md)
 - [TaskGidAddDependentsBody](docs/TaskGidAddDependentsBody.md)
 - [TaskGidAddFollowersBody](docs/TaskGidAddFollowersBody.md)
 - [TaskGidAddProjectBody](docs/TaskGidAddProjectBody.md)
 - [TaskGidAddTagBody](docs/TaskGidAddTagBody.md)
 - [TaskGidDuplicateBody](docs/TaskGidDuplicateBody.md)
 - [TaskGidRemoveDependenciesBody](docs/TaskGidRemoveDependenciesBody.md)
 - [TaskGidRemoveDependentsBody](docs/TaskGidRemoveDependentsBody.md)
 - [TaskGidRemoveFollowersBody](docs/TaskGidRemoveFollowersBody.md)
 - [TaskGidRemoveProjectBody](docs/TaskGidRemoveProjectBody.md)
 - [TaskGidRemoveTagBody](docs/TaskGidRemoveTagBody.md)
 - [TaskGidSetParentBody](docs/TaskGidSetParentBody.md)
 - [TaskGidStoriesBody](docs/TaskGidStoriesBody.md)
 - [TaskGidSubtasksBody](docs/TaskGidSubtasksBody.md)
 - [TaskGidTimeTrackingEntriesBody](docs/TaskGidTimeTrackingEntriesBody.md)
 - [TaskRemoveFollowersRequest](docs/TaskRemoveFollowersRequest.md)
 - [TaskRemoveProjectRequest](docs/TaskRemoveProjectRequest.md)
 - [TaskRemoveTagRequest](docs/TaskRemoveTagRequest.md)
 - [TaskRequest](docs/TaskRequest.md)
 - [TaskResponse](docs/TaskResponse.md)
 - [TaskResponseArray](docs/TaskResponseArray.md)
 - [TaskResponseAssigneeSection](docs/TaskResponseAssigneeSection.md)
 - [TaskResponseCustomFields](docs/TaskResponseCustomFields.md)
 - [TaskResponseData](docs/TaskResponseData.md)
 - [TaskResponseParent](docs/TaskResponseParent.md)
 - [TaskResponseTags](docs/TaskResponseTags.md)
 - [TaskResponseWorkspace](docs/TaskResponseWorkspace.md)
 - [TaskSetParentRequest](docs/TaskSetParentRequest.md)
 - [TasksBody](docs/TasksBody.md)
 - [TasksTaskGidBody](docs/TasksTaskGidBody.md)
 - [TeamAddUserRequest](docs/TeamAddUserRequest.md)
 - [TeamBase](docs/TeamBase.md)
 - [TeamCompact](docs/TeamCompact.md)
 - [TeamGidAddUserBody](docs/TeamGidAddUserBody.md)
 - [TeamGidProjectsBody](docs/TeamGidProjectsBody.md)
 - [TeamGidRemoveUserBody](docs/TeamGidRemoveUserBody.md)
 - [TeamMembershipBase](docs/TeamMembershipBase.md)
 - [TeamMembershipCompact](docs/TeamMembershipCompact.md)
 - [TeamMembershipResponse](docs/TeamMembershipResponse.md)
 - [TeamMembershipResponseArray](docs/TeamMembershipResponseArray.md)
 - [TeamMembershipResponseData](docs/TeamMembershipResponseData.md)
 - [TeamRemoveUserRequest](docs/TeamRemoveUserRequest.md)
 - [TeamRequest](docs/TeamRequest.md)
 - [TeamResponse](docs/TeamResponse.md)
 - [TeamResponseArray](docs/TeamResponseArray.md)
 - [TeamResponseData](docs/TeamResponseData.md)
 - [TeamResponseOrganization](docs/TeamResponseOrganization.md)
 - [TeamsBody](docs/TeamsBody.md)
 - [TeamsTeamGidBody](docs/TeamsTeamGidBody.md)
 - [TemplateRole](docs/TemplateRole.md)
 - [TimePeriodBase](docs/TimePeriodBase.md)
 - [TimePeriodCompact](docs/TimePeriodCompact.md)
 - [TimePeriodResponse](docs/TimePeriodResponse.md)
 - [TimePeriodResponseArray](docs/TimePeriodResponseArray.md)
 - [TimePeriodResponseData](docs/TimePeriodResponseData.md)
 - [TimeTrackingEntriesTimeTrackingEntryGidBody](docs/TimeTrackingEntriesTimeTrackingEntryGidBody.md)
 - [TimeTrackingEntryBase](docs/TimeTrackingEntryBase.md)
 - [TimeTrackingEntryBaseData](docs/TimeTrackingEntryBaseData.md)
 - [TimeTrackingEntryCompact](docs/TimeTrackingEntryCompact.md)
 - [TimeTrackingEntryCompactArray](docs/TimeTrackingEntryCompactArray.md)
 - [UpdateTimeTrackingEntryRequest](docs/UpdateTimeTrackingEntryRequest.md)
 - [UserBase](docs/UserBase.md)
 - [UserBaseResponse](docs/UserBaseResponse.md)
 - [UserBaseResponseData](docs/UserBaseResponseData.md)
 - [UserBaseResponsePhoto](docs/UserBaseResponsePhoto.md)
 - [UserCompact](docs/UserCompact.md)
 - [UserRequest](docs/UserRequest.md)
 - [UserResponse](docs/UserResponse.md)
 - [UserResponseArray](docs/UserResponseArray.md)
 - [UserResponseData](docs/UserResponseData.md)
 - [UserTaskListBase](docs/UserTaskListBase.md)
 - [UserTaskListCompact](docs/UserTaskListCompact.md)
 - [UserTaskListRequest](docs/UserTaskListRequest.md)
 - [UserTaskListResponse](docs/UserTaskListResponse.md)
 - [UserTaskListResponseData](docs/UserTaskListResponseData.md)
 - [WebhookCompact](docs/WebhookCompact.md)
 - [WebhookCompactResource](docs/WebhookCompactResource.md)
 - [WebhookFilter](docs/WebhookFilter.md)
 - [WebhookRequest](docs/WebhookRequest.md)
 - [WebhookRequestFilters](docs/WebhookRequestFilters.md)
 - [WebhookResponse](docs/WebhookResponse.md)
 - [WebhookResponseArray](docs/WebhookResponseArray.md)
 - [WebhookResponseData](docs/WebhookResponseData.md)
 - [WebhookUpdateRequest](docs/WebhookUpdateRequest.md)
 - [WebhooksBody](docs/WebhooksBody.md)
 - [WebhooksWebhookGidBody](docs/WebhooksWebhookGidBody.md)
 - [WorkspaceAddUserRequest](docs/WorkspaceAddUserRequest.md)
 - [WorkspaceBase](docs/WorkspaceBase.md)
 - [WorkspaceCompact](docs/WorkspaceCompact.md)
 - [WorkspaceGidAddUserBody](docs/WorkspaceGidAddUserBody.md)
 - [WorkspaceGidProjectsBody](docs/WorkspaceGidProjectsBody.md)
 - [WorkspaceGidRemoveUserBody](docs/WorkspaceGidRemoveUserBody.md)
 - [WorkspaceGidTagsBody](docs/WorkspaceGidTagsBody.md)
 - [WorkspaceMembershipBase](docs/WorkspaceMembershipBase.md)
 - [WorkspaceMembershipCompact](docs/WorkspaceMembershipCompact.md)
 - [WorkspaceMembershipRequest](docs/WorkspaceMembershipRequest.md)
 - [WorkspaceMembershipResponse](docs/WorkspaceMembershipResponse.md)
 - [WorkspaceMembershipResponseArray](docs/WorkspaceMembershipResponseArray.md)
 - [WorkspaceMembershipResponseData](docs/WorkspaceMembershipResponseData.md)
 - [WorkspaceMembershipResponseUserTaskList](docs/WorkspaceMembershipResponseUserTaskList.md)
 - [WorkspaceMembershipResponseVacationDates](docs/WorkspaceMembershipResponseVacationDates.md)
 - [WorkspaceRemoveUserRequest](docs/WorkspaceRemoveUserRequest.md)
 - [WorkspaceRequest](docs/WorkspaceRequest.md)
 - [WorkspaceResponse](docs/WorkspaceResponse.md)
 - [WorkspaceResponseArray](docs/WorkspaceResponseArray.md)
 - [WorkspaceResponseData](docs/WorkspaceResponseData.md)
 - [WorkspacesWorkspaceGidBody](docs/WorkspacesWorkspaceGidBody.md)

## Documentation For Authorization


## oauth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://app.asana.com/-/oauth_authorize
- **Scopes**: 
 - **default**: Provides access to all endpoints documented in our API reference. If no scopes are requested, this scope is assumed by default.
 - **openid**: Provides access to OpenID Connect ID tokens and the OpenID Connect user info endpoint.
 - **email**: Provides access to the user’s email through the OpenID Connect user info endpoint.
 - **profile**: Provides access to the user’s name and profile photo through the OpenID Connect user info endpoint.


## Getting events

In order to get events you will need a sync token. This sync token can be acquired in the error message from the initial
request to [get_events](docs/EventsApi.md#get_events).

```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
events_api_instance = asana.EventsApi(api_client)
resource = '12345' # str | A resource ID to subscribe to. The resource can be a task or project.
sync = '' # str | A sync token received from the last request, or none on first sync. Events will be returned from the point in time that the sync token was generated. *Note: On your first request, omit the sync token. The response will be the same as for an expired sync token, and will include a new valid sync token.If the sync token is too old (which may happen from time to time) the API will return a `412 Precondition Failed` error, and include a fresh sync token in the response.* (optional)

try:
    # Initial request to get the sync token
    api_response = events_api_instance.get_events(resource, sync=sync)
except ApiException as e:
    # Set the sync token
    sync = json.loads(e.body.decode('utf-8'))['sync']

try:
    # Follow up request to get events
    api_response = events_api_instance.get_events(resource, sync=sync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events: %s\n" % e)
```

## Pagination

```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
task_api_instance = asana.TasksApi(api_client)
limit = 10 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
project = '321654' # str | The project to filter tasks on. (optional)

try:
    # Get multiple tasks with next_page
    offset = None
    while True:
        # If the "offset" is None make a request without providing the offset query parameter
        # Asana throws an error if we make a request with a "offset" query param of None
        if offset is None:
            api_response = task_api_instance.get_tasks(limit=limit, project=project)
        else:
            api_response = task_api_instance.get_tasks(limit=limit, project=project, offset=offset)

        # Do something
        # EX: print response
        pprint(api_response)

        # Check to see if there is a next_page
        if api_response.next_page:
            offset = api_response.next_page.offset
        else:
            break
except ApiException as e:
  print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

## Accessing repsonse data

By default, the client library returns a class object of the resource. You can use dot notation to access the response data.

TIP: look at the "Return type" section of the documented endpoint to understand which properties are accessible. (EX: [get_task](docs/TasksApi.md#get_task))

### Example: Accessing task data (dot notation)
```python
.
.
.
try:
    task = tasks_api_instance.get_task(task_gid).data
    task_name = task.name
    task_notes = task.notes
except ApiException as e:
    .
    .
    .
```

If you would like to convert the class object into a dictionary and access the data via bracket notation, you can use the `to_dict()` method.

### Example: Accessing task data (bracket notation)
```python
.
.
.
try:
    task_dict = tasks_api_instance.get_task(task_gid).to_dict()
    task_dict_data = task_dict['data']
    task_name = task_dict_data['name']
    task_notes = task_dict_data['notes']
except ApiException as e:
    .
    .
    .
```

## Accessing response status code and headers

In the scenario you want to access the response headers or the status code along with the response data you can
provide the `_return_http_data_only` parameter argument in the request method and set the value to `False`

```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.UsersApi(api_client)
user_gid = 'me' # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.

try:
    # Get a user - Add asana-enable in the request
    api_response = api_instance.get_user(user_gid, _return_http_data_only=False) # returns a tuple: (object, status, headers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

## Adding deprecation flag to your "asana-enable" header

### On the client
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# Add asana-enable header for the client
api_client.default_headers['asana-enable'] = 'string_ids'
```

OR

### On the request
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.UsersApi(api_client)
user_gid = 'me' # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.

try:
    # Get a user - Add asana-enable in the request
    api_response = api_instance.get_user(user_gid, header_params={'asana-enable': 'string_ids'})
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

## Documentation for Using the `call_api` method

Use this to make HTTP calls when the endpoint does not exist in the current library version or has bugs

### Example: GET, POST, PUT, DELETE on tasks

#### GET - get a task
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

try:
    # GET - get a task
    api_response = api_client.call_api(
        "/tasks/{task_gid}",
        "GET",
        path_params={"task_gid": "<YOUR_TASK_GID>"},
        query_params=[],
        header_params={"Accept": "application/json; charset=utf-8"},
        body=None,
        post_params=[],
        files={},
        response_type=object, # If there is an existing response model for the resource you can use that EX: "TaskResponseData" or you can specify one of the following types: float, bool, bytes, str, object
        auth_settings=["oauth2"],
        async_req=None,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
        collection_formats={},
    )
    pprint(api_response)
except ApiException as e:
    print("Exception: %s\n" % e)
```

#### GET - get multiple tasks -> with opt_fields
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

try:
    # GET - get multiple tasks
    api_response = api_client.call_api(
        "/tasks",
        "GET",
        path_params={},
        query_params=[('opt_fields', 'name,notes,projects')],
        header_params={"Accept": "application/json; charset=utf-8"},
        body=None,
        post_params=[],
        files={},
        response_type=object, # If there is an existing response model for the resource you can use that EX: "TaskResponseData" or you can specify one of the following types: float, bool, bytes, str, object
        auth_settings=["oauth2"],
        async_req=None,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
        collection_formats={},
    )
    pprint(api_response)
except ApiException as e:
    print("Exception: %s\n" % e)
```

#### POST - create a task
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

try:
    # POST - create a task
    api_response = api_client.call_api(
        "/tasks",
        "POST",
        path_params={},
        query_params=[],
        header_params={
            "Accept": "application/json; charset=utf-8",
            "Content-Type": "application/json; charset=utf-8",
        },
        body={
            "data": {
                "name": "New Task",
                "projects": ["<YOUR_PROJECT_GID>"],
            }
        },
        post_params=[],
        files={},
        response_type=object, # If there is an existing response model for the resource you can use that EX: "TaskResponseData" or you can specify one of the following types: float, bool, bytes, str, object
        auth_settings=["oauth2"],
        async_req=None,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
        collection_formats={},
    )
    pprint(api_response)
except ApiException as e:
    print("Exception: %s\n" % e)
```

#### PUT - update a task
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

try:
    # PUT - update a task
    api_response = api_client.call_api(
        "/tasks/{task_gid}",
        "PUT",
        path_params={"task_gid": "<YOUR_TASK_GID>"},
        query_params=[],
        header_params={
            "Accept": "application/json; charset=utf-8",
            "Content-Type": "application/json; charset=utf-8",
        },
        body={
            "data": {
                "name": "Updated Task",
            }
        },
        post_params=[],
        files={},
        response_type=object, # If there is an existing response model for the resource you can use that EX: "TaskResponseData" or you can specify one of the following types: float, bool, bytes, str, object
        auth_settings=["oauth2"],
        async_req=None,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
        collection_formats={},
    )
    pprint(api_response)
except ApiException as e:
    print("Exception: %s\n" % e)
```

#### DELETE - delete a task
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: 
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

try:
    # DELETE - delete a task
    api_response = api_client.call_api(
        "/tasks/{task_gid}",
        "DELETE",
        path_params={"task_gid": "<YOUR_TASK_GID>"},
        query_params=[],
        header_params={"Accept": "application/json; charset=utf-8"},
        body=None,
        post_params=[],
        files={},
        response_type=object, # If there is an existing response model for the resource you can use that EX: "EmptyResponseData" or you can specify one of the following types: float, bool, bytes, str, object
        auth_settings=["oauth2"],
        async_req=None,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
        collection_formats={},
    )
    pprint(api_response)
except ApiException as e:
    print("Exception: %s\n" % e)
```

## Author



[release-image]: https://img.shields.io/github/release/asana/python-asana.svg

[github-actions-image]: https://github.com/Asana/python-asana/workflows/Build/badge.svg
[github-actions-url]: https://github.com/Asana/python-asana/actions

[pypi-image]: https://img.shields.io/pypi/v/asana.svg?style=flat-square
[pypi-url]: https://pypi.python.org/pypi/asana/
