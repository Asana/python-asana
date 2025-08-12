# asana [![GitHub release][release-image]]() [![PyPi Version][pypi-image]][pypi-url]

- API version: 1.0
- Package version: 5.2.1

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

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
users_api_instance = asana.UsersApi(api_client)
user_gid = "me"
opts = {}

try:
    # Get a user
    user = users_api_instance.get_user(user_gid, opts)
    pprint(user)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Example: GET, POST, PUT, DELETE on tasks

#### GET - get multiple tasks
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tasks_api_instance = asana.TasksApi(api_client)
opts = { 
    'limit': 50,
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9",
    'assignee': "14641",
    'project': "321654",
    'section': "321654",
    'workspace': "321654",
    'completed_since': '2012-02-22T02:06:58.158Z',
    'modified_since': '2012-02-22T02:06:58.158Z',
    'opt_fields': "actual_time_minutes,approval_status,assignee,assignee.name,assignee_section,assignee_section.name,assignee_status,completed,completed_at,completed_by,completed_by.name,created_at,created_by,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,dependencies,dependents,due_at,due_on,external,external.data,followers,followers.name,hearted,hearts,hearts.user,hearts.user.name,html_notes,is_rendered_as_separator,liked,likes,likes.user,likes.user.name,memberships,memberships.project,memberships.project.name,memberships.section,memberships.section.name,modified_at,name,notes,num_hearts,num_likes,num_subtasks,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permalink_url,projects,projects.name,resource_subtype,start_at,start_on,tags,tags.name,uri,workspace,workspace.name"
}

try:
    # Get multiple tasks
    tasks = tasks_api_instance.get_tasks(opts)
    for task in tasks:
        pprint(task)
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

#### POST - create a task
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tasks_api_instance = asana.TasksApi(api_client)
body = {
    "data": {
        "name": "New Task",
        "projects": ["<YOUR_PROJECT_GID>"],
    }
}
opts = {}

try:
    # Create a task
    task = tasks_api_instance.create_task(body, opts)
    pprint(task)
except ApiException as e:
    print("Exception when calling TasksApi->create_task: %s\n" % e)
```

#### PUT - update a task
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tasks_api_instance = asana.TasksApi(api_client)
body = {
    "data": {
        "name": "Updated Task",
    }
}
task_gid = "<YOUR_TASK_GID>"
opts = {}

try:
    # Update a task
    task = tasks_api_instance.update_task(body, task_gid, opts)
    pprint(task)
except ApiException as e:
    print("Exception when calling TasksApi->update_task: %s\n" % e)
```

#### DELETE - delete a task
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tasks_api_instance = asana.TasksApi(api_client)
task_gid = "<YOUR_TASK_GID>"

try:
    # Delete a task
    task = tasks_api_instance.delete_task(task_gid)
    pprint(task)
except ApiException as e:
    print("Exception when calling TasksApi->delete_task: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://app.asana.com/api/1.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AllocationsApi* | [**create_allocation**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/AllocationsApi.md#create_allocation) | **POST** /allocations | Create an allocation
*AllocationsApi* | [**delete_allocation**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/AllocationsApi.md#delete_allocation) | **DELETE** /allocations/{allocation_gid} | Delete an allocation
*AllocationsApi* | [**get_allocation**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/AllocationsApi.md#get_allocation) | **GET** /allocations/{allocation_gid} | Get an allocation
*AllocationsApi* | [**get_allocations**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/AllocationsApi.md#get_allocations) | **GET** /allocations | Get multiple allocations
*AllocationsApi* | [**update_allocation**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/AllocationsApi.md#update_allocation) | **PUT** /allocations/{allocation_gid} | Update an allocation
*AttachmentsApi* | [**create_attachment_for_object**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/AttachmentsApi.md#create_attachment_for_object) | **POST** /attachments | Upload an attachment
*AttachmentsApi* | [**delete_attachment**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/AttachmentsApi.md#delete_attachment) | **DELETE** /attachments/{attachment_gid} | Delete an attachment
*AttachmentsApi* | [**get_attachment**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/AttachmentsApi.md#get_attachment) | **GET** /attachments/{attachment_gid} | Get an attachment
*AttachmentsApi* | [**get_attachments_for_object**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/AttachmentsApi.md#get_attachments_for_object) | **GET** /attachments | Get attachments from an object
*AuditLogAPIApi* | [**get_audit_log_events**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/AuditLogAPIApi.md#get_audit_log_events) | **GET** /workspaces/{workspace_gid}/audit_log_events | Get audit log events
*BatchAPIApi* | [**create_batch_request**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/BatchAPIApi.md#create_batch_request) | **POST** /batch | Submit parallel requests
*CustomFieldSettingsApi* | [**get_custom_field_settings_for_portfolio**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/CustomFieldSettingsApi.md#get_custom_field_settings_for_portfolio) | **GET** /portfolios/{portfolio_gid}/custom_field_settings | Get a portfolio&#x27;s custom fields
*CustomFieldSettingsApi* | [**get_custom_field_settings_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/CustomFieldSettingsApi.md#get_custom_field_settings_for_project) | **GET** /projects/{project_gid}/custom_field_settings | Get a project&#x27;s custom fields
*CustomFieldsApi* | [**create_custom_field**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/CustomFieldsApi.md#create_custom_field) | **POST** /custom_fields | Create a custom field
*CustomFieldsApi* | [**create_enum_option_for_custom_field**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/CustomFieldsApi.md#create_enum_option_for_custom_field) | **POST** /custom_fields/{custom_field_gid}/enum_options | Create an enum option
*CustomFieldsApi* | [**delete_custom_field**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/CustomFieldsApi.md#delete_custom_field) | **DELETE** /custom_fields/{custom_field_gid} | Delete a custom field
*CustomFieldsApi* | [**get_custom_field**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/CustomFieldsApi.md#get_custom_field) | **GET** /custom_fields/{custom_field_gid} | Get a custom field
*CustomFieldsApi* | [**get_custom_fields_for_workspace**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/CustomFieldsApi.md#get_custom_fields_for_workspace) | **GET** /workspaces/{workspace_gid}/custom_fields | Get a workspace&#x27;s custom fields
*CustomFieldsApi* | [**insert_enum_option_for_custom_field**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/CustomFieldsApi.md#insert_enum_option_for_custom_field) | **POST** /custom_fields/{custom_field_gid}/enum_options/insert | Reorder a custom field&#x27;s enum
*CustomFieldsApi* | [**update_custom_field**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/CustomFieldsApi.md#update_custom_field) | **PUT** /custom_fields/{custom_field_gid} | Update a custom field
*CustomFieldsApi* | [**update_enum_option**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/CustomFieldsApi.md#update_enum_option) | **PUT** /enum_options/{enum_option_gid} | Update an enum option
*CustomTypesApi* | [**get_custom_type**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/CustomTypesApi.md#get_custom_type) | **GET** /custom_types/{custom_type_gid} | Get a custom type
*CustomTypesApi* | [**get_custom_types**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/CustomTypesApi.md#get_custom_types) | **GET** /custom_types | Get all custom types associated with an object
*EventsApi* | [**get_events**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/EventsApi.md#get_events) | **GET** /events | Get events on a resource
*ExportsApi* | [**create_graph_export**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ExportsApi.md#create_graph_export) | **POST** /exports/graph | Initiate a graph export
*ExportsApi* | [**create_resource_export**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ExportsApi.md#create_resource_export) | **POST** /exports/resource | Initiate a resource export
*GoalRelationshipsApi* | [**add_supporting_relationship**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalRelationshipsApi.md#add_supporting_relationship) | **POST** /goals/{goal_gid}/addSupportingRelationship | Add a supporting goal relationship
*GoalRelationshipsApi* | [**get_goal_relationship**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalRelationshipsApi.md#get_goal_relationship) | **GET** /goal_relationships/{goal_relationship_gid} | Get a goal relationship
*GoalRelationshipsApi* | [**get_goal_relationships**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalRelationshipsApi.md#get_goal_relationships) | **GET** /goal_relationships | Get goal relationships
*GoalRelationshipsApi* | [**remove_supporting_relationship**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalRelationshipsApi.md#remove_supporting_relationship) | **POST** /goals/{goal_gid}/removeSupportingRelationship | Removes a supporting goal relationship
*GoalRelationshipsApi* | [**update_goal_relationship**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalRelationshipsApi.md#update_goal_relationship) | **PUT** /goal_relationships/{goal_relationship_gid} | Update a goal relationship
*GoalsApi* | [**add_followers**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalsApi.md#add_followers) | **POST** /goals/{goal_gid}/addFollowers | Add a collaborator to a goal
*GoalsApi* | [**create_goal**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalsApi.md#create_goal) | **POST** /goals | Create a goal
*GoalsApi* | [**create_goal_metric**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalsApi.md#create_goal_metric) | **POST** /goals/{goal_gid}/setMetric | Create a goal metric
*GoalsApi* | [**delete_goal**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalsApi.md#delete_goal) | **DELETE** /goals/{goal_gid} | Delete a goal
*GoalsApi* | [**get_goal**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalsApi.md#get_goal) | **GET** /goals/{goal_gid} | Get a goal
*GoalsApi* | [**get_goals**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalsApi.md#get_goals) | **GET** /goals | Get goals
*GoalsApi* | [**get_parent_goals_for_goal**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalsApi.md#get_parent_goals_for_goal) | **GET** /goals/{goal_gid}/parentGoals | Get parent goals from a goal
*GoalsApi* | [**remove_followers**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalsApi.md#remove_followers) | **POST** /goals/{goal_gid}/removeFollowers | Remove a collaborator from a goal
*GoalsApi* | [**update_goal**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalsApi.md#update_goal) | **PUT** /goals/{goal_gid} | Update a goal
*GoalsApi* | [**update_goal_metric**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/GoalsApi.md#update_goal_metric) | **POST** /goals/{goal_gid}/setMetricCurrentValue | Update a goal metric
*JobsApi* | [**get_job**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/JobsApi.md#get_job) | **GET** /jobs/{job_gid} | Get a job by id
*MembershipsApi* | [**create_membership**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/MembershipsApi.md#create_membership) | **POST** /memberships | Create a membership
*MembershipsApi* | [**delete_membership**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/MembershipsApi.md#delete_membership) | **DELETE** /memberships/{membership_gid} | Delete a membership
*MembershipsApi* | [**get_membership**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/MembershipsApi.md#get_membership) | **GET** /memberships/{membership_gid} | Get a membership
*MembershipsApi* | [**get_memberships**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/MembershipsApi.md#get_memberships) | **GET** /memberships | Get multiple memberships
*MembershipsApi* | [**update_membership**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/MembershipsApi.md#update_membership) | **PUT** /memberships/{membership_gid} | Update a membership
*OrganizationExportsApi* | [**create_organization_export**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/OrganizationExportsApi.md#create_organization_export) | **POST** /organization_exports | Create an organization export request
*OrganizationExportsApi* | [**get_organization_export**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/OrganizationExportsApi.md#get_organization_export) | **GET** /organization_exports/{organization_export_gid} | Get details on an org export request
*PortfolioMembershipsApi* | [**get_portfolio_membership**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfolioMembershipsApi.md#get_portfolio_membership) | **GET** /portfolio_memberships/{portfolio_membership_gid} | Get a portfolio membership
*PortfolioMembershipsApi* | [**get_portfolio_memberships**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfolioMembershipsApi.md#get_portfolio_memberships) | **GET** /portfolio_memberships | Get multiple portfolio memberships
*PortfolioMembershipsApi* | [**get_portfolio_memberships_for_portfolio**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfolioMembershipsApi.md#get_portfolio_memberships_for_portfolio) | **GET** /portfolios/{portfolio_gid}/portfolio_memberships | Get memberships from a portfolio
*PortfoliosApi* | [**add_custom_field_setting_for_portfolio**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfoliosApi.md#add_custom_field_setting_for_portfolio) | **POST** /portfolios/{portfolio_gid}/addCustomFieldSetting | Add a custom field to a portfolio
*PortfoliosApi* | [**add_item_for_portfolio**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfoliosApi.md#add_item_for_portfolio) | **POST** /portfolios/{portfolio_gid}/addItem | Add a portfolio item
*PortfoliosApi* | [**add_members_for_portfolio**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfoliosApi.md#add_members_for_portfolio) | **POST** /portfolios/{portfolio_gid}/addMembers | Add users to a portfolio
*PortfoliosApi* | [**create_portfolio**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfoliosApi.md#create_portfolio) | **POST** /portfolios | Create a portfolio
*PortfoliosApi* | [**delete_portfolio**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfoliosApi.md#delete_portfolio) | **DELETE** /portfolios/{portfolio_gid} | Delete a portfolio
*PortfoliosApi* | [**get_items_for_portfolio**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfoliosApi.md#get_items_for_portfolio) | **GET** /portfolios/{portfolio_gid}/items | Get portfolio items
*PortfoliosApi* | [**get_portfolio**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfoliosApi.md#get_portfolio) | **GET** /portfolios/{portfolio_gid} | Get a portfolio
*PortfoliosApi* | [**get_portfolios**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfoliosApi.md#get_portfolios) | **GET** /portfolios | Get multiple portfolios
*PortfoliosApi* | [**remove_custom_field_setting_for_portfolio**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfoliosApi.md#remove_custom_field_setting_for_portfolio) | **POST** /portfolios/{portfolio_gid}/removeCustomFieldSetting | Remove a custom field from a portfolio
*PortfoliosApi* | [**remove_item_for_portfolio**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfoliosApi.md#remove_item_for_portfolio) | **POST** /portfolios/{portfolio_gid}/removeItem | Remove a portfolio item
*PortfoliosApi* | [**remove_members_for_portfolio**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfoliosApi.md#remove_members_for_portfolio) | **POST** /portfolios/{portfolio_gid}/removeMembers | Remove users from a portfolio
*PortfoliosApi* | [**update_portfolio**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/PortfoliosApi.md#update_portfolio) | **PUT** /portfolios/{portfolio_gid} | Update a portfolio
*ProjectBriefsApi* | [**create_project_brief**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectBriefsApi.md#create_project_brief) | **POST** /projects/{project_gid}/project_briefs | Create a project brief
*ProjectBriefsApi* | [**delete_project_brief**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectBriefsApi.md#delete_project_brief) | **DELETE** /project_briefs/{project_brief_gid} | Delete a project brief
*ProjectBriefsApi* | [**get_project_brief**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectBriefsApi.md#get_project_brief) | **GET** /project_briefs/{project_brief_gid} | Get a project brief
*ProjectBriefsApi* | [**update_project_brief**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectBriefsApi.md#update_project_brief) | **PUT** /project_briefs/{project_brief_gid} | Update a project brief
*ProjectMembershipsApi* | [**get_project_membership**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectMembershipsApi.md#get_project_membership) | **GET** /project_memberships/{project_membership_gid} | Get a project membership
*ProjectMembershipsApi* | [**get_project_memberships_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectMembershipsApi.md#get_project_memberships_for_project) | **GET** /projects/{project_gid}/project_memberships | Get memberships from a project
*ProjectStatusesApi* | [**create_project_status_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectStatusesApi.md#create_project_status_for_project) | **POST** /projects/{project_gid}/project_statuses | Create a project status
*ProjectStatusesApi* | [**delete_project_status**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectStatusesApi.md#delete_project_status) | **DELETE** /project_statuses/{project_status_gid} | Delete a project status
*ProjectStatusesApi* | [**get_project_status**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectStatusesApi.md#get_project_status) | **GET** /project_statuses/{project_status_gid} | Get a project status
*ProjectStatusesApi* | [**get_project_statuses_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectStatusesApi.md#get_project_statuses_for_project) | **GET** /projects/{project_gid}/project_statuses | Get statuses from a project
*ProjectTemplatesApi* | [**delete_project_template**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectTemplatesApi.md#delete_project_template) | **DELETE** /project_templates/{project_template_gid} | Delete a project template
*ProjectTemplatesApi* | [**get_project_template**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectTemplatesApi.md#get_project_template) | **GET** /project_templates/{project_template_gid} | Get a project template
*ProjectTemplatesApi* | [**get_project_templates**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectTemplatesApi.md#get_project_templates) | **GET** /project_templates | Get multiple project templates
*ProjectTemplatesApi* | [**get_project_templates_for_team**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectTemplatesApi.md#get_project_templates_for_team) | **GET** /teams/{team_gid}/project_templates | Get a team&#x27;s project templates
*ProjectTemplatesApi* | [**instantiate_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectTemplatesApi.md#instantiate_project) | **POST** /project_templates/{project_template_gid}/instantiateProject | Instantiate a project from a project template
*ProjectsApi* | [**add_custom_field_setting_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#add_custom_field_setting_for_project) | **POST** /projects/{project_gid}/addCustomFieldSetting | Add a custom field to a project
*ProjectsApi* | [**add_followers_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#add_followers_for_project) | **POST** /projects/{project_gid}/addFollowers | Add followers to a project
*ProjectsApi* | [**add_members_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#add_members_for_project) | **POST** /projects/{project_gid}/addMembers | Add users to a project
*ProjectsApi* | [**create_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#create_project) | **POST** /projects | Create a project
*ProjectsApi* | [**create_project_for_team**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#create_project_for_team) | **POST** /teams/{team_gid}/projects | Create a project in a team
*ProjectsApi* | [**create_project_for_workspace**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#create_project_for_workspace) | **POST** /workspaces/{workspace_gid}/projects | Create a project in a workspace
*ProjectsApi* | [**delete_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#delete_project) | **DELETE** /projects/{project_gid} | Delete a project
*ProjectsApi* | [**duplicate_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#duplicate_project) | **POST** /projects/{project_gid}/duplicate | Duplicate a project
*ProjectsApi* | [**get_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#get_project) | **GET** /projects/{project_gid} | Get a project
*ProjectsApi* | [**get_projects**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#get_projects) | **GET** /projects | Get multiple projects
*ProjectsApi* | [**get_projects_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#get_projects_for_task) | **GET** /tasks/{task_gid}/projects | Get projects a task is in
*ProjectsApi* | [**get_projects_for_team**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#get_projects_for_team) | **GET** /teams/{team_gid}/projects | Get a team&#x27;s projects
*ProjectsApi* | [**get_projects_for_workspace**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#get_projects_for_workspace) | **GET** /workspaces/{workspace_gid}/projects | Get all projects in a workspace
*ProjectsApi* | [**get_task_counts_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#get_task_counts_for_project) | **GET** /projects/{project_gid}/task_counts | Get task count of a project
*ProjectsApi* | [**project_save_as_template**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#project_save_as_template) | **POST** /projects/{project_gid}/saveAsTemplate | Create a project template from a project
*ProjectsApi* | [**remove_custom_field_setting_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#remove_custom_field_setting_for_project) | **POST** /projects/{project_gid}/removeCustomFieldSetting | Remove a custom field from a project
*ProjectsApi* | [**remove_followers_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#remove_followers_for_project) | **POST** /projects/{project_gid}/removeFollowers | Remove followers from a project
*ProjectsApi* | [**remove_members_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#remove_members_for_project) | **POST** /projects/{project_gid}/removeMembers | Remove users from a project
*ProjectsApi* | [**update_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#update_project) | **PUT** /projects/{project_gid} | Update a project
*RulesApi* | [**trigger_rule**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/RulesApi.md#trigger_rule) | **POST** /rule_triggers/{rule_trigger_gid}/run | Trigger a rule
*SectionsApi* | [**add_task_for_section**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/SectionsApi.md#add_task_for_section) | **POST** /sections/{section_gid}/addTask | Add task to section
*SectionsApi* | [**create_section_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/SectionsApi.md#create_section_for_project) | **POST** /projects/{project_gid}/sections | Create a section in a project
*SectionsApi* | [**delete_section**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/SectionsApi.md#delete_section) | **DELETE** /sections/{section_gid} | Delete a section
*SectionsApi* | [**get_section**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/SectionsApi.md#get_section) | **GET** /sections/{section_gid} | Get a section
*SectionsApi* | [**get_sections_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/SectionsApi.md#get_sections_for_project) | **GET** /projects/{project_gid}/sections | Get sections in a project
*SectionsApi* | [**insert_section_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/SectionsApi.md#insert_section_for_project) | **POST** /projects/{project_gid}/sections/insert | Move or Insert sections
*SectionsApi* | [**update_section**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/SectionsApi.md#update_section) | **PUT** /sections/{section_gid} | Update a section
*StatusUpdatesApi* | [**create_status_for_object**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/StatusUpdatesApi.md#create_status_for_object) | **POST** /status_updates | Create a status update
*StatusUpdatesApi* | [**delete_status**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/StatusUpdatesApi.md#delete_status) | **DELETE** /status_updates/{status_update_gid} | Delete a status update
*StatusUpdatesApi* | [**get_status**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/StatusUpdatesApi.md#get_status) | **GET** /status_updates/{status_update_gid} | Get a status update
*StatusUpdatesApi* | [**get_statuses_for_object**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/StatusUpdatesApi.md#get_statuses_for_object) | **GET** /status_updates | Get status updates from an object
*StoriesApi* | [**create_story_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/StoriesApi.md#create_story_for_task) | **POST** /tasks/{task_gid}/stories | Create a story on a task
*StoriesApi* | [**delete_story**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/StoriesApi.md#delete_story) | **DELETE** /stories/{story_gid} | Delete a story
*StoriesApi* | [**get_stories_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/StoriesApi.md#get_stories_for_task) | **GET** /tasks/{task_gid}/stories | Get stories from a task
*StoriesApi* | [**get_story**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/StoriesApi.md#get_story) | **GET** /stories/{story_gid} | Get a story
*StoriesApi* | [**update_story**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/StoriesApi.md#update_story) | **PUT** /stories/{story_gid} | Update a story
*TagsApi* | [**create_tag**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TagsApi.md#create_tag) | **POST** /tags | Create a tag
*TagsApi* | [**create_tag_for_workspace**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TagsApi.md#create_tag_for_workspace) | **POST** /workspaces/{workspace_gid}/tags | Create a tag in a workspace
*TagsApi* | [**delete_tag**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TagsApi.md#delete_tag) | **DELETE** /tags/{tag_gid} | Delete a tag
*TagsApi* | [**get_tag**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TagsApi.md#get_tag) | **GET** /tags/{tag_gid} | Get a tag
*TagsApi* | [**get_tags**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TagsApi.md#get_tags) | **GET** /tags | Get multiple tags
*TagsApi* | [**get_tags_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TagsApi.md#get_tags_for_task) | **GET** /tasks/{task_gid}/tags | Get a task&#x27;s tags
*TagsApi* | [**get_tags_for_workspace**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TagsApi.md#get_tags_for_workspace) | **GET** /workspaces/{workspace_gid}/tags | Get tags in a workspace
*TagsApi* | [**update_tag**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TagsApi.md#update_tag) | **PUT** /tags/{tag_gid} | Update a tag
*TaskTemplatesApi* | [**delete_task_template**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TaskTemplatesApi.md#delete_task_template) | **DELETE** /task_templates/{task_template_gid} | Delete a task template
*TaskTemplatesApi* | [**get_task_template**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TaskTemplatesApi.md#get_task_template) | **GET** /task_templates/{task_template_gid} | Get a task template
*TaskTemplatesApi* | [**get_task_templates**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TaskTemplatesApi.md#get_task_templates) | **GET** /task_templates | Get multiple task templates
*TaskTemplatesApi* | [**instantiate_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TaskTemplatesApi.md#instantiate_task) | **POST** /task_templates/{task_template_gid}/instantiateTask | Instantiate a task from a task template
*TasksApi* | [**add_dependencies_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#add_dependencies_for_task) | **POST** /tasks/{task_gid}/addDependencies | Set dependencies for a task
*TasksApi* | [**add_dependents_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#add_dependents_for_task) | **POST** /tasks/{task_gid}/addDependents | Set dependents for a task
*TasksApi* | [**add_followers_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#add_followers_for_task) | **POST** /tasks/{task_gid}/addFollowers | Add followers to a task
*TasksApi* | [**add_project_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#add_project_for_task) | **POST** /tasks/{task_gid}/addProject | Add a project to a task
*TasksApi* | [**add_tag_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#add_tag_for_task) | **POST** /tasks/{task_gid}/addTag | Add a tag to a task
*TasksApi* | [**create_subtask_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#create_subtask_for_task) | **POST** /tasks/{task_gid}/subtasks | Create a subtask
*TasksApi* | [**create_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#create_task) | **POST** /tasks | Create a task
*TasksApi* | [**delete_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#delete_task) | **DELETE** /tasks/{task_gid} | Delete a task
*TasksApi* | [**duplicate_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#duplicate_task) | **POST** /tasks/{task_gid}/duplicate | Duplicate a task
*TasksApi* | [**get_dependencies_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#get_dependencies_for_task) | **GET** /tasks/{task_gid}/dependencies | Get dependencies from a task
*TasksApi* | [**get_dependents_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#get_dependents_for_task) | **GET** /tasks/{task_gid}/dependents | Get dependents from a task
*TasksApi* | [**get_subtasks_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#get_subtasks_for_task) | **GET** /tasks/{task_gid}/subtasks | Get subtasks from a task
*TasksApi* | [**get_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#get_task) | **GET** /tasks/{task_gid} | Get a task
*TasksApi* | [**get_task_for_custom_id**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#get_task_for_custom_id) | **GET** /workspaces/{workspace_gid}/tasks/custom_id/{custom_id} | Get a task for a given custom ID
*TasksApi* | [**get_tasks**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#get_tasks) | **GET** /tasks | Get multiple tasks
*TasksApi* | [**get_tasks_for_project**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#get_tasks_for_project) | **GET** /projects/{project_gid}/tasks | Get tasks from a project
*TasksApi* | [**get_tasks_for_section**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#get_tasks_for_section) | **GET** /sections/{section_gid}/tasks | Get tasks from a section
*TasksApi* | [**get_tasks_for_tag**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#get_tasks_for_tag) | **GET** /tags/{tag_gid}/tasks | Get tasks from a tag
*TasksApi* | [**get_tasks_for_user_task_list**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#get_tasks_for_user_task_list) | **GET** /user_task_lists/{user_task_list_gid}/tasks | Get tasks from a user task list
*TasksApi* | [**remove_dependencies_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#remove_dependencies_for_task) | **POST** /tasks/{task_gid}/removeDependencies | Unlink dependencies from a task
*TasksApi* | [**remove_dependents_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#remove_dependents_for_task) | **POST** /tasks/{task_gid}/removeDependents | Unlink dependents from a task
*TasksApi* | [**remove_follower_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#remove_follower_for_task) | **POST** /tasks/{task_gid}/removeFollowers | Remove followers from a task
*TasksApi* | [**remove_project_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#remove_project_for_task) | **POST** /tasks/{task_gid}/removeProject | Remove a project from a task
*TasksApi* | [**remove_tag_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#remove_tag_for_task) | **POST** /tasks/{task_gid}/removeTag | Remove a tag from a task
*TasksApi* | [**search_tasks_for_workspace**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#search_tasks_for_workspace) | **GET** /workspaces/{workspace_gid}/tasks/search | Search tasks in a workspace
*TasksApi* | [**set_parent_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#set_parent_for_task) | **POST** /tasks/{task_gid}/setParent | Set the parent of a task
*TasksApi* | [**update_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#update_task) | **PUT** /tasks/{task_gid} | Update a task
*TeamMembershipsApi* | [**get_team_membership**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TeamMembershipsApi.md#get_team_membership) | **GET** /team_memberships/{team_membership_gid} | Get a team membership
*TeamMembershipsApi* | [**get_team_memberships**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TeamMembershipsApi.md#get_team_memberships) | **GET** /team_memberships | Get team memberships
*TeamMembershipsApi* | [**get_team_memberships_for_team**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TeamMembershipsApi.md#get_team_memberships_for_team) | **GET** /teams/{team_gid}/team_memberships | Get memberships from a team
*TeamMembershipsApi* | [**get_team_memberships_for_user**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TeamMembershipsApi.md#get_team_memberships_for_user) | **GET** /users/{user_gid}/team_memberships | Get memberships from a user
*TeamsApi* | [**add_user_for_team**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TeamsApi.md#add_user_for_team) | **POST** /teams/{team_gid}/addUser | Add a user to a team
*TeamsApi* | [**create_team**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TeamsApi.md#create_team) | **POST** /teams | Create a team
*TeamsApi* | [**get_team**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TeamsApi.md#get_team) | **GET** /teams/{team_gid} | Get a team
*TeamsApi* | [**get_teams_for_user**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TeamsApi.md#get_teams_for_user) | **GET** /users/{user_gid}/teams | Get teams for a user
*TeamsApi* | [**get_teams_for_workspace**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TeamsApi.md#get_teams_for_workspace) | **GET** /workspaces/{workspace_gid}/teams | Get teams in a workspace
*TeamsApi* | [**remove_user_for_team**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TeamsApi.md#remove_user_for_team) | **POST** /teams/{team_gid}/removeUser | Remove a user from a team
*TeamsApi* | [**update_team**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TeamsApi.md#update_team) | **PUT** /teams/{team_gid} | Update a team
*TimePeriodsApi* | [**get_time_period**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TimePeriodsApi.md#get_time_period) | **GET** /time_periods/{time_period_gid} | Get a time period
*TimePeriodsApi* | [**get_time_periods**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TimePeriodsApi.md#get_time_periods) | **GET** /time_periods | Get time periods
*TimeTrackingEntriesApi* | [**create_time_tracking_entry**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TimeTrackingEntriesApi.md#create_time_tracking_entry) | **POST** /tasks/{task_gid}/time_tracking_entries | Create a time tracking entry
*TimeTrackingEntriesApi* | [**delete_time_tracking_entry**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TimeTrackingEntriesApi.md#delete_time_tracking_entry) | **DELETE** /time_tracking_entries/{time_tracking_entry_gid} | Delete a time tracking entry
*TimeTrackingEntriesApi* | [**get_time_tracking_entries**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TimeTrackingEntriesApi.md#get_time_tracking_entries) | **GET** /time_tracking_entries | Get multiple time tracking entries
*TimeTrackingEntriesApi* | [**get_time_tracking_entries_for_task**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TimeTrackingEntriesApi.md#get_time_tracking_entries_for_task) | **GET** /tasks/{task_gid}/time_tracking_entries | Get time tracking entries for a task
*TimeTrackingEntriesApi* | [**get_time_tracking_entry**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TimeTrackingEntriesApi.md#get_time_tracking_entry) | **GET** /time_tracking_entries/{time_tracking_entry_gid} | Get a time tracking entry
*TimeTrackingEntriesApi* | [**update_time_tracking_entry**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TimeTrackingEntriesApi.md#update_time_tracking_entry) | **PUT** /time_tracking_entries/{time_tracking_entry_gid} | Update a time tracking entry
*TypeaheadApi* | [**typeahead_for_workspace**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TypeaheadApi.md#typeahead_for_workspace) | **GET** /workspaces/{workspace_gid}/typeahead | Get objects via typeahead
*UserTaskListsApi* | [**get_user_task_list**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/UserTaskListsApi.md#get_user_task_list) | **GET** /user_task_lists/{user_task_list_gid} | Get a user task list
*UserTaskListsApi* | [**get_user_task_list_for_user**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/UserTaskListsApi.md#get_user_task_list_for_user) | **GET** /users/{user_gid}/user_task_list | Get a user&#x27;s task list
*UsersApi* | [**get_favorites_for_user**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/UsersApi.md#get_favorites_for_user) | **GET** /users/{user_gid}/favorites | Get a user&#x27;s favorites
*UsersApi* | [**get_user**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/UsersApi.md#get_user) | **GET** /users/{user_gid} | Get a user
*UsersApi* | [**get_users**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/UsersApi.md#get_users) | **GET** /users | Get multiple users
*UsersApi* | [**get_users_for_team**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/UsersApi.md#get_users_for_team) | **GET** /teams/{team_gid}/users | Get users in a team
*UsersApi* | [**get_users_for_workspace**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/UsersApi.md#get_users_for_workspace) | **GET** /workspaces/{workspace_gid}/users | Get users in a workspace or organization
*WebhooksApi* | [**create_webhook**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/WebhooksApi.md#create_webhook) | **POST** /webhooks | Establish a webhook
*WebhooksApi* | [**delete_webhook**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{webhook_gid} | Delete a webhook
*WebhooksApi* | [**get_webhook**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/WebhooksApi.md#get_webhook) | **GET** /webhooks/{webhook_gid} | Get a webhook
*WebhooksApi* | [**get_webhooks**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/WebhooksApi.md#get_webhooks) | **GET** /webhooks | Get multiple webhooks
*WebhooksApi* | [**update_webhook**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/WebhooksApi.md#update_webhook) | **PUT** /webhooks/{webhook_gid} | Update a webhook
*WorkspaceMembershipsApi* | [**get_workspace_membership**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/WorkspaceMembershipsApi.md#get_workspace_membership) | **GET** /workspace_memberships/{workspace_membership_gid} | Get a workspace membership
*WorkspaceMembershipsApi* | [**get_workspace_memberships_for_user**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/WorkspaceMembershipsApi.md#get_workspace_memberships_for_user) | **GET** /users/{user_gid}/workspace_memberships | Get workspace memberships for a user
*WorkspaceMembershipsApi* | [**get_workspace_memberships_for_workspace**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/WorkspaceMembershipsApi.md#get_workspace_memberships_for_workspace) | **GET** /workspaces/{workspace_gid}/workspace_memberships | Get the workspace memberships for a workspace
*WorkspacesApi* | [**add_user_for_workspace**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/WorkspacesApi.md#add_user_for_workspace) | **POST** /workspaces/{workspace_gid}/addUser | Add a user to a workspace or organization
*WorkspacesApi* | [**get_workspace**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspace_gid} | Get a workspace
*WorkspacesApi* | [**get_workspace_events**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/WorkspacesApi.md#get_workspace_events) | **GET** /workspaces/{workspace_gid}/events | Get workspace events
*WorkspacesApi* | [**get_workspaces**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/WorkspacesApi.md#get_workspaces) | **GET** /workspaces | Get multiple workspaces
*WorkspacesApi* | [**remove_user_for_workspace**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/WorkspacesApi.md#remove_user_for_workspace) | **POST** /workspaces/{workspace_gid}/removeUser | Remove a user from a workspace or organization
*WorkspacesApi* | [**update_workspace**](https://github.com/Asana/python-asana/blob/v5.2.1/docs/WorkspacesApi.md#update_workspace) | **PUT** /workspaces/{workspace_gid} | Update a workspace

## Accessing response data

### Example: Accessing task data
```python
.
.
.
try:
    task = tasks_api_instance.get_task(task_gid, opts)
    task_name = task['name']
    task_notes = task['notes']
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

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
users_api_instance = asana.UsersApi(api_client)
user_gid = 'me' # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
opts = {}

try:
    # Get a user - Add asana-enable in the request
    (api_response, status, headers) = users_api_instance.get_user(user_gid, opts, _return_http_data_only=False) # returns a tuple: (response, status, headers)
    pprint(api_response)
    pprint(status)
    pprint(headers)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

## Adding deprecation flag: "asana-enable" or "asana-disable" header

### On the client
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
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

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
users_api_instance = asana.UsersApi(api_client)
user_gid = 'me' # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
opts = {}

try:
    # Get a user - Add asana-enable in the request
    api_response = users_api_instance.get_user(user_gid, opts, header_params={'asana-enable': 'string_ids'})
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

## Async requests with multithreading

This client library uses multithreading to make async requests. To make async requests you can pass in `async_req=True` in the method call.

NOTE:
- This feature disables our auto-pagination feature
- You will want to add logic to handle the Asana API rate limits

The code belows is an example of how to make 15 async create task calls. It does not handle the Asana API rate limits.
You will have to implement your own solution for API rate limits based on your tier.

```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

tasks_api_instance = asana.TasksApi(api_client)
threads = []
for i in range(1, 15+1):
    body = {
        "data": {
            "name": f"Task: {i}",
            "projects": ["<YOUR_PROJECT_GID>"]
        }
    }
    opts = {}
    threads.append(tasks_api_instance.create_task(body, opts, async_req=True))

for thread in threads:
    try:
        pprint(thread.get())
    except ApiException as e:
        print("Exception when calling TasksApi->create_task: %s\n" % e)
```

## Pagination

The pagination feature is enabled by default. This means two things:

1: Endpoints that return a single response (EX: [get_task](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#get_task) ([Get a task](https://developers.asana.com/reference/gettask)), [get_project](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#get_project) ([Get a project](https://developers.asana.com/reference/getproject)), etc...)
will return a response with the `"data"` key abstracted from the response.

Instead of returning:
```python
{
    "data": {
        "gid": "123",
        "actual_time_minutes": null,
        "assignee": null,
        ...
        "workspace": {
            "gid": "1234567",
            "name": "user@example.com",
            "resource_type": "workspace"
        }
    }
}
```

It returns:
```python
{
    "gid": "123",
    "actual_time_minutes": null,
    "assignee": null,
    ...
    "workspace": {
        "gid": "1234567",
        "name": "user@example.com",
        "resource_type": "workspace"
    }
}
```

2: Endpoints that return an array of resources (EX: [get_tasks](https://github.com/Asana/python-asana/blob/v5.2.1/docs/TasksApi.md#get_tasks) ([Get multiple tasks](https://developers.asana.com/reference/gettasks)), [get_projects](https://github.com/Asana/python-asana/blob/v5.2.1/docs/ProjectsApi.md#get_projects) ([Get multiple projects](https://developers.asana.com/reference/getprojects)), etc...)
will return a generator object ([PageIterator.items](https://github.com/Asana/python-asana/blob/v5.2.1/asana/pagination/page_iterator.py)) that you can use to iterate through each result.

Example usage 1:
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

tasks_api_instance = asana.TasksApi(api_client)
opts = {"project": "<YOUR_PROJECT_GID>"}

try:
    tasks = tasks_api_instance.get_tasks(opts)
    for task in tasks:
        pprint(task)

except Exception as e:
    print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

Example response:
```python
{'gid': '123',
 'name': 'Task 1',
 'resource_subtype': 'default_task',
 'resource_type': 'task'},
 .
 .
 .
```

Example usage 2:
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

tasks_api_instance = asana.TasksApi(api_client)
opts = {"project": "<YOUR_PROJECT_GID>"}

try:
    tasks = tasks_api_instance.get_tasks(opts)
    pprint(list(tasks))

except Exception as e:
    print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

Example response:
```python
[{'gid': '123',
 'name': 'Task 1',
 'resource_subtype': 'default_task',
 'resource_type': 'task'},
 .
 .
 .]
```

### Ending pagination early

In the scenario where you want to end the pagination early, you can specify an `item_limit` in the method call. This will stop the iterator from going past that limit.

**Example Scenario:** You have 1000 tasks in a project and are only interested in the first 2 tasks. Instead of letting the pagination code continue to run to get all those 1000 tasks you can specify that you only want the first X results with `item_limit`.

**Without `item_limit` - The for loop will continue to run until it runs out of tasks:**

```python
    ...
    tasks = tasks_api_instance.get_tasks(opts)
    for task in tasks:
        pprint(task)
    ...
```

**Sample response:**

```python
{'gid': '123',
 'name': 'Task 1',
 'resource_subtype': 'default_task',
 'resource_type': 'task'},
 .
 .
 .
 <1000th_TASK>
```

**With `item_limit` - the for loop will stop at the `item_limit` you specified:**
```python
    ...
    tasks = tasks_api_instance.get_tasks(opts, item_limit=2)
    for task in tasks:
        pprint(task)
    ...
```

**Sample response:**

```python
{'gid': '123',
 'name': 'Task 1',
 'resource_subtype': 'default_task',
 'resource_type': 'task'},
{'gid': '456',
 'name': 'Task 2',
 'resource_subtype': 'default_task',
 'resource_type': 'task'}
```

Alternatively, if you are iterating over the generator object in a for loop, you can also just break out of the loop.

**EX:**
```python
...
opts = {'project': "<YOUR_PROJECT_GID>"}

try:
    count = 0
    tasks = tasks_api_instance.get_tasks(opts)
    for task in tasks:
        if count == 2:
            break
        pprint(task)
        count += 1
    ...
```

**Sample response:**

```python
{'gid': '123',
 'name': 'Task 1',
 'resource_subtype': 'default_task',
 'resource_type': 'task'},
 {'gid': '456',
 'name': 'Task 2',
 'resource_subtype': 'default_task',
 'resource_type': 'task'}
```

### Disabling default pagination behaviour

If you do not want to use the default pagination behaviour there are two ways to disbale it.

1: Per request - Disable pagination behavior for a single request - pass in `full_payload=True` in the method request
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

tasks_api_instance = asana.TasksApi(api_client)
opts = {"project": "<YOUR_PROJECT>", "limit": 2}

try:
    tasks = tasks_api_instance.get_tasks(opts, full_payload=True)
    pprint(tasks)
except Exception as e:
    print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

Sample response:
```python
{'data': [{'gid': '123',
           'name': 'Task 1',
           'resource_subtype': 'default_task',
           'resource_type': 'task'},
          {'gid': '456',
           'name': 'Task 2',
           'resource_subtype': 'default_task',
           'resource_type': 'task'}],
 'next_page': {'offset': 'eyJ0...',
               'path': '/tasks?project=789&limit=2&offset=eyJ0...',
               'uri': 'https://app.asana.com/api/1.0/tasks?project=789&limit=2&offset=eyJ0...'}}
```

2: Globally - Disable pagination behavior for all requests - Set `return_page_iterator` to False
```python
...
configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
configuration.return_page_iterator = False
api_client = asana.ApiClient(configuration)
...
```

## Retries

### Default configuration

By default, we retry failed requests (i.e., requests that receive any of the following response statuses: `429`, `500`, `502`, `503`, or `504`)
up to 5 times, using a backoff factor of 2, resulting in wait times of 1s, 2s, 4s, 8s, and 16s between attempts.
For `429 (Too Many Requests)` responses, the `respect_retry_after_header` option is set to `True` by default
(See [urllib3](https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html)), ensuring that retries adhere to the `Retry-After` header
from the [Asana API](https://developers.asana.com/docs/rate-limits).


NOTE: the retry strategy applies to `DELETE`, `GET`, `HEAD`, `OPTIONS`, `PUT`, `TRACE` requests (See `allowed_methods` in [urllib3](https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html))

```
self.retry_strategy = Retry(
    total=5, # Number of retries
    backoff_factor=2, # Exponential backoff factor (1s, 2s, 4s, etc.)
    status_forcelist=[429, 500, 502, 503, 504], # Retry only on these status codes
)
```

### Customize retry configuration/strategy

To customize your retry strategy, you can override the default `retry_strategy` in your configuration.
For details on configurable options for Retry, refer to the documentation: [urllib3](https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html).

#### Example - override default `retry_strategy`
```
import asana
from urllib3.util.retry import Retry

configuration = asana.Configuration()
configuration.retry_strategy = Retry(
    total=10, # Maximum number of retries
    backoff_factor=4, # Exponential backoff factor (1s, 2s, 4s, etc.)
)
...
```

## Documentation for Using the `call_api` method

Use this to make HTTP calls when the endpoint does not exist in the current library version or has bugs

### Example: GET, POST, PUT, DELETE on tasks

#### GET - get a task
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

try:
    # GET - get a task
    api_response = api_client.call_api(
        "/tasks/{task_gid}",
        "GET",
        path_params={"task_gid": "<YOUR_TASK_GID>"},
        query_params={},
        header_params={"Accept": "application/json; charset=utf-8"},
        body=None,
        post_params=[],
        files={},
        response_type=object, # You can specify one of the following types: float, bool, bytes, str, object
        auth_settings=["token"],
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

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

try:
    # GET - get multiple tasks
    api_response = api_client.call_api(
        "/tasks",
        "GET",
        path_params={},
        query_params={
            "project": "<YOUR_PROJECT_GID>",
            "opt_fields": "name,notes,projects",
        },
        header_params={"Accept": "application/json; charset=utf-8"},
        body=None,
        post_params=[],
        files={},
        response_type=object, # You can specify one of the following types: float, bool, bytes, str, object
        auth_settings=["token"],
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

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

try:
    # POST - create a task
    api_response = api_client.call_api(
        "/tasks",
        "POST",
        path_params={},
        query_params={},
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
        response_type=object, # You can specify one of the following types: float, bool, bytes, str, object
        auth_settings=["token"],
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

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

try:
    # PUT - update a task
    api_response = api_client.call_api(
        "/tasks/{task_gid}",
        "PUT",
        path_params={"task_gid": "<YOUR_TASK_GID>"},
        query_params={},
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
        response_type=object, # You can specify one of the following types: float, bool, bytes, str, object
        auth_settings=["token"],
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

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

try:
    # DELETE - delete a task
    api_response = api_client.call_api(
        "/tasks/{task_gid}",
        "DELETE",
        path_params={"task_gid": "<YOUR_TASK_GID>"},
        query_params={},
        header_params={"Accept": "application/json; charset=utf-8"},
        body=None,
        post_params=[],
        files={},
        response_type=object, # You can specify one of the following types: float, bool, bytes, str, object
        auth_settings=["token"],
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

[release-image]: https://img.shields.io/github/release/asana/python-asana.svg

[pypi-image]: https://img.shields.io/pypi/v/asana.svg?style=flat-square
[pypi-url]: https://pypi.python.org/pypi/asana/
