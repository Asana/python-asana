# asana.ProjectsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_field_setting_for_project**](ProjectsApi.md#add_custom_field_setting_for_project) | **POST** /projects/{project_gid}/addCustomFieldSetting | Add a custom field to a project
[**add_followers_for_project**](ProjectsApi.md#add_followers_for_project) | **POST** /projects/{project_gid}/addFollowers | Add followers to a project
[**add_members_for_project**](ProjectsApi.md#add_members_for_project) | **POST** /projects/{project_gid}/addMembers | Add users to a project
[**create_project**](ProjectsApi.md#create_project) | **POST** /projects | Create a project
[**create_project_for_team**](ProjectsApi.md#create_project_for_team) | **POST** /teams/{team_gid}/projects | Create a project in a team
[**create_project_for_workspace**](ProjectsApi.md#create_project_for_workspace) | **POST** /workspaces/{workspace_gid}/projects | Create a project in a workspace
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /projects/{project_gid} | Delete a project
[**duplicate_project**](ProjectsApi.md#duplicate_project) | **POST** /projects/{project_gid}/duplicate | Duplicate a project
[**get_project**](ProjectsApi.md#get_project) | **GET** /projects/{project_gid} | Get a project
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /projects | Get multiple projects
[**get_projects_for_task**](ProjectsApi.md#get_projects_for_task) | **GET** /tasks/{task_gid}/projects | Get projects a task is in
[**get_projects_for_team**](ProjectsApi.md#get_projects_for_team) | **GET** /teams/{team_gid}/projects | Get a team&#x27;s projects
[**get_projects_for_workspace**](ProjectsApi.md#get_projects_for_workspace) | **GET** /workspaces/{workspace_gid}/projects | Get all projects in a workspace
[**get_task_counts_for_project**](ProjectsApi.md#get_task_counts_for_project) | **GET** /projects/{project_gid}/task_counts | Get task count of a project
[**project_save_as_template**](ProjectsApi.md#project_save_as_template) | **POST** /projects/{project_gid}/saveAsTemplate | Create a project template from a project
[**remove_custom_field_setting_for_project**](ProjectsApi.md#remove_custom_field_setting_for_project) | **POST** /projects/{project_gid}/removeCustomFieldSetting | Remove a custom field from a project
[**remove_followers_for_project**](ProjectsApi.md#remove_followers_for_project) | **POST** /projects/{project_gid}/removeFollowers | Remove followers from a project
[**remove_members_for_project**](ProjectsApi.md#remove_members_for_project) | **POST** /projects/{project_gid}/removeMembers | Remove users from a project
[**search_projects_for_workspace**](ProjectsApi.md#search_projects_for_workspace) | **GET** /workspaces/{workspace_gid}/projects/search | Search projects in a workspace
[**update_project**](ProjectsApi.md#update_project) | **PUT** /projects/{project_gid} | Update a project

# **add_custom_field_setting_for_project**

Add a custom field to a project

<b>Required scope: </b><code>projects:write</code>  Custom fields are associated with projects by way of custom field settings.  This method creates a setting for the project.

([more information](https://developers.asana.com/reference/addcustomfieldsettingforproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | Information about the custom field setting.
project_gid = "1331" # str | Globally unique identifier for the project.
opts = {
    'opt_fields': "custom_field,custom_field.asana_created_field,custom_field.created_by,custom_field.created_by.name,custom_field.currency_code,custom_field.custom_label,custom_field.custom_label_position,custom_field.date_value,custom_field.date_value.date,custom_field.date_value.date_time,custom_field.default_access_level,custom_field.description,custom_field.display_value,custom_field.enabled,custom_field.enum_options,custom_field.enum_options.color,custom_field.enum_options.enabled,custom_field.enum_options.name,custom_field.enum_value,custom_field.enum_value.color,custom_field.enum_value.enabled,custom_field.enum_value.name,custom_field.format,custom_field.has_notifications_enabled,custom_field.html_text_value,custom_field.id_prefix,custom_field.input_restrictions,custom_field.is_formula_field,custom_field.is_global_to_workspace,custom_field.is_value_read_only,custom_field.multi_enum_values,custom_field.multi_enum_values.color,custom_field.multi_enum_values.enabled,custom_field.multi_enum_values.name,custom_field.name,custom_field.number_value,custom_field.people_value,custom_field.people_value.name,custom_field.precision,custom_field.privacy_setting,custom_field.reference_value,custom_field.reference_value.name,custom_field.representation_type,custom_field.resource_subtype,custom_field.text_value,custom_field.type,is_important,parent,parent.name,project,project.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Add a custom field to a project
    api_response = projects_api_instance.add_custom_field_setting_for_project(body, project_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_custom_field_setting_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| Information about the custom field setting. | 
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **add_followers_for_project**

Add followers to a project

Adds the specified list of users as followers to the project. Followers are a subset of members who have opted in to receive \"tasks added\" notifications for a project. Therefore, if the users are not already members of the project, they will also become members as a result of this operation. Returns the updated project record.

([more information](https://developers.asana.com/reference/addfollowersforproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | Information about the followers being added.
project_gid = "1331" # str | Globally unique identifier for the project.
opts = {
    'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.default_access_level,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.html_text_value,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.privacy_setting,custom_field_settings.custom_field.reference_value,custom_field_settings.custom_field.reference_value.name,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Add followers to a project
    api_response = projects_api_instance.add_followers_for_project(body, project_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_followers_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| Information about the followers being added. | 
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **add_members_for_project**

Add users to a project

Adds the specified list of users as members of the project. Note that a user being added as a member may also be added as a *follower* as a result of this operation. This is because the user's default notification settings (i.e., in the \"Notifications\" tab of \"My Profile Settings\") will override this endpoint's default behavior of setting \"Tasks added\" notifications to `false`. Returns the updated project record.

([more information](https://developers.asana.com/reference/addmembersforproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | Information about the members being added.
project_gid = "1331" # str | Globally unique identifier for the project.
opts = {
    'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.default_access_level,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.html_text_value,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.privacy_setting,custom_field_settings.custom_field.reference_value,custom_field_settings.custom_field.reference_value.name,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Add users to a project
    api_response = projects_api_instance.add_members_for_project(body, project_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_members_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| Information about the members being added. | 
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_project**

Create a project

<b>Required scope: </b><code>projects:write</code>  Create a new project in a workspace or team.  Every project is required to be created in a specific workspace or organization, and this cannot be changed once set. Note that you can use the `workspace` parameter regardless of whether or not it is an organization.  If the workspace for your project is an organization, you must also supply a `team` to share the project with.  Returns the full record of the newly created project.  **Deprecation notice:** The `team` parameter and the `private_to_team` value for `privacy_setting` are deprecated. When either is included in the request, the `Asana-Change` response header will indicate an affected deprecation. Clients should switch to using `POST /memberships` with `{ parent: project, member: team }` to share a project with a team after creation.

([more information](https://developers.asana.com/reference/createproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The project to create.
opts = {
    'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.default_access_level,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.html_text_value,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.privacy_setting,custom_field_settings.custom_field.reference_value,custom_field_settings.custom_field.reference_value.name,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Create a project
    api_response = projects_api_instance.create_project(body, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The project to create. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_project_for_team**

Create a project in a team

<b>Required scope: </b><code>projects:write</code>  Creates a project shared with the given team.  Returns the full record of the newly created project.

([more information](https://developers.asana.com/reference/createprojectforteam))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The new project to create.
team_gid = "159874" # str | Globally unique identifier for the team.
opts = {
    'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.default_access_level,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.html_text_value,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.privacy_setting,custom_field_settings.custom_field.reference_value,custom_field_settings.custom_field.reference_value.name,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Create a project in a team
    api_response = projects_api_instance.create_project_for_team(body, team_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project_for_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The new project to create. | 
 **team_gid** | **str**| Globally unique identifier for the team. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_project_for_workspace**

Create a project in a workspace

<b>Required scope: </b><code>projects:write</code>  Creates a project in the workspace.  If the workspace for your project is an organization, you must also supply a team to share the project with.  Returns the full record of the newly created project.

([more information](https://developers.asana.com/reference/createprojectforworkspace))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The new project to create.
workspace_gid = "12345" # str | Globally unique identifier for the workspace or organization.
opts = {
    'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.default_access_level,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.html_text_value,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.privacy_setting,custom_field_settings.custom_field.reference_value,custom_field_settings.custom_field.reference_value.name,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Create a project in a workspace
    api_response = projects_api_instance.create_project_for_workspace(body, workspace_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->create_project_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The new project to create. | 
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_project**

Delete a project

<b>Required scope: </b><code>projects:delete</code>  A specific, existing project can be deleted by making a DELETE request on the URL for that project.  Returns an empty data record.

([more information](https://developers.asana.com/reference/deleteproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
project_gid = "1331" # str | Globally unique identifier for the project.


try:
    # Delete a project
    api_response = projects_api_instance.delete_project(project_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **duplicate_project**

Duplicate a project

<b>Required scope: </b><code>projects:write</code>  Creates and returns a job that will asynchronously handle the duplication.

([more information](https://developers.asana.com/reference/duplicateproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
project_gid = "1331" # str | Globally unique identifier for the project.
opts = {
    'body': {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}}, # dict | Describes the duplicate's name and the elements that will be duplicated.
    'opt_fields': "new_graph_export,new_graph_export.completed_at,new_graph_export.created_at,new_graph_export.download_url,new_portfolio,new_portfolio.name,new_project,new_project.name,new_project_template,new_project_template.name,new_resource_export,new_resource_export.completed_at,new_resource_export.created_at,new_resource_export.download_url,new_task,new_task.created_by,new_task.name,new_task.resource_subtype,resource_subtype,status", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Duplicate a project
    api_response = projects_api_instance.duplicate_project(project_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->duplicate_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **body** | **Dict**| Describes the duplicate&#x27;s name and the elements that will be duplicated. | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_project**

Get a project

<b>Required scope: </b><code>projects:read</code>  Returns the complete project record for a single project.

([more information](https://developers.asana.com/reference/getproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
project_gid = "1331" # str | Globally unique identifier for the project.
opts = {
    'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.default_access_level,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.html_text_value,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.privacy_setting,custom_field_settings.custom_field.reference_value,custom_field_settings.custom_field.reference_value.name,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a project
    api_response = projects_api_instance.get_project(project_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_projects**

Get multiple projects

<b>Required scope: </b><code>projects:read</code>  Returns the compact project records for some filtered set of projects. Use one or more of the parameters provided to filter the projects returned. *Note: This endpoint may timeout for large domains. Try filtering by team!* **The `team` filter is deprecated.** Please use `GET /memberships` with `{ member: team, resource_subtype: project_membership }` to find projects shared with a team.

([more information](https://developers.asana.com/reference/getprojects))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'workspace': "1331", # str | The workspace or organization to filter projects on.
    'team': "14916", # str | **Deprecated.** The team to filter projects on. Please use `GET /memberships` with `{ member: team, resource_subtype: project_membership }` instead.
    'archived': False, # bool | Only return projects whose `archived` field takes on the value of this parameter.
    'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.default_access_level,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.html_text_value,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.privacy_setting,custom_field_settings.custom_field.reference_value,custom_field_settings.custom_field.reference_value.name,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,offset,owner,path,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,uri,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get multiple projects
    api_response = projects_api_instance.get_projects(opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **workspace** | **str**| The workspace or organization to filter projects on. | [optional] 
 **team** | **str**| **Deprecated.** The team to filter projects on. Please use &#x60;GET /memberships&#x60; with &#x60;{ member: team, resource_subtype: project_membership }&#x60; instead. | [optional] 
 **archived** | **bool**| Only return projects whose &#x60;archived&#x60; field takes on the value of this parameter. | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_projects_for_task**

Get projects a task is in

<b>Required scope: </b><code>projects:read</code>  Returns a compact representation of all of the projects the task is in.

([more information](https://developers.asana.com/reference/getprojectsfortask))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
task_gid = "321654" # str | The task to operate on.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.default_access_level,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.html_text_value,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.privacy_setting,custom_field_settings.custom_field.reference_value,custom_field_settings.custom_field.reference_value.name,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,offset,owner,path,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,uri,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get projects a task is in
    api_response = projects_api_instance.get_projects_for_task(task_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_projects_for_team**

Get a team&#x27;s projects

<b>Required scope: </b><code>projects:read</code>  Returns the compact project records for all projects in the team.

([more information](https://developers.asana.com/reference/getprojectsforteam))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
team_gid = "159874" # str | Globally unique identifier for the team.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'archived': False, # bool | Only return projects whose `archived` field takes on the value of this parameter.
    'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.default_access_level,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.html_text_value,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.privacy_setting,custom_field_settings.custom_field.reference_value,custom_field_settings.custom_field.reference_value.name,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,offset,owner,path,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,uri,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a team's projects
    api_response = projects_api_instance.get_projects_for_team(team_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects_for_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_gid** | **str**| Globally unique identifier for the team. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **archived** | **bool**| Only return projects whose &#x60;archived&#x60; field takes on the value of this parameter. | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_projects_for_workspace**

Get all projects in a workspace

<b>Required scope: </b><code>projects:read</code>  Returns the compact project records for all projects in the workspace. *Note: This endpoint may timeout for large domains. To fetch projects shared with a specific team, use `GET /memberships` with `member` set to the team GID and `resource_subtype` set to `project_membership`.*

([more information](https://developers.asana.com/reference/getprojectsforworkspace))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
workspace_gid = "12345" # str | Globally unique identifier for the workspace or organization.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'archived': False, # bool | Only return projects whose `archived` field takes on the value of this parameter.
    'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.default_access_level,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.html_text_value,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.privacy_setting,custom_field_settings.custom_field.reference_value,custom_field_settings.custom_field.reference_value.name,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,offset,owner,path,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,uri,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get all projects in a workspace
    api_response = projects_api_instance.get_projects_for_workspace(workspace_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_projects_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **archived** | **bool**| Only return projects whose &#x60;archived&#x60; field takes on the value of this parameter. | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_task_counts_for_project**

Get task count of a project

<b>Required scope: </b><code>projects:read</code>  Get an object that holds task count fields. **All fields are excluded by default**. You must [opt in](/docs/inputoutput-options) using `opt_fields` to get any information from this endpoint.  This endpoint has an additional [rate limit](/docs/rate-limits) and each field counts especially high against our [cost limits](/docs/rate-limits#cost-limits).  Milestones are just tasks, so they are included in the `num_tasks`, `num_incomplete_tasks`, and `num_completed_tasks` counts.

([more information](https://developers.asana.com/reference/gettaskcountsforproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
project_gid = "1331" # str | Globally unique identifier for the project.
opts = {
    'opt_fields': "num_completed_milestones,num_completed_tasks,num_incomplete_milestones,num_incomplete_tasks,num_milestones,num_tasks", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get task count of a project
    api_response = projects_api_instance.get_task_counts_for_project(project_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_task_counts_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **project_save_as_template**

Create a project template from a project

Creates and returns a job that will asynchronously handle the project template creation.

([more information](https://developers.asana.com/reference/projectsaveastemplate))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | Describes the inputs used for creating a project template, such as the resulting project template's name, which team it should be created in.
project_gid = "1331" # str | Globally unique identifier for the project.
opts = {
    'opt_fields': "new_graph_export,new_graph_export.completed_at,new_graph_export.created_at,new_graph_export.download_url,new_portfolio,new_portfolio.name,new_project,new_project.name,new_project_template,new_project_template.name,new_resource_export,new_resource_export.completed_at,new_resource_export.created_at,new_resource_export.download_url,new_task,new_task.created_by,new_task.name,new_task.resource_subtype,resource_subtype,status", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Create a project template from a project
    api_response = projects_api_instance.project_save_as_template(body, project_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->project_save_as_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| Describes the inputs used for creating a project template, such as the resulting project template&#x27;s name, which team it should be created in. | 
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **remove_custom_field_setting_for_project**

Remove a custom field from a project

<b>Required scope: </b><code>projects:write</code>  Removes a custom field setting from a project.

([more information](https://developers.asana.com/reference/removecustomfieldsettingforproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | Information about the custom field setting being removed.
project_gid = "1331" # str | Globally unique identifier for the project.


try:
    # Remove a custom field from a project
    api_response = projects_api_instance.remove_custom_field_setting_for_project(body, project_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->remove_custom_field_setting_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| Information about the custom field setting being removed. | 
 **project_gid** | **str**| Globally unique identifier for the project. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **remove_followers_for_project**

Remove followers from a project

Removes the specified list of users from following the project, this will not affect project membership status. Returns the updated project record.

([more information](https://developers.asana.com/reference/removefollowersforproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | Information about the followers being removed.
project_gid = "1331" # str | Globally unique identifier for the project.
opts = {
    'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.default_access_level,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.html_text_value,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.privacy_setting,custom_field_settings.custom_field.reference_value,custom_field_settings.custom_field.reference_value.name,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Remove followers from a project
    api_response = projects_api_instance.remove_followers_for_project(body, project_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->remove_followers_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| Information about the followers being removed. | 
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **remove_members_for_project**

Remove users from a project

Removes the specified list of users from members of the project. Returns the updated project record.

([more information](https://developers.asana.com/reference/removemembersforproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | Information about the members being removed.
project_gid = "1331" # str | Globally unique identifier for the project.
opts = {
    'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.default_access_level,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.html_text_value,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.privacy_setting,custom_field_settings.custom_field.reference_value,custom_field_settings.custom_field.reference_value.name,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Remove users from a project
    api_response = projects_api_instance.remove_members_for_project(body, project_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->remove_members_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| Information about the members being removed. | 
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **search_projects_for_workspace**

Search projects in a workspace

<b>Required scope: </b><code>projects:read</code>  To mirror the functionality of the Asana web app's advanced search feature, the Asana API has a project search endpoint that allows you to build complex filters to find and retrieve the exact data you need. #### Premium access Like the Asana web product's advance search feature, this search endpoint will only be available to premium Asana users. A user is premium if any of the following is true:  - The workspace in which the search is being performed is a premium workspace - The user is a member of a premium team inside the workspace  Even if a user is only a member of a premium team inside a non-premium workspace, search will allow them to find data anywhere in the workspace, not just inside the premium team. Making a search request using credentials of a non-premium user will result in a `402 Payment Required` error. #### Pagination Search results are not stable; repeating the same query multiple times may return the data in a different order, even if the data do not change. Because of this, the traditional [pagination](/docs/pagination) available elsewhere in the Asana API is not available here. However, you can paginate manually by sorting the search results by their creation time and then modifying each subsequent query to exclude data you have already seen. Page sizes are limited to a maximum of 100 items, and can be specified by the `limit` query parameter. #### Eventual consistency Changes in Asana (regardless of whether they’re made though the web product or the API) are forwarded to our search infrastructure to be indexed. This process can take between 10 and 60 seconds to complete under normal operation, and longer during some production incidents. Making a change to a project that would alter its presence in a particular search query will not be reflected immediately. This is also true of the advanced search feature in the web product. Because of this delay, the search endpoint is not suited for use cases that require immediate consistency after writes. If you need read-your-write behavior or strongly consistent results, we recommend using [Get multiple projects](/reference/getprojects) instead. #### Rate limits You may receive a `429 Too Many Requests` response if you hit any of our [rate limits](/docs/rate-limits). #### Custom field parameters | Parameter name | Custom field type | Accepted type | |---|---|---| | custom_fields.{gid}.is_set | All | Boolean | | custom_fields.{gid}.value | Text | String | | custom_fields.{gid}.value | Number | Number | | custom_fields.{gid}.value | Enum | Enum option ID | | custom_fields.{gid}.starts_with | Text only | String | | custom_fields.{gid}.ends_with | Text only | String | | custom_fields.{gid}.contains | Text only | String | | custom_fields.{gid}.less_than | Number only | Number | | custom_fields.{gid}.greater_than | Number only | Number |   For example, if the gid of the custom field is 12345, the query parameter to find projects where it is set would be `custom_fields.12345.is_set=true`. To match an exact value for an enum custom field, use the gid of the desired enum option and not the name of the enum option: `custom_fields.12345.value=67890`.  **Not Supported**: searching for multiple exact matches of a custom field, searching for multi-enum custom field

([more information](https://developers.asana.com/reference/searchprojectsforworkspace))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
workspace_gid = "12345" # str | Globally unique identifier for the workspace or organization.
opts = {
    'text': "Bugs", # str | Performs full-text search on the project name.
    'sort_by': "modified_at", # str | One of `due_date`, `created_at`, `completed_at`, `relevance`, or `modified_at`, defaults to `modified_at`.
    'sort_ascending': False, # bool | Default `false`.
    'completed': False, # bool | Filter on project completion status.
    'teams.any': "12345,67890", # str | Comma-separated list of team IDs.
    'owner.any': "12345,67890", # str | Comma-separated list of user identifiers to filter on as project owners. This can either be the string \"me\", an email, or the gid of a user.
    'members.any': "12345,67890", # str | Comma-separated list of user identifiers to filter on as members. This can either be the string \"me\", an email, or the gid of a user.
    'members.not': "12345,67890", # str | Comma-separated list of user identifiers to exclude as members. This can either be the string \"me\", an email, or the gid of a user.
    'portfolios.any': "12345,67890", # str | Comma-separated list of portfolio IDs to filter on.
    'completed_on': '2019-09-15', # date | ISO 8601 date string or `null`.
    'completed_on.before': '2019-09-15', # date | ISO 8601 date string.
    'completed_on.after': '2019-09-15', # date | ISO 8601 date string.
    'completed_at.before': '2019-04-15T01:01:46.055Z', # datetime | ISO 8601 datetime string.
    'completed_at.after': '2019-04-15T01:01:46.055Z', # datetime | ISO 8601 datetime string.
    'created_on': '2019-09-15', # date | ISO 8601 date string or `null`.
    'created_on.before': '2019-09-15', # date | ISO 8601 date string.
    'created_on.after': '2019-09-15', # date | ISO 8601 date string.
    'created_at.before': '2019-04-15T01:01:46.055Z', # datetime | ISO 8601 datetime string.
    'created_at.after': '2019-04-15T01:01:46.055Z', # datetime | ISO 8601 datetime string.
    'due_on': '2019-09-15', # date | ISO 8601 date string or `null`.
    'due_on.before': '2019-09-15', # date | ISO 8601 date string.
    'due_on.after': '2019-09-15', # date | ISO 8601 date string.
    'due_at.before': '2019-04-15T01:01:46.055Z', # datetime | ISO 8601 datetime string.
    'due_at.after': '2019-04-15T01:01:46.055Z', # datetime | ISO 8601 datetime string.
    'start_on': '2019-09-15', # date | ISO 8601 date string or `null`.
    'start_on.before': '2019-09-15', # date | ISO 8601 date string.
    'start_on.after': '2019-09-15', # date | ISO 8601 date string.
    'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.default_access_level,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.html_text_value,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.privacy_setting,custom_field_settings.custom_field.reference_value,custom_field_settings.custom_field.reference_value.name,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Search projects in a workspace
    api_response = projects_api_instance.search_projects_for_workspace(workspace_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling ProjectsApi->search_projects_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **text** | **str**| Performs full-text search on the project name. | [optional] 
 **sort_by** | **str**| One of &#x60;due_date&#x60;, &#x60;created_at&#x60;, &#x60;completed_at&#x60;, &#x60;relevance&#x60;, or &#x60;modified_at&#x60;, defaults to &#x60;modified_at&#x60;. | [optional] [default to modified_at]
 **sort_ascending** | **bool**| Default &#x60;false&#x60;. | [optional] [default to false]
 **completed** | **bool**| Filter on project completion status. | [optional] 
 **teams.any** | **str**| Comma-separated list of team IDs. | [optional] 
 **owner.any** | **str**| Comma-separated list of user identifiers to filter on as project owners. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 
 **members.any** | **str**| Comma-separated list of user identifiers to filter on as members. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 
 **members.not** | **str**| Comma-separated list of user identifiers to exclude as members. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 
 **portfolios.any** | **str**| Comma-separated list of portfolio IDs to filter on. | [optional] 
 **completed_on** | **date**| ISO 8601 date string or &#x60;null&#x60;. | [optional] 
 **completed_on.before** | **date**| ISO 8601 date string. | [optional] 
 **completed_on.after** | **date**| ISO 8601 date string. | [optional] 
 **completed_at.before** | **datetime**| ISO 8601 datetime string. | [optional] 
 **completed_at.after** | **datetime**| ISO 8601 datetime string. | [optional] 
 **created_on** | **date**| ISO 8601 date string or &#x60;null&#x60;. | [optional] 
 **created_on.before** | **date**| ISO 8601 date string. | [optional] 
 **created_on.after** | **date**| ISO 8601 date string. | [optional] 
 **created_at.before** | **datetime**| ISO 8601 datetime string. | [optional] 
 **created_at.after** | **datetime**| ISO 8601 datetime string. | [optional] 
 **due_on** | **date**| ISO 8601 date string or &#x60;null&#x60;. | [optional] 
 **due_on.before** | **date**| ISO 8601 date string. | [optional] 
 **due_on.after** | **date**| ISO 8601 date string. | [optional] 
 **due_at.before** | **datetime**| ISO 8601 datetime string. | [optional] 
 **due_at.after** | **datetime**| ISO 8601 datetime string. | [optional] 
 **start_on** | **date**| ISO 8601 date string or &#x60;null&#x60;. | [optional] 
 **start_on.before** | **date**| ISO 8601 date string. | [optional] 
 **start_on.after** | **date**| ISO 8601 date string. | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_project**

Update a project

<b>Required scope: </b><code>projects:write</code>  A specific, existing project can be updated by making a PUT request on the URL for that project. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the task.  Returns the complete updated project record.  **Deprecation notice:** Updating the `team` field is deprecated. When this field is included in the request, the `Asana-Change` response header will indicate an affected deprecation. Clients should switch to using `POST /memberships` with `{ parent: project, member: team }` to share a project with a team.

([more information](https://developers.asana.com/reference/updateproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
projects_api_instance = asana.ProjectsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The updated fields for the project.
project_gid = "1331" # str | Globally unique identifier for the project.
opts = {
    'opt_fields': "archived,color,completed,completed_at,completed_by,completed_by.name,created_at,created_from_template,created_from_template.name,current_status,current_status.author,current_status.author.name,current_status.color,current_status.created_at,current_status.created_by,current_status.created_by.name,current_status.html_text,current_status.modified_at,current_status.text,current_status.title,current_status_update,current_status_update.resource_subtype,current_status_update.title,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.asana_created_field,custom_field_settings.custom_field.created_by,custom_field_settings.custom_field.created_by.name,custom_field_settings.custom_field.currency_code,custom_field_settings.custom_field.custom_label,custom_field_settings.custom_field.custom_label_position,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.default_access_level,custom_field_settings.custom_field.description,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.format,custom_field_settings.custom_field.has_notifications_enabled,custom_field_settings.custom_field.html_text_value,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_global_to_workspace,custom_field_settings.custom_field.is_value_read_only,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.people_value,custom_field_settings.custom_field.people_value.name,custom_field_settings.custom_field.precision,custom_field_settings.custom_field.privacy_setting,custom_field_settings.custom_field.reference_value,custom_field_settings.custom_field.reference_value.name,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.resource_subtype,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,custom_field_settings.parent,custom_field_settings.parent.name,custom_field_settings.project,custom_field_settings.project.name,custom_fields,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.representation_type,custom_fields.text_value,custom_fields.type,default_access_level,default_view,due_date,due_on,followers,followers.name,html_notes,icon,members,members.name,minimum_access_level_for_customization,minimum_access_level_for_sharing,modified_at,name,notes,owner,permalink_url,privacy_setting,project_brief,public,start_on,team,team.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Update a project
    api_response = projects_api_instance.update_project(body, project_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The updated fields for the project. | 
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

