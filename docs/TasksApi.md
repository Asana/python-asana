# asana.TasksApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dependencies_for_task**](TasksApi.md#add_dependencies_for_task) | **POST** /tasks/{task_gid}/addDependencies | Set dependencies for a task
[**add_dependents_for_task**](TasksApi.md#add_dependents_for_task) | **POST** /tasks/{task_gid}/addDependents | Set dependents for a task
[**add_followers_for_task**](TasksApi.md#add_followers_for_task) | **POST** /tasks/{task_gid}/addFollowers | Add followers to a task
[**add_project_for_task**](TasksApi.md#add_project_for_task) | **POST** /tasks/{task_gid}/addProject | Add a project to a task
[**add_tag_for_task**](TasksApi.md#add_tag_for_task) | **POST** /tasks/{task_gid}/addTag | Add a tag to a task
[**create_subtask_for_task**](TasksApi.md#create_subtask_for_task) | **POST** /tasks/{task_gid}/subtasks | Create a subtask
[**create_task**](TasksApi.md#create_task) | **POST** /tasks | Create a task
[**delete_task**](TasksApi.md#delete_task) | **DELETE** /tasks/{task_gid} | Delete a task
[**duplicate_task**](TasksApi.md#duplicate_task) | **POST** /tasks/{task_gid}/duplicate | Duplicate a task
[**get_dependencies_for_task**](TasksApi.md#get_dependencies_for_task) | **GET** /tasks/{task_gid}/dependencies | Get dependencies from a task
[**get_dependents_for_task**](TasksApi.md#get_dependents_for_task) | **GET** /tasks/{task_gid}/dependents | Get dependents from a task
[**get_subtasks_for_task**](TasksApi.md#get_subtasks_for_task) | **GET** /tasks/{task_gid}/subtasks | Get subtasks from a task
[**get_task**](TasksApi.md#get_task) | **GET** /tasks/{task_gid} | Get a task
[**get_tasks**](TasksApi.md#get_tasks) | **GET** /tasks | Get multiple tasks
[**get_tasks_for_project**](TasksApi.md#get_tasks_for_project) | **GET** /projects/{project_gid}/tasks | Get tasks from a project
[**get_tasks_for_section**](TasksApi.md#get_tasks_for_section) | **GET** /sections/{section_gid}/tasks | Get tasks from a section
[**get_tasks_for_tag**](TasksApi.md#get_tasks_for_tag) | **GET** /tags/{tag_gid}/tasks | Get tasks from a tag
[**get_tasks_for_user_task_list**](TasksApi.md#get_tasks_for_user_task_list) | **GET** /user_task_lists/{user_task_list_gid}/tasks | Get tasks from a user task list
[**remove_dependencies_for_task**](TasksApi.md#remove_dependencies_for_task) | **POST** /tasks/{task_gid}/removeDependencies | Unlink dependencies from a task
[**remove_dependents_for_task**](TasksApi.md#remove_dependents_for_task) | **POST** /tasks/{task_gid}/removeDependents | Unlink dependents from a task
[**remove_follower_for_task**](TasksApi.md#remove_follower_for_task) | **POST** /tasks/{task_gid}/removeFollowers | Remove followers from a task
[**remove_project_for_task**](TasksApi.md#remove_project_for_task) | **POST** /tasks/{task_gid}/removeProject | Remove a project from a task
[**remove_tag_for_task**](TasksApi.md#remove_tag_for_task) | **POST** /tasks/{task_gid}/removeTag | Remove a tag from a task
[**search_tasks_for_workspace**](TasksApi.md#search_tasks_for_workspace) | **GET** /workspaces/{workspace_gid}/tasks/search | Search tasks in a workspace
[**set_parent_for_task**](TasksApi.md#set_parent_for_task) | **POST** /tasks/{task_gid}/setParent | Set the parent of a task
[**update_task**](TasksApi.md#update_task) | **PUT** /tasks/{task_gid} | Update a task

# **add_dependencies_for_task**
> EmptyResponseData add_dependencies_for_task(body, task_gid)

Set dependencies for a task

Marks a set of tasks as dependencies of this task, if they are not already dependencies. *A task can have at most 30 dependents and dependencies combined*.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TaskGidAddDependenciesBody({"param1": "value1", "param2": "value2",}) # TaskGidAddDependenciesBody | The list of tasks to set as dependencies.
task_gid = '321654' # str | The task to operate on.

try:
    # Set dependencies for a task
    api_response = api_instance.add_dependencies_for_task(body, task_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->add_dependencies_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidAddDependenciesBody**](TaskGidAddDependenciesBody.md)| The list of tasks to set as dependencies. | 
 **task_gid** | **str**| The task to operate on. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dependents_for_task**
> EmptyResponseData add_dependents_for_task(body, task_gid)

Set dependents for a task

Marks a set of tasks as dependents of this task, if they are not already dependents. *A task can have at most 30 dependents and dependencies combined*.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TaskGidAddDependentsBody({"param1": "value1", "param2": "value2",}) # TaskGidAddDependentsBody | The list of tasks to add as dependents.
task_gid = '321654' # str | The task to operate on.

try:
    # Set dependents for a task
    api_response = api_instance.add_dependents_for_task(body, task_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->add_dependents_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidAddDependentsBody**](TaskGidAddDependentsBody.md)| The list of tasks to add as dependents. | 
 **task_gid** | **str**| The task to operate on. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_followers_for_task**
> TaskResponseData add_followers_for_task(body, task_gid, opt_fields=opt_fields)

Add followers to a task

Adds followers to a task. Returns an empty data block. Each task can be associated with zero or more followers in the system. Requests to add/remove followers, if successful, will return the complete updated task record, described above.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TaskGidAddFollowersBody({"param1": "value1", "param2": "value2",}) # TaskGidAddFollowersBody | The followers to add to the task.
task_gid = '321654' # str | The task to operate on.
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","parent","parent.created_by","parent.name","parent.resource_subtype","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Add followers to a task
    api_response = api_instance.add_followers_for_task(body, task_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->add_followers_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidAddFollowersBody**](TaskGidAddFollowersBody.md)| The followers to add to the task. | 
 **task_gid** | **str**| The task to operate on. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseData**](TaskResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_project_for_task**
> EmptyResponseData add_project_for_task(body, task_gid)

Add a project to a task

Adds the task to the specified project, in the optional location specified. If no location arguments are given, the task will be added to the end of the project.  `addProject` can also be used to reorder a task within a project or section that already contains it.  At most one of `insert_before`, `insert_after`, or `section` should be specified. Inserting into a section in an non-order-dependent way can be done by specifying section, otherwise, to insert within a section in a particular place, specify `insert_before` or `insert_after` and a task within the section to anchor the position of this task.  Returns an empty data block.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TaskGidAddProjectBody({"param1": "value1", "param2": "value2",}) # TaskGidAddProjectBody | The project to add the task to.
task_gid = '321654' # str | The task to operate on.

try:
    # Add a project to a task
    api_response = api_instance.add_project_for_task(body, task_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->add_project_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidAddProjectBody**](TaskGidAddProjectBody.md)| The project to add the task to. | 
 **task_gid** | **str**| The task to operate on. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_tag_for_task**
> EmptyResponseData add_tag_for_task(body, task_gid)

Add a tag to a task

Adds a tag to a task. Returns an empty data block.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TaskGidAddTagBody({"param1": "value1", "param2": "value2",}) # TaskGidAddTagBody | The tag to add to the task.
task_gid = '321654' # str | The task to operate on.

try:
    # Add a tag to a task
    api_response = api_instance.add_tag_for_task(body, task_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->add_tag_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidAddTagBody**](TaskGidAddTagBody.md)| The tag to add to the task. | 
 **task_gid** | **str**| The task to operate on. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subtask_for_task**
> TaskResponseData create_subtask_for_task(body, task_gid, opt_fields=opt_fields)

Create a subtask

Creates a new subtask and adds it to the parent task. Returns the full record for the newly created subtask.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TaskGidSubtasksBody({"param1": "value1", "param2": "value2",}) # TaskGidSubtasksBody | The new subtask to create.
task_gid = '321654' # str | The task to operate on.
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","parent","parent.created_by","parent.name","parent.resource_subtype","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Create a subtask
    api_response = api_instance.create_subtask_for_task(body, task_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->create_subtask_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidSubtasksBody**](TaskGidSubtasksBody.md)| The new subtask to create. | 
 **task_gid** | **str**| The task to operate on. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseData**](TaskResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_task**
> TaskResponseData create_task(body, opt_fields=opt_fields)

Create a task

Creating a new task is as easy as POSTing to the `/tasks` endpoint with a data block containing the fields you’d like to set on the task. Any unspecified fields will take on default values.  Every task is required to be created in a specific workspace, and this workspace cannot be changed once set. The workspace need not be set explicitly if you specify `projects` or a `parent` task instead.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TasksBody({"param1": "value1", "param2": "value2",}) # TasksBody | The task to create.
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","parent","parent.created_by","parent.name","parent.resource_subtype","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Create a task
    api_response = api_instance.create_task(body, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TasksBody**](TasksBody.md)| The task to create. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseData**](TaskResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task**
> EmptyResponseData delete_task(task_gid)

Delete a task

A specific, existing task can be deleted by making a DELETE request on the URL for that task. Deleted tasks go into the “trash” of the user making the delete request. Tasks can be recovered from the trash within a period of 30 days; afterward they are completely removed from the system.  Returns an empty data record.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
task_gid = '321654' # str | The task to operate on.

try:
    # Delete a task
    api_response = api_instance.delete_task(task_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_task**
> JobResponseData duplicate_task(body, task_gid, opt_fields=opt_fields)

Duplicate a task

Creates and returns a job that will asynchronously handle the duplication.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TaskGidDuplicateBody({"param1": "value1", "param2": "value2",}) # TaskGidDuplicateBody | Describes the duplicate's name and the fields that will be duplicated.
task_gid = '321654' # str | The task to operate on.
opt_fields = ["new_project","new_project.name","new_project_template","new_project_template.name","new_task","new_task.created_by","new_task.name","new_task.resource_subtype","resource_subtype","status"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Duplicate a task
    api_response = api_instance.duplicate_task(body, task_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->duplicate_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidDuplicateBody**](TaskGidDuplicateBody.md)| Describes the duplicate&#x27;s name and the fields that will be duplicated. | 
 **task_gid** | **str**| The task to operate on. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**JobResponseData**](JobResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dependencies_for_task**
> TaskResponseArray get_dependencies_for_task(task_gid, limit=limit, offset=offset, opt_fields=opt_fields)

Get dependencies from a task

Returns the compact representations of all of the dependencies of a task.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
task_gid = '321654' # str | The task to operate on.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","offset","parent","parent.created_by","parent.name","parent.resource_subtype","path","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","uri","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get dependencies from a task
    api_response = api_instance.get_dependencies_for_task(task_gid, limit=limit, offset=offset, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_dependencies_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseArray**](TaskResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dependents_for_task**
> TaskResponseArray get_dependents_for_task(task_gid, limit=limit, offset=offset, opt_fields=opt_fields)

Get dependents from a task

Returns the compact representations of all of the dependents of a task.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
task_gid = '321654' # str | The task to operate on.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","offset","parent","parent.created_by","parent.name","parent.resource_subtype","path","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","uri","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get dependents from a task
    api_response = api_instance.get_dependents_for_task(task_gid, limit=limit, offset=offset, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_dependents_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseArray**](TaskResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subtasks_for_task**
> TaskResponseArray get_subtasks_for_task(task_gid, limit=limit, offset=offset, opt_fields=opt_fields)

Get subtasks from a task

Returns a compact representation of all of the subtasks of a task.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
task_gid = '321654' # str | The task to operate on.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","offset","parent","parent.created_by","parent.name","parent.resource_subtype","path","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","uri","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get subtasks from a task
    api_response = api_instance.get_subtasks_for_task(task_gid, limit=limit, offset=offset, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_subtasks_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseArray**](TaskResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> TaskResponseData get_task(task_gid, opt_fields=opt_fields)

Get a task

Returns the complete task record for a single task.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
task_gid = '321654' # str | The task to operate on.
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","parent","parent.created_by","parent.name","parent.resource_subtype","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a task
    api_response = api_instance.get_task(task_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseData**](TaskResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> TaskResponseArray get_tasks(limit=limit, offset=offset, assignee=assignee, project=project, section=section, workspace=workspace, completed_since=completed_since, modified_since=modified_since, opt_fields=opt_fields)

Get multiple tasks

Returns the compact task records for some filtered set of tasks. Use one or more of the parameters provided to filter the tasks returned. You must specify a `project` or `tag` if you do not specify `assignee` and `workspace`.  For more complex task retrieval, use [workspaces/{workspace_gid}/tasks/search](/reference/searchtasksforworkspace).

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
assignee = '14641' # str | The assignee to filter tasks on. If searching for unassigned tasks, assignee.any = null can be specified. *Note: If you specify `assignee`, you must also specify the `workspace` to filter on.* (optional)
project = '321654' # str | The project to filter tasks on. (optional)
section = '321654' # str | The section to filter tasks on. (optional)
workspace = '321654' # str | The workspace to filter tasks on. *Note: If you specify `workspace`, you must also specify the `assignee` to filter on.* (optional)
completed_since = '2012-02-22T02:06:58.158Z' # datetime | Only return tasks that are either incomplete or that have been completed since this time. (optional)
modified_since = '2012-02-22T02:06:58.158Z' # datetime | Only return tasks that have been modified since the given time.  *Note: A task is considered “modified” if any of its properties change, or associations between it and other objects are modified (e.g.  a task being added to a project). A task is not considered modified just because another object it is associated with (e.g. a subtask) is modified. Actions that count as modifying the task include assigning, renaming, completing, and adding stories.* (optional)
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","offset","parent","parent.created_by","parent.name","parent.resource_subtype","path","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","uri","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get multiple tasks
    api_response = api_instance.get_tasks(limit=limit, offset=offset, assignee=assignee, project=project, section=section, workspace=workspace, completed_since=completed_since, modified_since=modified_since, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **assignee** | **str**| The assignee to filter tasks on. If searching for unassigned tasks, assignee.any &#x3D; null can be specified. *Note: If you specify &#x60;assignee&#x60;, you must also specify the &#x60;workspace&#x60; to filter on.* | [optional] 
 **project** | **str**| The project to filter tasks on. | [optional] 
 **section** | **str**| The section to filter tasks on. | [optional] 
 **workspace** | **str**| The workspace to filter tasks on. *Note: If you specify &#x60;workspace&#x60;, you must also specify the &#x60;assignee&#x60; to filter on.* | [optional] 
 **completed_since** | **datetime**| Only return tasks that are either incomplete or that have been completed since this time. | [optional] 
 **modified_since** | **datetime**| Only return tasks that have been modified since the given time.  *Note: A task is considered “modified” if any of its properties change, or associations between it and other objects are modified (e.g.  a task being added to a project). A task is not considered modified just because another object it is associated with (e.g. a subtask) is modified. Actions that count as modifying the task include assigning, renaming, completing, and adding stories.* | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseArray**](TaskResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_for_project**
> TaskResponseArray get_tasks_for_project(project_gid, completed_since=completed_since, limit=limit, offset=offset, opt_fields=opt_fields)

Get tasks from a project

Returns the compact task records for all tasks within the given project, ordered by their priority within the project. Tasks can exist in more than one project at a time.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
project_gid = '1331' # str | Globally unique identifier for the project.
completed_since = '2012-02-22T02:06:58.158Z' # str | Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  (optional)
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","offset","parent","parent.created_by","parent.name","parent.resource_subtype","path","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","uri","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get tasks from a project
    api_response = api_instance.get_tasks_for_project(project_gid, completed_since=completed_since, limit=limit, offset=offset, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **completed_since** | **str**| Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseArray**](TaskResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_for_section**
> TaskResponseArray get_tasks_for_section(section_gid, limit=limit, offset=offset, completed_since=completed_since, opt_fields=opt_fields)

Get tasks from a section

*Board view only*: Returns the compact section records for all tasks within the given section.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
section_gid = '321654' # str | The globally unique identifier for the section.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
completed_since = '2012-02-22T02:06:58.158Z' # str | Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  (optional)
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","offset","parent","parent.created_by","parent.name","parent.resource_subtype","path","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","uri","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get tasks from a section
    api_response = api_instance.get_tasks_for_section(section_gid, limit=limit, offset=offset, completed_since=completed_since, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks_for_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_gid** | **str**| The globally unique identifier for the section. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **completed_since** | **str**| Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseArray**](TaskResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_for_tag**
> TaskResponseArray get_tasks_for_tag(tag_gid, limit=limit, offset=offset, opt_fields=opt_fields)

Get tasks from a tag

Returns the compact task records for all tasks with the given tag. Tasks can have more than one tag at a time.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
tag_gid = '11235' # str | Globally unique identifier for the tag.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","offset","parent","parent.created_by","parent.name","parent.resource_subtype","path","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","uri","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get tasks from a tag
    api_response = api_instance.get_tasks_for_tag(tag_gid, limit=limit, offset=offset, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks_for_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_gid** | **str**| Globally unique identifier for the tag. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseArray**](TaskResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_for_user_task_list**
> TaskResponseArray get_tasks_for_user_task_list(user_task_list_gid, completed_since=completed_since, limit=limit, offset=offset, opt_fields=opt_fields)

Get tasks from a user task list

Returns the compact list of tasks in a user’s My Tasks list. *Note: Access control is enforced for this endpoint as with all Asana API endpoints, meaning a user’s private tasks will be filtered out if the API-authenticated user does not have access to them.* *Note: Both complete and incomplete tasks are returned by default unless they are filtered out (for example, setting `completed_since=now` will return only incomplete tasks, which is the default view for “My Tasks” in Asana.)*

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
user_task_list_gid = '12345' # str | Globally unique identifier for the user task list.
completed_since = '2012-02-22T02:06:58.158Z' # str | Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  (optional)
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","offset","parent","parent.created_by","parent.name","parent.resource_subtype","path","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","uri","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get tasks from a user task list
    api_response = api_instance.get_tasks_for_user_task_list(user_task_list_gid, completed_since=completed_since, limit=limit, offset=offset, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks_for_user_task_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_task_list_gid** | **str**| Globally unique identifier for the user task list. | 
 **completed_since** | **str**| Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*.  | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseArray**](TaskResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dependencies_for_task**
> EmptyResponseData remove_dependencies_for_task(body, task_gid)

Unlink dependencies from a task

Unlinks a set of dependencies from this task.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TaskGidRemoveDependenciesBody({"param1": "value1", "param2": "value2",}) # TaskGidRemoveDependenciesBody | The list of tasks to unlink as dependencies.
task_gid = '321654' # str | The task to operate on.

try:
    # Unlink dependencies from a task
    api_response = api_instance.remove_dependencies_for_task(body, task_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->remove_dependencies_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidRemoveDependenciesBody**](TaskGidRemoveDependenciesBody.md)| The list of tasks to unlink as dependencies. | 
 **task_gid** | **str**| The task to operate on. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_dependents_for_task**
> EmptyResponseData remove_dependents_for_task(body, task_gid)

Unlink dependents from a task

Unlinks a set of dependents from this task.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TaskGidRemoveDependentsBody({"param1": "value1", "param2": "value2",}) # TaskGidRemoveDependentsBody | The list of tasks to remove as dependents.
task_gid = '321654' # str | The task to operate on.

try:
    # Unlink dependents from a task
    api_response = api_instance.remove_dependents_for_task(body, task_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->remove_dependents_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidRemoveDependentsBody**](TaskGidRemoveDependentsBody.md)| The list of tasks to remove as dependents. | 
 **task_gid** | **str**| The task to operate on. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_follower_for_task**
> TaskResponseData remove_follower_for_task(body, task_gid, opt_fields=opt_fields)

Remove followers from a task

Removes each of the specified followers from the task if they are following. Returns the complete, updated record for the affected task.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TaskGidRemoveFollowersBody({"param1": "value1", "param2": "value2",}) # TaskGidRemoveFollowersBody | The followers to remove from the task.
task_gid = '321654' # str | The task to operate on.
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","parent","parent.created_by","parent.name","parent.resource_subtype","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Remove followers from a task
    api_response = api_instance.remove_follower_for_task(body, task_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->remove_follower_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidRemoveFollowersBody**](TaskGidRemoveFollowersBody.md)| The followers to remove from the task. | 
 **task_gid** | **str**| The task to operate on. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseData**](TaskResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_project_for_task**
> EmptyResponseData remove_project_for_task(body, task_gid)

Remove a project from a task

Removes the task from the specified project. The task will still exist in the system, but it will not be in the project anymore.  Returns an empty data block.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TaskGidRemoveProjectBody({"param1": "value1", "param2": "value2",}) # TaskGidRemoveProjectBody | The project to remove the task from.
task_gid = '321654' # str | The task to operate on.

try:
    # Remove a project from a task
    api_response = api_instance.remove_project_for_task(body, task_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->remove_project_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidRemoveProjectBody**](TaskGidRemoveProjectBody.md)| The project to remove the task from. | 
 **task_gid** | **str**| The task to operate on. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_tag_for_task**
> EmptyResponseData remove_tag_for_task(body, task_gid)

Remove a tag from a task

Removes a tag from a task. Returns an empty data block.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TaskGidRemoveTagBody({"param1": "value1", "param2": "value2",}) # TaskGidRemoveTagBody | The tag to remove from the task.
task_gid = '321654' # str | The task to operate on.

try:
    # Remove a tag from a task
    api_response = api_instance.remove_tag_for_task(body, task_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->remove_tag_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidRemoveTagBody**](TaskGidRemoveTagBody.md)| The tag to remove from the task. | 
 **task_gid** | **str**| The task to operate on. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tasks_for_workspace**
> TaskResponseArray search_tasks_for_workspace(workspace_gid, text=text, resource_subtype=resource_subtype, assignee_any=assignee_any, assignee_not=assignee_not, portfolios_any=portfolios_any, projects_any=projects_any, projects_not=projects_not, projects_all=projects_all, sections_any=sections_any, sections_not=sections_not, sections_all=sections_all, tags_any=tags_any, tags_not=tags_not, tags_all=tags_all, teams_any=teams_any, followers_not=followers_not, created_by_any=created_by_any, created_by_not=created_by_not, assigned_by_any=assigned_by_any, assigned_by_not=assigned_by_not, liked_by_not=liked_by_not, commented_on_by_not=commented_on_by_not, due_on_before=due_on_before, due_on_after=due_on_after, due_on=due_on, due_at_before=due_at_before, due_at_after=due_at_after, start_on_before=start_on_before, start_on_after=start_on_after, start_on=start_on, created_on_before=created_on_before, created_on_after=created_on_after, created_on=created_on, created_at_before=created_at_before, created_at_after=created_at_after, completed_on_before=completed_on_before, completed_on_after=completed_on_after, completed_on=completed_on, completed_at_before=completed_at_before, completed_at_after=completed_at_after, modified_on_before=modified_on_before, modified_on_after=modified_on_after, modified_on=modified_on, modified_at_before=modified_at_before, modified_at_after=modified_at_after, is_blocking=is_blocking, is_blocked=is_blocked, has_attachment=has_attachment, completed=completed, is_subtask=is_subtask, sort_by=sort_by, sort_ascending=sort_ascending, opt_fields=opt_fields)

Search tasks in a workspace

To mirror the functionality of the Asana web app's advanced search feature, the Asana API has a task search endpoint that allows you to build complex filters to find and retrieve the exact data you need. #### Premium access Like the Asana web product's advance search feature, this search endpoint will only be available to premium Asana users. A user is premium if any of the following is true:  - The workspace in which the search is being performed is a premium workspace - The user is a member of a premium team inside the workspace  Even if a user is only a member of a premium team inside a non-premium workspace, search will allow them to find data anywhere in the workspace, not just inside the premium team. Making a search request using credentials of a non-premium user will result in a `402 Payment Required` error. #### Pagination Search results are not stable; repeating the same query multiple times may return the data in a different order, even if the data do not change. Because of this, the traditional [pagination](https://developers.asana.com/docs/#pagination) available elsewhere in the Asana API is not available here. However, you can paginate manually by sorting the search results by their creation time and then modifying each subsequent query to exclude data you have already seen. Page sizes are limited to a maximum of 100 items, and can be specified by the `limit` query parameter. #### Eventual consistency Changes in Asana (regardless of whether they’re made though the web product or the API) are forwarded to our search infrastructure to be indexed. This process can take between 10 and 60 seconds to complete under normal operation, and longer during some production incidents. Making a change to a task that would alter its presence in a particular search query will not be reflected immediately. This is also true of the advanced search feature in the web product. #### Rate limits You may receive a `429 Too Many Requests` response if you hit any of our [rate limits](https://developers.asana.com/docs/#rate-limits). #### Custom field parameters | Parameter name | Custom field type | Accepted type | |---|---|---| | custom_fields.{gid}.is_set | All | Boolean | | custom_fields.{gid}.value | Text | String | | custom_fields.{gid}.value | Number | Number | | custom_fields.{gid}.value | Enum | Enum option ID | | custom_fields.{gid}.starts_with | Text only | String | | custom_fields.{gid}.ends_with | Text only | String | | custom_fields.{gid}.contains | Text only | String | | custom_fields.{gid}.less_than | Number only | Number | | custom_fields.{gid}.greater_than | Number only | Number |   For example, if the gid of the custom field is 12345, these query parameter to find tasks where it is set would be `custom_fields.12345.is_set=true`. To match an exact value for an enum custom field, use the gid of the desired enum option and not the name of the enum option: `custom_fields.12345.value=67890`.  **Not Supported**: searching for multiple exact matches of a custom field, searching for multi-enum custom field  *Note: If you specify `projects.any` and `sections.any`, you will receive tasks for the project **and** tasks for the section. If you're looking for only tasks in a section, omit the `projects.any` from the request.*

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
workspace_gid = '12345' # str | Globally unique identifier for the workspace or organization.
text = 'Bug' # str | Performs full-text search on both task name and description (optional)
resource_subtype = 'milestone' # str | Filters results by the task's resource_subtype (optional) (default to milestone)
assignee_any = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
assignee_not = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
portfolios_any = '12345,23456,34567' # str | Comma-separated list of portfolio IDs (optional)
projects_any = '12345,23456,34567' # str | Comma-separated list of project IDs (optional)
projects_not = '12345,23456,34567' # str | Comma-separated list of project IDs (optional)
projects_all = '12345,23456,34567' # str | Comma-separated list of project IDs (optional)
sections_any = '12345,23456,34567' # str | Comma-separated list of section or column IDs (optional)
sections_not = '12345,23456,34567' # str | Comma-separated list of section or column IDs (optional)
sections_all = '12345,23456,34567' # str | Comma-separated list of section or column IDs (optional)
tags_any = '12345,23456,34567' # str | Comma-separated list of tag IDs (optional)
tags_not = '12345,23456,34567' # str | Comma-separated list of tag IDs (optional)
tags_all = '12345,23456,34567' # str | Comma-separated list of tag IDs (optional)
teams_any = '12345,23456,34567' # str | Comma-separated list of team IDs (optional)
followers_not = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
created_by_any = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
created_by_not = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
assigned_by_any = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
assigned_by_not = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
liked_by_not = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
commented_on_by_not = '12345,23456,34567' # str | Comma-separated list of user identifiers (optional)
due_on_before = '2019-09-15' # date | ISO 8601 date string (optional)
due_on_after = '2019-09-15' # date | ISO 8601 date string (optional)
due_on = '2019-09-15' # date | ISO 8601 date string or `null` (optional)
due_at_before = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
due_at_after = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
start_on_before = '2019-09-15' # date | ISO 8601 date string (optional)
start_on_after = '2019-09-15' # date | ISO 8601 date string (optional)
start_on = '2019-09-15' # date | ISO 8601 date string or `null` (optional)
created_on_before = '2019-09-15' # date | ISO 8601 date string (optional)
created_on_after = '2019-09-15' # date | ISO 8601 date string (optional)
created_on = '2019-09-15' # date | ISO 8601 date string or `null` (optional)
created_at_before = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
created_at_after = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
completed_on_before = '2019-09-15' # date | ISO 8601 date string (optional)
completed_on_after = '2019-09-15' # date | ISO 8601 date string (optional)
completed_on = '2019-09-15' # date | ISO 8601 date string or `null` (optional)
completed_at_before = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
completed_at_after = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
modified_on_before = '2019-09-15' # date | ISO 8601 date string (optional)
modified_on_after = '2019-09-15' # date | ISO 8601 date string (optional)
modified_on = '2019-09-15' # date | ISO 8601 date string or `null` (optional)
modified_at_before = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
modified_at_after = '2019-04-15T01:01:46.055Z' # datetime | ISO 8601 datetime string (optional)
is_blocking = false # bool | Filter to incomplete tasks with dependents (optional)
is_blocked = false # bool | Filter to tasks with incomplete dependencies (optional)
has_attachment = false # bool | Filter to tasks with attachments (optional)
completed = false # bool | Filter to completed tasks (optional)
is_subtask = false # bool | Filter to subtasks (optional)
sort_by = 'modified_at' # str | One of `due_date`, `created_at`, `completed_at`, `likes`, or `modified_at`, defaults to `modified_at` (optional) (default to modified_at)
sort_ascending = false # bool | Default `false` (optional) (default to false)
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","parent","parent.created_by","parent.name","parent.resource_subtype","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Search tasks in a workspace
    api_response = api_instance.search_tasks_for_workspace(workspace_gid, text=text, resource_subtype=resource_subtype, assignee_any=assignee_any, assignee_not=assignee_not, portfolios_any=portfolios_any, projects_any=projects_any, projects_not=projects_not, projects_all=projects_all, sections_any=sections_any, sections_not=sections_not, sections_all=sections_all, tags_any=tags_any, tags_not=tags_not, tags_all=tags_all, teams_any=teams_any, followers_not=followers_not, created_by_any=created_by_any, created_by_not=created_by_not, assigned_by_any=assigned_by_any, assigned_by_not=assigned_by_not, liked_by_not=liked_by_not, commented_on_by_not=commented_on_by_not, due_on_before=due_on_before, due_on_after=due_on_after, due_on=due_on, due_at_before=due_at_before, due_at_after=due_at_after, start_on_before=start_on_before, start_on_after=start_on_after, start_on=start_on, created_on_before=created_on_before, created_on_after=created_on_after, created_on=created_on, created_at_before=created_at_before, created_at_after=created_at_after, completed_on_before=completed_on_before, completed_on_after=completed_on_after, completed_on=completed_on, completed_at_before=completed_at_before, completed_at_after=completed_at_after, modified_on_before=modified_on_before, modified_on_after=modified_on_after, modified_on=modified_on, modified_at_before=modified_at_before, modified_at_after=modified_at_after, is_blocking=is_blocking, is_blocked=is_blocked, has_attachment=has_attachment, completed=completed, is_subtask=is_subtask, sort_by=sort_by, sort_ascending=sort_ascending, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->search_tasks_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **text** | **str**| Performs full-text search on both task name and description | [optional] 
 **resource_subtype** | **str**| Filters results by the task&#x27;s resource_subtype | [optional] [default to milestone]
 **assignee_any** | **str**| Comma-separated list of user identifiers | [optional] 
 **assignee_not** | **str**| Comma-separated list of user identifiers | [optional] 
 **portfolios_any** | **str**| Comma-separated list of portfolio IDs | [optional] 
 **projects_any** | **str**| Comma-separated list of project IDs | [optional] 
 **projects_not** | **str**| Comma-separated list of project IDs | [optional] 
 **projects_all** | **str**| Comma-separated list of project IDs | [optional] 
 **sections_any** | **str**| Comma-separated list of section or column IDs | [optional] 
 **sections_not** | **str**| Comma-separated list of section or column IDs | [optional] 
 **sections_all** | **str**| Comma-separated list of section or column IDs | [optional] 
 **tags_any** | **str**| Comma-separated list of tag IDs | [optional] 
 **tags_not** | **str**| Comma-separated list of tag IDs | [optional] 
 **tags_all** | **str**| Comma-separated list of tag IDs | [optional] 
 **teams_any** | **str**| Comma-separated list of team IDs | [optional] 
 **followers_not** | **str**| Comma-separated list of user identifiers | [optional] 
 **created_by_any** | **str**| Comma-separated list of user identifiers | [optional] 
 **created_by_not** | **str**| Comma-separated list of user identifiers | [optional] 
 **assigned_by_any** | **str**| Comma-separated list of user identifiers | [optional] 
 **assigned_by_not** | **str**| Comma-separated list of user identifiers | [optional] 
 **liked_by_not** | **str**| Comma-separated list of user identifiers | [optional] 
 **commented_on_by_not** | **str**| Comma-separated list of user identifiers | [optional] 
 **due_on_before** | **date**| ISO 8601 date string | [optional] 
 **due_on_after** | **date**| ISO 8601 date string | [optional] 
 **due_on** | **date**| ISO 8601 date string or &#x60;null&#x60; | [optional] 
 **due_at_before** | **datetime**| ISO 8601 datetime string | [optional] 
 **due_at_after** | **datetime**| ISO 8601 datetime string | [optional] 
 **start_on_before** | **date**| ISO 8601 date string | [optional] 
 **start_on_after** | **date**| ISO 8601 date string | [optional] 
 **start_on** | **date**| ISO 8601 date string or &#x60;null&#x60; | [optional] 
 **created_on_before** | **date**| ISO 8601 date string | [optional] 
 **created_on_after** | **date**| ISO 8601 date string | [optional] 
 **created_on** | **date**| ISO 8601 date string or &#x60;null&#x60; | [optional] 
 **created_at_before** | **datetime**| ISO 8601 datetime string | [optional] 
 **created_at_after** | **datetime**| ISO 8601 datetime string | [optional] 
 **completed_on_before** | **date**| ISO 8601 date string | [optional] 
 **completed_on_after** | **date**| ISO 8601 date string | [optional] 
 **completed_on** | **date**| ISO 8601 date string or &#x60;null&#x60; | [optional] 
 **completed_at_before** | **datetime**| ISO 8601 datetime string | [optional] 
 **completed_at_after** | **datetime**| ISO 8601 datetime string | [optional] 
 **modified_on_before** | **date**| ISO 8601 date string | [optional] 
 **modified_on_after** | **date**| ISO 8601 date string | [optional] 
 **modified_on** | **date**| ISO 8601 date string or &#x60;null&#x60; | [optional] 
 **modified_at_before** | **datetime**| ISO 8601 datetime string | [optional] 
 **modified_at_after** | **datetime**| ISO 8601 datetime string | [optional] 
 **is_blocking** | **bool**| Filter to incomplete tasks with dependents | [optional] 
 **is_blocked** | **bool**| Filter to tasks with incomplete dependencies | [optional] 
 **has_attachment** | **bool**| Filter to tasks with attachments | [optional] 
 **completed** | **bool**| Filter to completed tasks | [optional] 
 **is_subtask** | **bool**| Filter to subtasks | [optional] 
 **sort_by** | **str**| One of &#x60;due_date&#x60;, &#x60;created_at&#x60;, &#x60;completed_at&#x60;, &#x60;likes&#x60;, or &#x60;modified_at&#x60;, defaults to &#x60;modified_at&#x60; | [optional] [default to modified_at]
 **sort_ascending** | **bool**| Default &#x60;false&#x60; | [optional] [default to false]
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseArray**](TaskResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_parent_for_task**
> TaskResponseData set_parent_for_task(body, task_gid, opt_fields=opt_fields)

Set the parent of a task

parent, or no parent task at all. Returns an empty data block. When using `insert_before` and `insert_after`, at most one of those two options can be specified, and they must already be subtasks of the parent.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TaskGidSetParentBody({"param1": "value1", "param2": "value2",}) # TaskGidSetParentBody | The new parent of the subtask.
task_gid = '321654' # str | The task to operate on.
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","parent","parent.created_by","parent.name","parent.resource_subtype","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Set the parent of a task
    api_response = api_instance.set_parent_for_task(body, task_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->set_parent_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidSetParentBody**](TaskGidSetParentBody.md)| The new parent of the subtask. | 
 **task_gid** | **str**| The task to operate on. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseData**](TaskResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> TaskResponseData update_task(body, task_gid, opt_fields=opt_fields)

Update a task

A specific, existing task can be updated by making a PUT request on the URL for that task. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the task.  Returns the complete updated task record.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TasksApi(api_client)
body = asana.TasksTaskGidBody({"param1": "value1", "param2": "value2",}) # TasksTaskGidBody | The task to update.
task_gid = '321654' # str | The task to operate on.
opt_fields = ["actual_time_minutes","approval_status","assignee","assignee.name","assignee_section","assignee_section.name","assignee_status","completed","completed_at","completed_by","completed_by.name","created_at","created_by","custom_fields","custom_fields.asana_created_field","custom_fields.created_by","custom_fields.created_by.name","custom_fields.currency_code","custom_fields.custom_label","custom_fields.custom_label_position","custom_fields.date_value","custom_fields.date_value.date","custom_fields.date_value.date_time","custom_fields.description","custom_fields.display_value","custom_fields.enabled","custom_fields.enum_options","custom_fields.enum_options.color","custom_fields.enum_options.enabled","custom_fields.enum_options.name","custom_fields.enum_value","custom_fields.enum_value.color","custom_fields.enum_value.enabled","custom_fields.enum_value.name","custom_fields.format","custom_fields.has_notifications_enabled","custom_fields.is_formula_field","custom_fields.is_global_to_workspace","custom_fields.is_value_read_only","custom_fields.multi_enum_values","custom_fields.multi_enum_values.color","custom_fields.multi_enum_values.enabled","custom_fields.multi_enum_values.name","custom_fields.name","custom_fields.number_value","custom_fields.people_value","custom_fields.people_value.name","custom_fields.precision","custom_fields.resource_subtype","custom_fields.text_value","custom_fields.type","dependencies","dependents","due_at","due_on","external","external.data","followers","followers.name","hearted","hearts","hearts.user","hearts.user.name","html_notes","is_rendered_as_separator","liked","likes","likes.user","likes.user.name","memberships","memberships.project","memberships.project.name","memberships.section","memberships.section.name","modified_at","name","notes","num_hearts","num_likes","num_subtasks","parent","parent.created_by","parent.name","parent.resource_subtype","permalink_url","projects","projects.name","resource_subtype","start_at","start_on","tags","tags.name","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Update a task
    api_response = api_instance.update_task(body, task_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->update_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TasksTaskGidBody**](TasksTaskGidBody.md)| The task to update. | 
 **task_gid** | **str**| The task to operate on. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskResponseData**](TaskResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

