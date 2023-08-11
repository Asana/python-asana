# asana.GoalsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_followers**](GoalsApi.md#add_followers) | **POST** /goals/{goal_gid}/addFollowers | Add a collaborator to a goal
[**create_goal**](GoalsApi.md#create_goal) | **POST** /goals | Create a goal
[**create_goal_metric**](GoalsApi.md#create_goal_metric) | **POST** /goals/{goal_gid}/setMetric | Create a goal metric
[**delete_goal**](GoalsApi.md#delete_goal) | **DELETE** /goals/{goal_gid} | Delete a goal
[**get_goal**](GoalsApi.md#get_goal) | **GET** /goals/{goal_gid} | Get a goal
[**get_goals**](GoalsApi.md#get_goals) | **GET** /goals | Get goals
[**get_parent_goals_for_goal**](GoalsApi.md#get_parent_goals_for_goal) | **GET** /goals/{goal_gid}/parentGoals | Get parent goals from a goal
[**remove_followers**](GoalsApi.md#remove_followers) | **POST** /goals/{goal_gid}/removeFollowers | Remove a collaborator from a goal
[**update_goal**](GoalsApi.md#update_goal) | **PUT** /goals/{goal_gid} | Update a goal
[**update_goal_metric**](GoalsApi.md#update_goal_metric) | **POST** /goals/{goal_gid}/setMetricCurrentValue | Update a goal metric

# **add_followers**
> GoalResponseData add_followers(body, goal_gid, opt_fields=opt_fields)

Add a collaborator to a goal

Adds followers to a goal. Returns the goal the followers were added to. Each goal can be associated with zero or more followers in the system. Requests to add/remove followers, if successful, will return the complete updated goal record, described above.

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
api_instance = asana.GoalsApi(api_client)
body = asana.GoalGidAddFollowersBody({"param1": "value1", "param2": "value2",}) # GoalGidAddFollowersBody | The followers to be added as collaborators
goal_gid = '12345' # str | Globally unique identifier for the goal.
opt_fields = ["current_status_update","current_status_update.resource_subtype","current_status_update.title","due_on","followers","followers.name","html_notes","is_workspace_level","liked","likes","likes.user","likes.user.name","metric","metric.can_manage","metric.currency_code","metric.current_display_value","metric.current_number_value","metric.initial_number_value","metric.precision","metric.progress_source","metric.resource_subtype","metric.target_number_value","metric.unit","name","notes","num_likes","owner","owner.name","start_on","status","team","team.name","time_period","time_period.display_name","time_period.end_on","time_period.period","time_period.start_on","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Add a collaborator to a goal
    api_response = api_instance.add_followers(body, goal_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->add_followers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GoalGidAddFollowersBody**](GoalGidAddFollowersBody.md)| The followers to be added as collaborators | 
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GoalResponseData**](GoalResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_goal**
> GoalResponseData create_goal(body, opt_fields=opt_fields)

Create a goal

Creates a new goal in a workspace or team.  Returns the full record of the newly created goal.

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
api_instance = asana.GoalsApi(api_client)
body = asana.GoalsBody({"param1": "value1", "param2": "value2",}) # GoalsBody | The goal to create.
opt_fields = ["current_status_update","current_status_update.resource_subtype","current_status_update.title","due_on","followers","followers.name","html_notes","is_workspace_level","liked","likes","likes.user","likes.user.name","metric","metric.can_manage","metric.currency_code","metric.current_display_value","metric.current_number_value","metric.initial_number_value","metric.precision","metric.progress_source","metric.resource_subtype","metric.target_number_value","metric.unit","name","notes","num_likes","owner","owner.name","start_on","status","team","team.name","time_period","time_period.display_name","time_period.end_on","time_period.period","time_period.start_on","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Create a goal
    api_response = api_instance.create_goal(body, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->create_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GoalsBody**](GoalsBody.md)| The goal to create. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GoalResponseData**](GoalResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_goal_metric**
> GoalResponseData create_goal_metric(body, goal_gid, opt_fields=opt_fields)

Create a goal metric

Creates and adds a goal metric to a specified goal. Note that this replaces an existing goal metric if one already exists.

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
api_instance = asana.GoalsApi(api_client)
body = asana.GoalGidSetMetricBody({"param1": "value1", "param2": "value2",}) # GoalGidSetMetricBody | The goal metric to create.
goal_gid = '12345' # str | Globally unique identifier for the goal.
opt_fields = ["current_status_update","current_status_update.resource_subtype","current_status_update.title","due_on","followers","followers.name","html_notes","is_workspace_level","liked","likes","likes.user","likes.user.name","metric","metric.can_manage","metric.currency_code","metric.current_display_value","metric.current_number_value","metric.initial_number_value","metric.precision","metric.progress_source","metric.resource_subtype","metric.target_number_value","metric.unit","name","notes","num_likes","owner","owner.name","start_on","status","team","team.name","time_period","time_period.display_name","time_period.end_on","time_period.period","time_period.start_on","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Create a goal metric
    api_response = api_instance.create_goal_metric(body, goal_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->create_goal_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GoalGidSetMetricBody**](GoalGidSetMetricBody.md)| The goal metric to create. | 
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GoalResponseData**](GoalResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_goal**
> EmptyResponseData delete_goal(goal_gid)

Delete a goal

A specific, existing goal can be deleted by making a DELETE request on the URL for that goal.  Returns an empty data record.

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
api_instance = asana.GoalsApi(api_client)
goal_gid = '12345' # str | Globally unique identifier for the goal.

try:
    # Delete a goal
    api_response = api_instance.delete_goal(goal_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->delete_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goal**
> GoalResponseData get_goal(goal_gid, opt_fields=opt_fields)

Get a goal

Returns the complete goal record for a single goal.

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
api_instance = asana.GoalsApi(api_client)
goal_gid = '12345' # str | Globally unique identifier for the goal.
opt_fields = ["current_status_update","current_status_update.resource_subtype","current_status_update.title","due_on","followers","followers.name","html_notes","is_workspace_level","liked","likes","likes.user","likes.user.name","metric","metric.can_manage","metric.currency_code","metric.current_display_value","metric.current_number_value","metric.initial_number_value","metric.precision","metric.progress_source","metric.resource_subtype","metric.target_number_value","metric.unit","name","notes","num_likes","owner","owner.name","start_on","status","team","team.name","time_period","time_period.display_name","time_period.end_on","time_period.period","time_period.start_on","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a goal
    api_response = api_instance.get_goal(goal_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->get_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GoalResponseData**](GoalResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_goals**
> GoalResponseArray get_goals(portfolio=portfolio, project=project, is_workspace_level=is_workspace_level, team=team, workspace=workspace, time_periods=time_periods, limit=limit, offset=offset, opt_fields=opt_fields)

Get goals

Returns compact goal records.

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
api_instance = asana.GoalsApi(api_client)
portfolio = '159874' # str | Globally unique identifier for supporting portfolio. (optional)
project = '512241' # str | Globally unique identifier for supporting project. (optional)
is_workspace_level = false # bool | Filter to goals with is_workspace_level set to query value. Must be used with the workspace parameter. (optional)
team = '31326' # str | Globally unique identifier for the team. (optional)
workspace = '31326' # str | Globally unique identifier for the workspace. (optional)
time_periods = ['221693,506165'] # list[str] | Globally unique identifiers for the time periods. (optional)
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["current_status_update","current_status_update.resource_subtype","current_status_update.title","due_on","followers","followers.name","html_notes","is_workspace_level","liked","likes","likes.user","likes.user.name","metric","metric.can_manage","metric.currency_code","metric.current_display_value","metric.current_number_value","metric.initial_number_value","metric.precision","metric.progress_source","metric.resource_subtype","metric.target_number_value","metric.unit","name","notes","num_likes","offset","owner","owner.name","path","start_on","status","team","team.name","time_period","time_period.display_name","time_period.end_on","time_period.period","time_period.start_on","uri","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get goals
    api_response = api_instance.get_goals(portfolio=portfolio, project=project, is_workspace_level=is_workspace_level, team=team, workspace=workspace, time_periods=time_periods, limit=limit, offset=offset, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->get_goals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio** | **str**| Globally unique identifier for supporting portfolio. | [optional] 
 **project** | **str**| Globally unique identifier for supporting project. | [optional] 
 **is_workspace_level** | **bool**| Filter to goals with is_workspace_level set to query value. Must be used with the workspace parameter. | [optional] 
 **team** | **str**| Globally unique identifier for the team. | [optional] 
 **workspace** | **str**| Globally unique identifier for the workspace. | [optional] 
 **time_periods** | [**list[str]**](str.md)| Globally unique identifiers for the time periods. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GoalResponseArray**](GoalResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parent_goals_for_goal**
> GoalResponseArray get_parent_goals_for_goal(goal_gid, opt_fields=opt_fields)

Get parent goals from a goal

Returns a compact representation of all of the parent goals of a goal.

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
api_instance = asana.GoalsApi(api_client)
goal_gid = '12345' # str | Globally unique identifier for the goal.
opt_fields = ["current_status_update","current_status_update.resource_subtype","current_status_update.title","due_on","followers","followers.name","html_notes","is_workspace_level","liked","likes","likes.user","likes.user.name","metric","metric.can_manage","metric.currency_code","metric.current_display_value","metric.current_number_value","metric.initial_number_value","metric.precision","metric.progress_source","metric.resource_subtype","metric.target_number_value","metric.unit","name","notes","num_likes","owner","owner.name","start_on","status","team","team.name","time_period","time_period.display_name","time_period.end_on","time_period.period","time_period.start_on","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get parent goals from a goal
    api_response = api_instance.get_parent_goals_for_goal(goal_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->get_parent_goals_for_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GoalResponseArray**](GoalResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_followers**
> GoalResponseData remove_followers(body, goal_gid, opt_fields=opt_fields)

Remove a collaborator from a goal

Removes followers from a goal. Returns the goal the followers were removed from. Each goal can be associated with zero or more followers in the system. Requests to add/remove followers, if successful, will return the complete updated goal record, described above.

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
api_instance = asana.GoalsApi(api_client)
body = asana.GoalGidRemoveFollowersBody({"param1": "value1", "param2": "value2",}) # GoalGidRemoveFollowersBody | The followers to be removed as collaborators
goal_gid = '12345' # str | Globally unique identifier for the goal.
opt_fields = ["current_status_update","current_status_update.resource_subtype","current_status_update.title","due_on","followers","followers.name","html_notes","is_workspace_level","liked","likes","likes.user","likes.user.name","metric","metric.can_manage","metric.currency_code","metric.current_display_value","metric.current_number_value","metric.initial_number_value","metric.precision","metric.progress_source","metric.resource_subtype","metric.target_number_value","metric.unit","name","notes","num_likes","owner","owner.name","start_on","status","team","team.name","time_period","time_period.display_name","time_period.end_on","time_period.period","time_period.start_on","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Remove a collaborator from a goal
    api_response = api_instance.remove_followers(body, goal_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->remove_followers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GoalGidRemoveFollowersBody**](GoalGidRemoveFollowersBody.md)| The followers to be removed as collaborators | 
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GoalResponseData**](GoalResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_goal**
> GoalResponseData update_goal(body, goal_gid, opt_fields=opt_fields)

Update a goal

An existing goal can be updated by making a PUT request on the URL for that goal. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated goal record.

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
api_instance = asana.GoalsApi(api_client)
body = asana.GoalsGoalGidBody({"param1": "value1", "param2": "value2",}) # GoalsGoalGidBody | The updated fields for the goal.
goal_gid = '12345' # str | Globally unique identifier for the goal.
opt_fields = ["current_status_update","current_status_update.resource_subtype","current_status_update.title","due_on","followers","followers.name","html_notes","is_workspace_level","liked","likes","likes.user","likes.user.name","metric","metric.can_manage","metric.currency_code","metric.current_display_value","metric.current_number_value","metric.initial_number_value","metric.precision","metric.progress_source","metric.resource_subtype","metric.target_number_value","metric.unit","name","notes","num_likes","owner","owner.name","start_on","status","team","team.name","time_period","time_period.display_name","time_period.end_on","time_period.period","time_period.start_on","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Update a goal
    api_response = api_instance.update_goal(body, goal_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->update_goal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GoalsGoalGidBody**](GoalsGoalGidBody.md)| The updated fields for the goal. | 
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GoalResponseData**](GoalResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_goal_metric**
> GoalResponseData update_goal_metric(body, goal_gid, opt_fields=opt_fields)

Update a goal metric

Updates a goal's existing metric's `current_number_value` if one exists, otherwise responds with a 400 status code.  Returns the complete updated goal metric record.

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
api_instance = asana.GoalsApi(api_client)
body = asana.GoalGidSetMetricCurrentValueBody({"param1": "value1", "param2": "value2",}) # GoalGidSetMetricCurrentValueBody | The updated fields for the goal metric.
goal_gid = '12345' # str | Globally unique identifier for the goal.
opt_fields = ["current_status_update","current_status_update.resource_subtype","current_status_update.title","due_on","followers","followers.name","html_notes","is_workspace_level","liked","likes","likes.user","likes.user.name","metric","metric.can_manage","metric.currency_code","metric.current_display_value","metric.current_number_value","metric.initial_number_value","metric.precision","metric.progress_source","metric.resource_subtype","metric.target_number_value","metric.unit","name","notes","num_likes","owner","owner.name","start_on","status","team","team.name","time_period","time_period.display_name","time_period.end_on","time_period.period","time_period.start_on","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Update a goal metric
    api_response = api_instance.update_goal_metric(body, goal_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalsApi->update_goal_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GoalGidSetMetricCurrentValueBody**](GoalGidSetMetricCurrentValueBody.md)| The updated fields for the goal metric. | 
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**GoalResponseData**](GoalResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

