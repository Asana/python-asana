# asana.ProjectBriefsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_brief**](ProjectBriefsApi.md#create_project_brief) | **POST** /projects/{project_gid}/project_briefs | Create a project brief
[**delete_project_brief**](ProjectBriefsApi.md#delete_project_brief) | **DELETE** /project_briefs/{project_brief_gid} | Delete a project brief
[**get_project_brief**](ProjectBriefsApi.md#get_project_brief) | **GET** /project_briefs/{project_brief_gid} | Get a project brief
[**update_project_brief**](ProjectBriefsApi.md#update_project_brief) | **PUT** /project_briefs/{project_brief_gid} | Update a project brief

# **create_project_brief**

Create a project brief

Creates a new project brief.  Returns the full record of the newly created project brief.

([more information](https://developers.asana.com/reference/createprojectbrief))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_briefs_api_instance = asana.ProjectBriefsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The project brief to create.
project_gid = "1331" # str | Globally unique identifier for the project.
opts = {
    'opt_fields': "html_text,permalink_url,project,project.name,text,title", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Create a project brief
    api_response = project_briefs_api_instance.create_project_brief(body, project_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectBriefsApi->create_project_brief: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The project brief to create. | 
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_project_brief**

Delete a project brief

Deletes a specific, existing project brief.  Returns an empty data record.

([more information](https://developers.asana.com/reference/deleteprojectbrief))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_briefs_api_instance = asana.ProjectBriefsApi(api_client)
project_brief_gid = "12345" # str | Globally unique identifier for the project brief.


try:
    # Delete a project brief
    api_response = project_briefs_api_instance.delete_project_brief(project_brief_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectBriefsApi->delete_project_brief: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_brief_gid** | **str**| Globally unique identifier for the project brief. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_project_brief**

Get a project brief

Get the full record for a project brief.

([more information](https://developers.asana.com/reference/getprojectbrief))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_briefs_api_instance = asana.ProjectBriefsApi(api_client)
project_brief_gid = "12345" # str | Globally unique identifier for the project brief.
opts = {
    'opt_fields': "html_text,permalink_url,project,project.name,text,title", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a project brief
    api_response = project_briefs_api_instance.get_project_brief(project_brief_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectBriefsApi->get_project_brief: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_brief_gid** | **str**| Globally unique identifier for the project brief. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_project_brief**

Update a project brief

An existing project brief can be updated by making a PUT request on the URL for that project brief. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated project brief record.

([more information](https://developers.asana.com/reference/updateprojectbrief))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_briefs_api_instance = asana.ProjectBriefsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The updated fields for the project brief.
project_brief_gid = "12345" # str | Globally unique identifier for the project brief.
opts = {
    'opt_fields': "html_text,permalink_url,project,project.name,text,title", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Update a project brief
    api_response = project_briefs_api_instance.update_project_brief(body, project_brief_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectBriefsApi->update_project_brief: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The updated fields for the project brief. | 
 **project_brief_gid** | **str**| Globally unique identifier for the project brief. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

