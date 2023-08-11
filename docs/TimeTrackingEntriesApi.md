# asana.TimeTrackingEntriesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_time_tracking_entry**](TimeTrackingEntriesApi.md#create_time_tracking_entry) | **POST** /tasks/{task_gid}/time_tracking_entries | Create a time tracking entry
[**delete_time_tracking_entry**](TimeTrackingEntriesApi.md#delete_time_tracking_entry) | **DELETE** /time_tracking_entries/{time_tracking_entry_gid} | Delete a time tracking entry
[**get_time_tracking_entries_for_task**](TimeTrackingEntriesApi.md#get_time_tracking_entries_for_task) | **GET** /tasks/{task_gid}/time_tracking_entries | Get time tracking entries for a task
[**get_time_tracking_entry**](TimeTrackingEntriesApi.md#get_time_tracking_entry) | **GET** /time_tracking_entries/{time_tracking_entry_gid} | Get a time tracking entry
[**update_time_tracking_entry**](TimeTrackingEntriesApi.md#update_time_tracking_entry) | **PUT** /time_tracking_entries/{time_tracking_entry_gid} | Update a time tracking entry

# **create_time_tracking_entry**
> TimeTrackingEntryBaseData create_time_tracking_entry(body, task_gid, opt_fields=opt_fields)

Create a time tracking entry

Creates a time tracking entry on a given task.  Returns the record of the newly created time tracking entry.

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
api_instance = asana.TimeTrackingEntriesApi(api_client)
body = asana.TaskGidTimeTrackingEntriesBody({"param1": "value1", "param2": "value2",}) # TaskGidTimeTrackingEntriesBody | Information about the time tracking entry.
task_gid = '321654' # str | The task to operate on.
opt_fields = ["created_at","created_by","created_by.name","duration_minutes","entered_on","task","task.created_by","task.name","task.resource_subtype"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Create a time tracking entry
    api_response = api_instance.create_time_tracking_entry(body, task_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingEntriesApi->create_time_tracking_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidTimeTrackingEntriesBody**](TaskGidTimeTrackingEntriesBody.md)| Information about the time tracking entry. | 
 **task_gid** | **str**| The task to operate on. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TimeTrackingEntryBaseData**](TimeTrackingEntryBaseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_time_tracking_entry**
> EmptyResponseData delete_time_tracking_entry(time_tracking_entry_gid)

Delete a time tracking entry

A specific, existing time tracking entry can be deleted by making a `DELETE` request on the URL for that time tracking entry.  Returns an empty data record.

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
api_instance = asana.TimeTrackingEntriesApi(api_client)
time_tracking_entry_gid = '917392' # str | Globally unique identifier for the time tracking entry.

try:
    # Delete a time tracking entry
    api_response = api_instance.delete_time_tracking_entry(time_tracking_entry_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingEntriesApi->delete_time_tracking_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_entry_gid** | **str**| Globally unique identifier for the time tracking entry. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_tracking_entries_for_task**
> TimeTrackingEntryCompactArray get_time_tracking_entries_for_task(task_gid, limit=limit, offset=offset, opt_fields=opt_fields)

Get time tracking entries for a task

Returns time tracking entries for a given task.

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
api_instance = asana.TimeTrackingEntriesApi(api_client)
task_gid = '321654' # str | The task to operate on.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["created_by","created_by.name","duration_minutes","entered_on","offset","path","uri"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get time tracking entries for a task
    api_response = api_instance.get_time_tracking_entries_for_task(task_gid, limit=limit, offset=offset, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingEntriesApi->get_time_tracking_entries_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TimeTrackingEntryCompactArray**](TimeTrackingEntryCompactArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_tracking_entry**
> TimeTrackingEntryBaseData get_time_tracking_entry(time_tracking_entry_gid, opt_fields=opt_fields)

Get a time tracking entry

Returns the complete time tracking entry record for a single time tracking entry.

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
api_instance = asana.TimeTrackingEntriesApi(api_client)
time_tracking_entry_gid = '917392' # str | Globally unique identifier for the time tracking entry.
opt_fields = ["created_at","created_by","created_by.name","duration_minutes","entered_on","task","task.created_by","task.name","task.resource_subtype"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a time tracking entry
    api_response = api_instance.get_time_tracking_entry(time_tracking_entry_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingEntriesApi->get_time_tracking_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_entry_gid** | **str**| Globally unique identifier for the time tracking entry. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TimeTrackingEntryBaseData**](TimeTrackingEntryBaseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_time_tracking_entry**
> TimeTrackingEntryBaseData update_time_tracking_entry(body, time_tracking_entry_gid, opt_fields=opt_fields)

Update a time tracking entry

A specific, existing time tracking entry can be updated by making a `PUT` request on the URL for that time tracking entry. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the task.  Returns the complete updated time tracking entry record.

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
api_instance = asana.TimeTrackingEntriesApi(api_client)
body = asana.TimeTrackingEntriesTimeTrackingEntryGidBody({"param1": "value1", "param2": "value2",}) # TimeTrackingEntriesTimeTrackingEntryGidBody | The updated fields for the time tracking entry.
time_tracking_entry_gid = '917392' # str | Globally unique identifier for the time tracking entry.
opt_fields = ["created_at","created_by","created_by.name","duration_minutes","entered_on","task","task.created_by","task.name","task.resource_subtype"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Update a time tracking entry
    api_response = api_instance.update_time_tracking_entry(body, time_tracking_entry_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingEntriesApi->update_time_tracking_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TimeTrackingEntriesTimeTrackingEntryGidBody**](TimeTrackingEntriesTimeTrackingEntryGidBody.md)| The updated fields for the time tracking entry. | 
 **time_tracking_entry_gid** | **str**| Globally unique identifier for the time tracking entry. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TimeTrackingEntryBaseData**](TimeTrackingEntryBaseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

