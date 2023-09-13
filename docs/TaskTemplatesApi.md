# asana.TaskTemplatesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task_template**](TaskTemplatesApi.md#get_task_template) | **GET** /task_templates/{task_template_gid} | Get a task template
[**get_task_templates**](TaskTemplatesApi.md#get_task_templates) | **GET** /task_templates | Get multiple task templates
[**instantiate_task**](TaskTemplatesApi.md#instantiate_task) | **POST** /task_templates/{task_template_gid}/instantiateTask | Instantiate a task from a task template

# **get_task_template**
> TaskTemplateResponseData get_task_template(task_template_gid, opt_fields=opt_fields)

Get a task template

Returns the complete task template record for a single task template.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TaskTemplatesApi(api_client)
task_template_gid = '1331' # str | Globally unique identifier for the task template.
opt_fields = ["created_at","created_by","name","project","template"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a task template
    api_response = api_instance.get_task_template(task_template_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskTemplatesApi->get_task_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_template_gid** | **str**| Globally unique identifier for the task template. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskTemplateResponseData**](TaskTemplateResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_templates**
> TaskTemplateResponseArray get_task_templates(limit=limit, offset=offset, project=project, opt_fields=opt_fields)

Get multiple task templates

Returns the compact task template records for some filtered set of task templates. You must specify a `project`

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TaskTemplatesApi(api_client)
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
project = '321654' # str | The project to filter task templates on. (optional)
opt_fields = ["created_at","created_by","name","project","template"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get multiple task templates
    api_response = api_instance.get_task_templates(limit=limit, offset=offset, project=project, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskTemplatesApi->get_task_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **project** | **str**| The project to filter task templates on. | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TaskTemplateResponseArray**](TaskTemplateResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instantiate_task**
> JobResponseData instantiate_task(task_template_gid, body=body, opt_fields=opt_fields)

Instantiate a task from a task template

Creates and returns a job that will asynchronously handle the task instantiation.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.TaskTemplatesApi(api_client)
task_template_gid = '1331' # str | Globally unique identifier for the task template.
body = asana.TaskTemplateGidInstantiateTaskBody({"param1": "value1", "param2": "value2",}) # TaskTemplateGidInstantiateTaskBody | Describes the inputs used for instantiating a task - the task's name. (optional)
opt_fields = ["new_project","new_project.name","new_project_template","new_project_template.name","new_task","new_task.created_by","new_task.name","new_task.resource_subtype","resource_subtype","status"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Instantiate a task from a task template
    api_response = api_instance.instantiate_task(task_template_gid, body=body, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskTemplatesApi->instantiate_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_template_gid** | **str**| Globally unique identifier for the task template. | 
 **body** | [**TaskTemplateGidInstantiateTaskBody**](TaskTemplateGidInstantiateTaskBody.md)| Describes the inputs used for instantiating a task - the task&#x27;s name. | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**JobResponseData**](JobResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

