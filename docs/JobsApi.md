# asana.JobsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job**](JobsApi.md#get_job) | **GET** /jobs/{job_gid} | Get a job by id

# **get_job**
> JobResponseData get_job(job_gid, opt_fields=opt_fields)

Get a job by id

Returns the full record for a job.

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
api_instance = asana.JobsApi(api_client)
job_gid = '12345' # str | Globally unique identifier for the job.
opt_fields = ["new_project","new_project.name","new_project_template","new_project_template.name","new_task","new_task.created_by","new_task.name","new_task.resource_subtype","resource_subtype","status"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a job by id
    api_response = api_instance.get_job(job_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_gid** | **str**| Globally unique identifier for the job. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**JobResponseData**](JobResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

