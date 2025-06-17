# asana.TaskTemplatesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_task_template**](TaskTemplatesApi.md#delete_task_template) | **DELETE** /task_templates/{task_template_gid} | Delete a task template
[**get_task_template**](TaskTemplatesApi.md#get_task_template) | **GET** /task_templates/{task_template_gid} | Get a task template
[**get_task_templates**](TaskTemplatesApi.md#get_task_templates) | **GET** /task_templates | Get multiple task templates
[**instantiate_task**](TaskTemplatesApi.md#instantiate_task) | **POST** /task_templates/{task_template_gid}/instantiateTask | Instantiate a task from a task template

# **delete_task_template**

Delete a task template

A specific, existing task template can be deleted by making a DELETE request on the URL for that task template. Returns an empty data record.

([more information](https://developers.asana.com/reference/deletetasktemplate))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
task_templates_api_instance = asana.TaskTemplatesApi(api_client)
task_template_gid = "1331" # str | Globally unique identifier for the task template.


try:
    # Delete a task template
    api_response = task_templates_api_instance.delete_task_template(task_template_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskTemplatesApi->delete_task_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_template_gid** | **str**| Globally unique identifier for the task template. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_task_template**

Get a task template

<b>Required scope: </b><code>task_templates:read</code>  Returns the complete task template record for a single task template.

([more information](https://developers.asana.com/reference/gettasktemplate))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
task_templates_api_instance = asana.TaskTemplatesApi(api_client)
task_template_gid = "1331" # str | Globally unique identifier for the task template.
opts = {
    'opt_fields': "created_at,created_by,name,project,template", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a task template
    api_response = task_templates_api_instance.get_task_template(task_template_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskTemplatesApi->get_task_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_template_gid** | **str**| Globally unique identifier for the task template. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_task_templates**

Get multiple task templates

<b>Required scope: </b><code>task_templates:read</code>  Returns the compact task template records for some filtered set of task templates. You must specify a `project`

([more information](https://developers.asana.com/reference/gettasktemplates))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
task_templates_api_instance = asana.TaskTemplatesApi(api_client)
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'project': "321654", # str | The project to filter task templates on.
    'opt_fields': "created_at,created_by,name,project,template", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get multiple task templates
    api_response = task_templates_api_instance.get_task_templates(opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling TaskTemplatesApi->get_task_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **project** | **str**| The project to filter task templates on. | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **instantiate_task**

Instantiate a task from a task template

Creates and returns a job that will asynchronously handle the task instantiation.

([more information](https://developers.asana.com/reference/instantiatetask))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
task_templates_api_instance = asana.TaskTemplatesApi(api_client)
task_template_gid = "1331" # str | Globally unique identifier for the task template.
opts = {
    'body': {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}}, # dict | Describes the inputs used for instantiating a task - the task's name.
    'opt_fields': "new_graph_export,new_graph_export.completed_at,new_graph_export.created_at,new_graph_export.download_url,new_project,new_project.name,new_project_template,new_project_template.name,new_task,new_task.created_by,new_task.name,new_task.resource_subtype,resource_subtype,status", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Instantiate a task from a task template
    api_response = task_templates_api_instance.instantiate_task(task_template_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaskTemplatesApi->instantiate_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_template_gid** | **str**| Globally unique identifier for the task template. | 
 **body** | **Dict**| Describes the inputs used for instantiating a task - the task&#x27;s name. | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

