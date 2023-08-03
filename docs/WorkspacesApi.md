# asana.WorkspacesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_for_workspace**](WorkspacesApi.md#add_user_for_workspace) | **POST** /workspaces/{workspace_gid}/addUser | Add a user to a workspace or organization
[**get_workspace**](WorkspacesApi.md#get_workspace) | **GET** /workspaces/{workspace_gid} | Get a workspace
[**get_workspaces**](WorkspacesApi.md#get_workspaces) | **GET** /workspaces | Get multiple workspaces
[**remove_user_for_workspace**](WorkspacesApi.md#remove_user_for_workspace) | **POST** /workspaces/{workspace_gid}/removeUser | Remove a user from a workspace or organization
[**update_workspace**](WorkspacesApi.md#update_workspace) | **PUT** /workspaces/{workspace_gid} | Update a workspace

# **add_user_for_workspace**
> UserBaseResponseData add_user_for_workspace(body, workspace_gid, opt_fields=opt_fields)

Add a user to a workspace or organization

Add a user to a workspace or organization. The user can be referenced by their globally unique user ID or their email address. Returns the full user record for the invited user.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.WorkspacesApi(asana.ApiClient(configuration))
body = asana.WorkspaceGidAddUserBody({"param1": "value1", "param2": "value2",}) # WorkspaceGidAddUserBody | The user to add to the workspace.
workspace_gid = '12345' # str | Globally unique identifier for the workspace or organization.
opt_fields = ["email","name","photo","photo.image_1024x1024","photo.image_128x128","photo.image_21x21","photo.image_27x27","photo.image_36x36","photo.image_60x60"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Add a user to a workspace or organization
  api_response = api_instance.add_user_for_workspace(body, workspace_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling WorkspacesApi->add_user_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkspaceGidAddUserBody**](WorkspaceGidAddUserBody.md)| The user to add to the workspace. | 
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**UserBaseResponseData**](UserBaseResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace**
> WorkspaceResponseData get_workspace(workspace_gid, opt_fields=opt_fields)

Get a workspace

Returns the full workspace record for a single workspace.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.WorkspacesApi(asana.ApiClient(configuration))
workspace_gid = '12345' # str | Globally unique identifier for the workspace or organization.
opt_fields = ["email_domains","is_organization","name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get a workspace
  api_response = api_instance.get_workspace(workspace_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling WorkspacesApi->get_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**WorkspaceResponseData**](WorkspaceResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspaces**
> WorkspaceResponseArray get_workspaces(limit=limit, offset=offset, opt_fields=opt_fields)

Get multiple workspaces

Returns the compact records for all workspaces visible to the authorized user.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.WorkspacesApi(asana.ApiClient(configuration))
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["email_domains","is_organization","name","offset","path","uri"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get multiple workspaces
  api_response = api_instance.get_workspaces(limit=limit, offset=offset, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling WorkspacesApi->get_workspaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**WorkspaceResponseArray**](WorkspaceResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_for_workspace**
> EmptyResponseData remove_user_for_workspace(body, workspace_gid)

Remove a user from a workspace or organization

Remove a user from a workspace or organization. The user making this call must be an admin in the workspace. The user can be referenced by their globally unique user ID or their email address. Returns an empty data record.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.WorkspacesApi(asana.ApiClient(configuration))
body = asana.WorkspaceGidRemoveUserBody({"param1": "value1", "param2": "value2",}) # WorkspaceGidRemoveUserBody | The user to remove from the workspace.
workspace_gid = '12345' # str | Globally unique identifier for the workspace or organization.

try:
  # Remove a user from a workspace or organization
  api_response = api_instance.remove_user_for_workspace(body, workspace_gid)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling WorkspacesApi->remove_user_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkspaceGidRemoveUserBody**](WorkspaceGidRemoveUserBody.md)| The user to remove from the workspace. | 
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_workspace**
> WorkspaceResponseData update_workspace(body, workspace_gid, opt_fields=opt_fields)

Update a workspace

A specific, existing workspace can be updated by making a PUT request on the URL for that workspace. Only the fields provided in the data block will be updated; any unspecified fields will remain unchanged. Currently the only field that can be modified for a workspace is its name. Returns the complete, updated workspace record.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.WorkspacesApi(asana.ApiClient(configuration))
body = asana.WorkspacesWorkspaceGidBody({"param1": "value1", "param2": "value2",}) # WorkspacesWorkspaceGidBody | The workspace object with all updated properties.
workspace_gid = '12345' # str | Globally unique identifier for the workspace or organization.
opt_fields = ["email_domains","is_organization","name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Update a workspace
  api_response = api_instance.update_workspace(body, workspace_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling WorkspacesApi->update_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkspacesWorkspaceGidBody**](WorkspacesWorkspaceGidBody.md)| The workspace object with all updated properties. | 
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**WorkspaceResponseData**](WorkspaceResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

