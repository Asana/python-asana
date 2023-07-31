# asana.ProjectBriefsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_brief**](ProjectBriefsApi.md#create_project_brief) | **POST** /projects/{project_gid}/project_briefs | Create a project brief
[**delete_project_brief**](ProjectBriefsApi.md#delete_project_brief) | **DELETE** /project_briefs/{project_brief_gid} | Delete a project brief
[**get_project_brief**](ProjectBriefsApi.md#get_project_brief) | **GET** /project_briefs/{project_brief_gid} | Get a project brief
[**update_project_brief**](ProjectBriefsApi.md#update_project_brief) | **PUT** /project_briefs/{project_brief_gid} | Update a project brief

# **create_project_brief**
> ProjectBriefResponseData create_project_brief(body, project_gid, opt_fields=opt_fields)

Create a project brief

Creates a new project brief.  Returns the full record of the newly created project brief.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.ProjectBriefsApi(asana.ApiClient(configuration))
body = asana.ProjectGidProjectBriefsBody({"param1": "value1", "param2": "value2",}) # ProjectGidProjectBriefsBody | The project brief to create.
project_gid = '1331' # str | Globally unique identifier for the project.
opt_fields = ["html_text","permalink_url","project","project.name","text","title"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Create a project brief
    api_response = api_instance.create_project_brief(body, project_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling ProjectBriefsApi->create_project_brief: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectGidProjectBriefsBody**](ProjectGidProjectBriefsBody.md)| The project brief to create. | 
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**ProjectBriefResponseData**](ProjectBriefResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_brief**
> EmptyResponseData delete_project_brief(project_brief_gid)

Delete a project brief

Deletes a specific, existing project brief.  Returns an empty data record.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.ProjectBriefsApi(asana.ApiClient(configuration))
project_brief_gid = '12345' # str | Globally unique identifier for the project brief.

try:
    # Delete a project brief
    api_response = api_instance.delete_project_brief(project_brief_gid)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling ProjectBriefsApi->delete_project_brief: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_brief_gid** | **str**| Globally unique identifier for the project brief. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_brief**
> ProjectBriefResponseData get_project_brief(project_brief_gid, opt_fields=opt_fields)

Get a project brief

Get the full record for a project brief.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.ProjectBriefsApi(asana.ApiClient(configuration))
project_brief_gid = '12345' # str | Globally unique identifier for the project brief.
opt_fields = ["html_text","permalink_url","project","project.name","text","title"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a project brief
    api_response = api_instance.get_project_brief(project_brief_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling ProjectBriefsApi->get_project_brief: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_brief_gid** | **str**| Globally unique identifier for the project brief. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**ProjectBriefResponseData**](ProjectBriefResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_brief**
> ProjectBriefResponseData update_project_brief(body, project_brief_gid, opt_fields=opt_fields)

Update a project brief

An existing project brief can be updated by making a PUT request on the URL for that project brief. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated project brief record.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.ProjectBriefsApi(asana.ApiClient(configuration))
body = asana.ProjectBriefsProjectBriefGidBody({"param1": "value1", "param2": "value2",}) # ProjectBriefsProjectBriefGidBody | The updated fields for the project brief.
project_brief_gid = '12345' # str | Globally unique identifier for the project brief.
opt_fields = ["html_text","permalink_url","project","project.name","text","title"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Update a project brief
    api_response = api_instance.update_project_brief(body, project_brief_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling ProjectBriefsApi->update_project_brief: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectBriefsProjectBriefGidBody**](ProjectBriefsProjectBriefGidBody.md)| The updated fields for the project brief. | 
 **project_brief_gid** | **str**| Globally unique identifier for the project brief. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**ProjectBriefResponseData**](ProjectBriefResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

