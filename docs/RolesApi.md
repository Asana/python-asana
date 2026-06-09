# asana.RolesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RolesApi.md#create_role) | **POST** /roles | Create a role
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /roles/{role_gid} | Delete a role
[**get_role**](RolesApi.md#get_role) | **GET** /roles/{role_gid} | Get a role
[**get_roles**](RolesApi.md#get_roles) | **GET** /roles | Get multiple roles
[**update_role**](RolesApi.md#update_role) | **PUT** /roles/{role_gid} | Update a role

# **create_role**

Create a role

<b>Required scope: </b><code>roles:write</code>  Creates a new RBAC role in the workspace.

([more information](https://developers.asana.com/reference/createrole))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
roles_api_instance = asana.RolesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The role to create.
opts = {
    'opt_fields': "base_role_type,creation_time,description,is_standard_role,modified_at,name,permissions,permissions.allowed_guest_invites,permissions.assign_roles,permissions.create_and_edit_ai_automations,permissions.create_and_edit_ai_teammates,permissions.create_app_authorization,permissions.create_global_custom_fields,permissions.create_pat_authorization,permissions.create_team,permissions.download_mobile_attachments,permissions.export_project_data,permissions.import_data,permissions.manage_roles,permissions.proactive_ai,permissions.share_goal_with_domain,permissions.share_portfolios_with_org,permissions.standard_ai,permissions.task_deletion_policy,permissions.upload_attachments,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Create a role
    api_response = roles_api_instance.create_role(body, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The role to create. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_role**

Delete a role

<b>Required scope: </b><code>roles:delete</code>  Deletes a role from a workspace.

([more information](https://developers.asana.com/reference/deleterole))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
roles_api_instance = asana.RolesApi(api_client)
role_gid = "12345" # str | Globally unique identifier for the role.


try:
    # Delete a role
    api_response = roles_api_instance.delete_role(role_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_gid** | **str**| Globally unique identifier for the role. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_role**

Get a role

<b>Required scope: </b><code>roles:read</code>  Returns the complete role record for a single role.

([more information](https://developers.asana.com/reference/getrole))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
roles_api_instance = asana.RolesApi(api_client)
role_gid = "12345" # str | Globally unique identifier for the role.
opts = {
    'opt_fields': "base_role_type,creation_time,description,is_standard_role,modified_at,name,permissions,permissions.allowed_guest_invites,permissions.assign_roles,permissions.create_and_edit_ai_automations,permissions.create_and_edit_ai_teammates,permissions.create_app_authorization,permissions.create_global_custom_fields,permissions.create_pat_authorization,permissions.create_team,permissions.download_mobile_attachments,permissions.export_project_data,permissions.import_data,permissions.manage_roles,permissions.proactive_ai,permissions.share_goal_with_domain,permissions.share_portfolios_with_org,permissions.standard_ai,permissions.task_deletion_policy,permissions.upload_attachments,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a role
    api_response = roles_api_instance.get_role(role_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_gid** | **str**| Globally unique identifier for the role. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_roles**

Get multiple roles

<b>Required scope: </b><code>roles:read</code>  Returns all RBAC roles for a workspace.

([more information](https://developers.asana.com/reference/getroles))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
roles_api_instance = asana.RolesApi(api_client)
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'workspace': "1331", # str | The workspace or organization to filter roles on.
    'archived': False, # bool | Only return projects whose `archived` field takes on the value of this parameter.
    'opt_fields': "base_role_type,creation_time,description,is_standard_role,modified_at,name,offset,path,permissions,permissions.allowed_guest_invites,permissions.assign_roles,permissions.create_and_edit_ai_automations,permissions.create_and_edit_ai_teammates,permissions.create_app_authorization,permissions.create_global_custom_fields,permissions.create_pat_authorization,permissions.create_team,permissions.download_mobile_attachments,permissions.export_project_data,permissions.import_data,permissions.manage_roles,permissions.proactive_ai,permissions.share_goal_with_domain,permissions.share_portfolios_with_org,permissions.standard_ai,permissions.task_deletion_policy,permissions.upload_attachments,uri,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get multiple roles
    api_response = roles_api_instance.get_roles(opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling RolesApi->get_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **workspace** | **str**| The workspace or organization to filter roles on. | [optional] 
 **archived** | **bool**| Only return projects whose &#x60;archived&#x60; field takes on the value of this parameter. | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_role**

Update a role

<b>Required scope: </b><code>roles:write</code>  Updates a role in a workspace.

([more information](https://developers.asana.com/reference/updaterole))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
roles_api_instance = asana.RolesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The updated fields for the role.
role_gid = "12345" # str | Globally unique identifier for the role.
opts = {
    'opt_fields': "base_role_type,creation_time,description,is_standard_role,modified_at,name,permissions,permissions.allowed_guest_invites,permissions.assign_roles,permissions.create_and_edit_ai_automations,permissions.create_and_edit_ai_teammates,permissions.create_app_authorization,permissions.create_global_custom_fields,permissions.create_pat_authorization,permissions.create_team,permissions.download_mobile_attachments,permissions.export_project_data,permissions.import_data,permissions.manage_roles,permissions.proactive_ai,permissions.share_goal_with_domain,permissions.share_portfolios_with_org,permissions.standard_ai,permissions.task_deletion_policy,permissions.upload_attachments,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Update a role
    api_response = roles_api_instance.update_role(body, role_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The updated fields for the role. | 
 **role_gid** | **str**| Globally unique identifier for the role. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

