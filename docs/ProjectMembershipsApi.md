# asana.ProjectMembershipsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_project_membership**](ProjectMembershipsApi.md#get_project_membership) | **GET** /project_memberships/{project_membership_gid} | Get a project membership
[**get_project_memberships_for_project**](ProjectMembershipsApi.md#get_project_memberships_for_project) | **GET** /projects/{project_gid}/project_memberships | Get memberships from a project

# **get_project_membership**

Get a project membership

Returns the complete project record for a single project membership.

([more information](https://developers.asana.com/reference/getprojectmembership))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_memberships_api_instance = asana.ProjectMembershipsApi(api_client)
project_membership_gid = "1331" # str | 
opts = {
    'opt_fields': "access_level,member,member.name,parent,parent.name,project,project.name,user,user.name,write_access" # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a project membership
    api_response = project_memberships_api_instance.get_project_membership(project_membership_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectMembershipsApi->get_project_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_membership_gid** | **str**|  | 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_project_memberships_for_project**

Get memberships from a project

Returns the compact project membership records for the project.

([more information](https://developers.asana.com/reference/getprojectmembershipsforproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_memberships_api_instance = asana.ProjectMembershipsApi(api_client)
project_gid = "1331" # str | Globally unique identifier for the project.
opts = {
    'user': "me", # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'    'opt_fields': "access_level,member,member.name,offset,parent,parent.name,path,uri" # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get memberships from a project
    api_response = project_memberships_api_instance.get_project_memberships_for_project(project_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling ProjectMembershipsApi->get_project_memberships_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
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

