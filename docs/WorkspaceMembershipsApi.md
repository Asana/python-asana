# asana.WorkspaceMembershipsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workspace_membership**](WorkspaceMembershipsApi.md#get_workspace_membership) | **GET** /workspace_memberships/{workspace_membership_gid} | Get a workspace membership
[**get_workspace_memberships_for_user**](WorkspaceMembershipsApi.md#get_workspace_memberships_for_user) | **GET** /users/{user_gid}/workspace_memberships | Get workspace memberships for a user
[**get_workspace_memberships_for_workspace**](WorkspaceMembershipsApi.md#get_workspace_memberships_for_workspace) | **GET** /workspaces/{workspace_gid}/workspace_memberships | Get the workspace memberships for a workspace

# **get_workspace_membership**

Get a workspace membership

Returns the complete workspace record for a single workspace membership.

([more information](https://developers.asana.com/reference/getworkspacemembership))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
workspace_memberships_api_instance = asana.WorkspaceMembershipsApi(api_client)
workspace_membership_gid = "12345" # str | 
opts = {
    'opt_fields': "created_at,is_active,is_admin,is_guest,user,user.name,user_task_list,user_task_list.name,user_task_list.owner,user_task_list.workspace,vacation_dates,vacation_dates.end_on,vacation_dates.start_on,workspace,workspace.name" # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a workspace membership
    api_response = workspace_memberships_api_instance.get_workspace_membership(workspace_membership_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkspaceMembershipsApi->get_workspace_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_membership_gid** | **str**|  | 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_workspace_memberships_for_user**

Get workspace memberships for a user

Returns the compact workspace membership records for the user.

([more information](https://developers.asana.com/reference/getworkspacemembershipsforuser))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
workspace_memberships_api_instance = asana.WorkspaceMembershipsApi(api_client)
user_gid = "me" # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'    'opt_fields': "created_at,is_active,is_admin,is_guest,offset,path,uri,user,user.name,user_task_list,user_task_list.name,user_task_list.owner,user_task_list.workspace,vacation_dates,vacation_dates.end_on,vacation_dates.start_on,workspace,workspace.name" # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get workspace memberships for a user
    api_response = workspace_memberships_api_instance.get_workspace_memberships_for_user(user_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling WorkspaceMembershipsApi->get_workspace_memberships_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_gid** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_workspace_memberships_for_workspace**

Get the workspace memberships for a workspace

Returns the compact workspace membership records for the workspace.

([more information](https://developers.asana.com/reference/getworkspacemembershipsforworkspace))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
workspace_memberships_api_instance = asana.WorkspaceMembershipsApi(api_client)
workspace_gid = "12345" # str | Globally unique identifier for the workspace or organization.
opts = {
    'user': "me", # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'    'opt_fields': "created_at,is_active,is_admin,is_guest,offset,path,uri,user,user.name,user_task_list,user_task_list.name,user_task_list.owner,user_task_list.workspace,vacation_dates,vacation_dates.end_on,vacation_dates.start_on,workspace,workspace.name" # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get the workspace memberships for a workspace
    api_response = workspace_memberships_api_instance.get_workspace_memberships_for_workspace(workspace_gid, opts)
    for data in api_response:
        pprint(data)
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
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

