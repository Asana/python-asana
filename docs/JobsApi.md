# asana.JobsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job**](JobsApi.md#get_job) | **GET** /jobs/{job_gid} | Get a job by id

# **get_job**

Get a job by id

Returns the full record for a job.

([more information](https://developers.asana.com/reference/getjob))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
jobs_api_instance = asana.JobsApi(api_client)
job_gid = "12345" # str | Globally unique identifier for the job.
opts = {
    'opt_fields': "new_project,new_project.name,new_project_template,new_project_template.name,new_task,new_task.created_by,new_task.name,new_task.resource_subtype,resource_subtype,status" # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a job by id
    api_response = jobs_api_instance.get_job(job_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_gid** | **str**| Globally unique identifier for the job. | 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

