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
> EmptyResponseData delete_project_template(project_template_gid)

Delete a project template

A specific, existing project template can be deleted by making a DELETE request on the URL for that project template.  Returns an empty data record.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.ProjectTemplatesApi(asana.ApiClient(configuration))
project_template_gid = '1331' # str | Globally unique identifier for the project template.

try:
  # Delete a project template
  api_response = api_instance.delete_project_template(project_template_gid)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling ProjectTemplatesApi->delete_project_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_gid** | **str**| Globally unique identifier for the project template. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_template**
> ProjectTemplateResponseData get_project_template(project_template_gid, opt_fields=opt_fields)

Get a project template

Returns the complete project template record for a single project template.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.ProjectTemplatesApi(asana.ApiClient(configuration))
project_template_gid = '1331' # str | Globally unique identifier for the project template.
opt_fields = ["color","description","html_description","name","owner","public","requested_dates","requested_dates.description","requested_dates.name","requested_roles","requested_roles.name","team","team.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get a project template
  api_response = api_instance.get_project_template(project_template_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling ProjectTemplatesApi->get_project_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_gid** | **str**| Globally unique identifier for the project template. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**ProjectTemplateResponseData**](ProjectTemplateResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_templates**
> ProjectTemplateResponseArray get_project_templates(workspace=workspace, team=team, limit=limit, offset=offset, opt_fields=opt_fields)

Get multiple project templates

Returns the compact project template records for all project templates in the given team or workspace.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.ProjectTemplatesApi(asana.ApiClient(configuration))
workspace = '12345' # str | The workspace to filter results on. (optional)
team = '14916' # str | The team to filter projects on. (optional)
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["color","description","html_description","name","offset","owner","path","public","requested_dates","requested_dates.description","requested_dates.name","requested_roles","requested_roles.name","team","team.name","uri"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get multiple project templates
  api_response = api_instance.get_project_templates(workspace=workspace, team=team, limit=limit, offset=offset, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling ProjectTemplatesApi->get_project_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace to filter results on. | [optional] 
 **team** | **str**| The team to filter projects on. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**ProjectTemplateResponseArray**](ProjectTemplateResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_templates_for_team**
> ProjectTemplateResponseArray get_project_templates_for_team(team_gid, limit=limit, offset=offset, opt_fields=opt_fields)

Get a team's project templates

Returns the compact project template records for all project templates in the team.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.ProjectTemplatesApi(asana.ApiClient(configuration))
team_gid = '159874' # str | Globally unique identifier for the team.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["color","description","html_description","name","offset","owner","path","public","requested_dates","requested_dates.description","requested_dates.name","requested_roles","requested_roles.name","team","team.name","uri"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get a team's project templates
  api_response = api_instance.get_project_templates_for_team(team_gid, limit=limit, offset=offset, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling ProjectTemplatesApi->get_project_templates_for_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_gid** | **str**| Globally unique identifier for the team. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**ProjectTemplateResponseArray**](ProjectTemplateResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instantiate_project**
> JobResponseData instantiate_project(project_template_gid, body=body, opt_fields=opt_fields)

Instantiate a project from a project template

Creates and returns a job that will asynchronously handle the project instantiation.  To form this request, it is recommended to first make a request to [get a project template](/reference/getprojecttemplate). Then, from the response, copy the `gid` from the object in the `requested_dates` array. This `gid` should be used in `requested_dates` to instantiate a project.  _Note: The body of this request will differ if your workspace is an organization. To determine if your workspace is an organization, use the [is_organization](/reference/workspaces) parameter._

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.ProjectTemplatesApi(asana.ApiClient(configuration))
project_template_gid = '1331' # str | Globally unique identifier for the project template.
body = asana.ProjectTemplateGidInstantiateProjectBody({"param1": "value1", "param2": "value2",}) # ProjectTemplateGidInstantiateProjectBody | Describes the inputs used for instantiating a project, such as the resulting project's name, which team it should be created in, and values for date variables. (optional)
opt_fields = ["new_project","new_project.name","new_project_template","new_project_template.name","new_task","new_task.name","new_task.resource_subtype","resource_subtype","status"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Instantiate a project from a project template
  api_response = api_instance.instantiate_project(project_template_gid, body=body, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling ProjectTemplatesApi->instantiate_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_template_gid** | **str**| Globally unique identifier for the project template. | 
 **body** | [**ProjectTemplateGidInstantiateProjectBody**](ProjectTemplateGidInstantiateProjectBody.md)| Describes the inputs used for instantiating a project, such as the resulting project&#x27;s name, which team it should be created in, and values for date variables. | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**JobResponseData**](JobResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

