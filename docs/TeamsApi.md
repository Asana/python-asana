# asana.TeamsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_for_team**](TeamsApi.md#add_user_for_team) | **POST** /teams/{team_gid}/addUser | Add a user to a team
[**create_team**](TeamsApi.md#create_team) | **POST** /teams | Create a team
[**get_team**](TeamsApi.md#get_team) | **GET** /teams/{team_gid} | Get a team
[**get_teams_for_user**](TeamsApi.md#get_teams_for_user) | **GET** /users/{user_gid}/teams | Get teams for a user
[**get_teams_for_workspace**](TeamsApi.md#get_teams_for_workspace) | **GET** /workspaces/{workspace_gid}/teams | Get teams in a workspace
[**remove_user_for_team**](TeamsApi.md#remove_user_for_team) | **POST** /teams/{team_gid}/removeUser | Remove a user from a team
[**update_team**](TeamsApi.md#update_team) | **PUT** /teams/{team_gid} | Update a team

# **add_user_for_team**

Add a user to a team

The user making this call must be a member of the team in order to add others. The user being added must exist in the same organization as the team.  Returns the complete team membership record for the newly added user.

([more information](https://developers.asana.com/reference/adduserforteam))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
teams_api_instance = asana.TeamsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The user to add to the team.
team_gid = "159874" # str | Globally unique identifier for the team.
opts = {
    'opt_fields': "is_admin,is_guest,is_limited_access,team,team.name,user,user.name", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Add a user to a team
    api_response = teams_api_instance.add_user_for_team(body, team_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->add_user_for_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The user to add to the team. | 
 **team_gid** | **str**| Globally unique identifier for the team. | 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_team**

Create a team

Creates a team within the current workspace.

([more information](https://developers.asana.com/reference/createteam))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
teams_api_instance = asana.TeamsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The team to create.
opts = {
    'opt_fields': "description,edit_team_name_or_description_access_level,edit_team_visibility_or_trash_team_access_level,guest_invite_management_access_level,html_description,join_request_management_access_level,member_invite_management_access_level,name,organization,organization.name,permalink_url,team_member_removal_access_level,visibility", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Create a team
    api_response = teams_api_instance.create_team(body, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The team to create. | 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_team**

Get a team

Returns the full record for a single team.

([more information](https://developers.asana.com/reference/getteam))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
teams_api_instance = asana.TeamsApi(api_client)
team_gid = "159874" # str | Globally unique identifier for the team.
opts = {
    'opt_fields': "description,edit_team_name_or_description_access_level,edit_team_visibility_or_trash_team_access_level,guest_invite_management_access_level,html_description,join_request_management_access_level,member_invite_management_access_level,name,organization,organization.name,permalink_url,team_member_removal_access_level,visibility", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a team
    api_response = teams_api_instance.get_team(team_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_gid** | **str**| Globally unique identifier for the team. | 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_teams_for_user**

Get teams for a user

Returns the compact records for all teams to which the given user is assigned.

([more information](https://developers.asana.com/reference/getteamsforuser))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
teams_api_instance = asana.TeamsApi(api_client)
user_gid = "me" # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
organization = "1331" # str | The workspace or organization to filter teams on.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    'opt_fields': "description,edit_team_name_or_description_access_level,edit_team_visibility_or_trash_team_access_level,guest_invite_management_access_level,html_description,join_request_management_access_level,member_invite_management_access_level,name,offset,organization,organization.name,path,permalink_url,team_member_removal_access_level,uri,visibility", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get teams for a user
    api_response = teams_api_instance.get_teams_for_user(user_gid, organization, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling TeamsApi->get_teams_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_gid** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | 
 **organization** | **str**| The workspace or organization to filter teams on. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_teams_for_workspace**

Get teams in a workspace

Returns the compact records for all teams in the workspace visible to the authorized user.

([more information](https://developers.asana.com/reference/getteamsforworkspace))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
teams_api_instance = asana.TeamsApi(api_client)
workspace_gid = "12345" # str | Globally unique identifier for the workspace or organization.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    'opt_fields': "description,edit_team_name_or_description_access_level,edit_team_visibility_or_trash_team_access_level,guest_invite_management_access_level,html_description,join_request_management_access_level,member_invite_management_access_level,name,offset,organization,organization.name,path,permalink_url,team_member_removal_access_level,uri,visibility", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get teams in a workspace
    api_response = teams_api_instance.get_teams_for_workspace(workspace_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling TeamsApi->get_teams_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **remove_user_for_team**

Remove a user from a team

The user making this call must be a member of the team in order to remove themselves or others.

([more information](https://developers.asana.com/reference/removeuserforteam))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
teams_api_instance = asana.TeamsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The user to remove from the team.
team_gid = "159874" # str | Globally unique identifier for the team.


try:
    # Remove a user from a team
    api_response = teams_api_instance.remove_user_for_team(body, team_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->remove_user_for_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The user to remove from the team. | 
 **team_gid** | **str**| Globally unique identifier for the team. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_team**

Update a team

Updates a team within the current workspace.

([more information](https://developers.asana.com/reference/updateteam))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
teams_api_instance = asana.TeamsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The team to update.
team_gid = "159874" # str | Globally unique identifier for the team.
opts = {
    'opt_fields': "description,edit_team_name_or_description_access_level,edit_team_visibility_or_trash_team_access_level,guest_invite_management_access_level,html_description,join_request_management_access_level,member_invite_management_access_level,name,organization,organization.name,permalink_url,team_member_removal_access_level,visibility", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Update a team
    api_response = teams_api_instance.update_team(body, team_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The team to update. | 
 **team_gid** | **str**| Globally unique identifier for the team. | 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

