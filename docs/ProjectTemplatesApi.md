# asana.ProjectTemplatesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_template**](ProjectTemplatesApi.md#delete_project_template) | **DELETE** /project_templates/{project_template_gid} | Delete a project template
[**get_project_template**](ProjectTemplatesApi.md#get_project_template) | **GET** /project_templates/{project_template_gid} | Get a project template
[**get_project_templates**](ProjectTemplatesApi.md#get_project_templates) | **GET** /project_templates | Get multiple project templates
[**get_project_templates_for_team**](ProjectTemplatesApi.md#get_project_templates_for_team) | **GET** /teams/{team_gid}/project_templates | Get a team&#x27;s project templates
[**instantiate_project**](ProjectTemplatesApi.md#instantiate_project) | **POST** /project_templates/{project_template_gid}/instantiateProject | Instantiate a project from a project template

# **delete_project_template**

Delete a project template

A specific, existing project template can be deleted by making a DELETE request on the URL for that project template.  Returns an empty data record.

([more information](https://developers.asana.com/reference/deleteprojecttemplate))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_templates_api_instance = asana.ProjectTemplatesApi(api_client)
project_template_gid = "1331" # str | Globally unique identifier for the project template.


try:
    # Delete a project template
    api_response = project_templates_api_instance.delete_project_template(project_template_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplatesApi->delete_project_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_gid** | **str**| Globally unique identifier for the project template. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_project_template**

Get a project template

Returns the complete project template record for a single project template.

([more information](https://developers.asana.com/reference/getprojecttemplate))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_templates_api_instance = asana.ProjectTemplatesApi(api_client)
project_template_gid = "1331" # str | Globally unique identifier for the project template.
opts = {
    'opt_fields': "color,description,html_description,name,owner,public,requested_dates,requested_dates.description,requested_dates.name,requested_roles,requested_roles.name,team,team.name", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a project template
    api_response = project_templates_api_instance.get_project_template(project_template_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplatesApi->get_project_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_gid** | **str**| Globally unique identifier for the project template. | 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_project_templates**

Get multiple project templates

Returns the compact project template records for all project templates in the given team or workspace.

([more information](https://developers.asana.com/reference/getprojecttemplates))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_templates_api_instance = asana.ProjectTemplatesApi(api_client)
opts = {
    'workspace': "12345", # str | The workspace to filter results on.
    'team': "14916", # str | The team to filter projects on.
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "color,description,html_description,name,offset,owner,path,public,requested_dates,requested_dates.description,requested_dates.name,requested_roles,requested_roles.name,team,team.name,uri", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get multiple project templates
    api_response = project_templates_api_instance.get_project_templates(opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling ProjectTemplatesApi->get_project_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace to filter results on. | [optional] 
 **team** | **str**| The team to filter projects on. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_project_templates_for_team**

Get a team&#x27;s project templates

Returns the compact project template records for all project templates in the team.

([more information](https://developers.asana.com/reference/getprojecttemplatesforteam))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_templates_api_instance = asana.ProjectTemplatesApi(api_client)
team_gid = "159874" # str | Globally unique identifier for the team.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "color,description,html_description,name,offset,owner,path,public,requested_dates,requested_dates.description,requested_dates.name,requested_roles,requested_roles.name,team,team.name,uri", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a team's project templates
    api_response = project_templates_api_instance.get_project_templates_for_team(team_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling ProjectTemplatesApi->get_project_templates_for_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_gid** | **str**| Globally unique identifier for the team. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **instantiate_project**

Instantiate a project from a project template

Creates and returns a job that will asynchronously handle the project instantiation.  To form this request, it is recommended to first make a request to [get a project template](/reference/getprojecttemplate). Then, from the response, copy the `gid` from the object in the `requested_dates` array. This `gid` should be used in `requested_dates` to instantiate a project.  _Note: The body of this request will differ if your workspace is an organization. To determine if your workspace is an organization, use the [is_organization](/reference/workspaces) parameter._

([more information](https://developers.asana.com/reference/instantiateproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_templates_api_instance = asana.ProjectTemplatesApi(api_client)
project_template_gid = "1331" # str | Globally unique identifier for the project template.
opts = {
    'body': {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}}, # dict | Describes the inputs used for instantiating a project, such as the resulting project's name, which team it should be created in, and values for date variables.
    'opt_fields': "new_project,new_project.name,new_project_template,new_project_template.name,new_task,new_task.created_by,new_task.name,new_task.resource_subtype,resource_subtype,status", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Instantiate a project from a project template
    api_response = project_templates_api_instance.instantiate_project(project_template_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTemplatesApi->instantiate_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_gid** | **str**| Globally unique identifier for the project template. | 
 **body** | **Dict**| Describes the inputs used for instantiating a project, such as the resulting project&#x27;s name, which team it should be created in, and values for date variables. | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

