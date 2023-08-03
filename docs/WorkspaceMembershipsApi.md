# asana.WorkspaceMembershipsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workspace_membership**](WorkspaceMembershipsApi.md#get_workspace_membership) | **GET** /workspace_memberships/{workspace_membership_gid} | Get a workspace membership
[**get_workspace_memberships_for_user**](WorkspaceMembershipsApi.md#get_workspace_memberships_for_user) | **GET** /users/{user_gid}/workspace_memberships | Get workspace memberships for a user
[**get_workspace_memberships_for_workspace**](WorkspaceMembershipsApi.md#get_workspace_memberships_for_workspace) | **GET** /workspaces/{workspace_gid}/workspace_memberships | Get the workspace memberships for a workspace

# **get_workspace_membership**
> WorkspaceMembershipResponseData get_workspace_membership(workspace_membership_gid, opt_fields=opt_fields)

Get a workspace membership

Returns the complete workspace record for a single workspace membership.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.WorkspaceMembershipsApi(asana.ApiClient(configuration))
workspace_membership_gid = '12345' # str | 
opt_fields = ["created_at","is_active","is_admin","is_guest","user","user.name","user_task_list","user_task_list.name","user_task_list.owner","user_task_list.workspace","vacation_dates","vacation_dates.end_on","vacation_dates.start_on","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get a workspace membership
  api_response = api_instance.get_workspace_membership(workspace_membership_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling WorkspaceMembershipsApi->get_workspace_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_membership_gid** | **str**|  | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**WorkspaceMembershipResponseData**](WorkspaceMembershipResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_memberships_for_user**
> WorkspaceMembershipResponseArray get_workspace_memberships_for_user(user_gid, limit=limit, offset=offset, opt_fields=opt_fields)

Get workspace memberships for a user

Returns the compact workspace membership records for the user.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.WorkspaceMembershipsApi(asana.ApiClient(configuration))
user_gid = 'me' # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["created_at","is_active","is_admin","is_guest","offset","path","uri","user","user.name","user_task_list","user_task_list.name","user_task_list.owner","user_task_list.workspace","vacation_dates","vacation_dates.end_on","vacation_dates.start_on","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get workspace memberships for a user
  api_response = api_instance.get_workspace_memberships_for_user(user_gid, limit=limit, offset=offset, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling WorkspaceMembershipsApi->get_workspace_memberships_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_gid** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**WorkspaceMembershipResponseArray**](WorkspaceMembershipResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_memberships_for_workspace**
> WorkspaceMembershipResponseArray get_workspace_memberships_for_workspace(workspace_gid, user=user, limit=limit, offset=offset, opt_fields=opt_fields)

Get the workspace memberships for a workspace

Returns the compact workspace membership records for the workspace.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.WorkspaceMembershipsApi(asana.ApiClient(configuration))
workspace_gid = '12345' # str | Globally unique identifier for the workspace or organization.
user = 'me' # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. (optional)
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["created_at","is_active","is_admin","is_guest","offset","path","uri","user","user.name","user_task_list","user_task_list.name","user_task_list.owner","user_task_list.workspace","vacation_dates","vacation_dates.end_on","vacation_dates.start_on","workspace","workspace.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get the workspace memberships for a workspace
  api_response = api_instance.get_workspace_memberships_for_workspace(workspace_gid, user=user, limit=limit, offset=offset, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling WorkspaceMembershipsApi->get_workspace_memberships_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **user** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**WorkspaceMembershipResponseArray**](WorkspaceMembershipResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

