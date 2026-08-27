# asana.TimeTrackingEntriesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_time_tracking_entry**](TimeTrackingEntriesApi.md#create_time_tracking_entry) | **POST** /tasks/{task_gid}/time_tracking_entries | Create a time tracking entry
[**delete_time_tracking_entry**](TimeTrackingEntriesApi.md#delete_time_tracking_entry) | **DELETE** /time_tracking_entries/{time_tracking_entry_gid} | Delete a time tracking entry
[**get_time_tracking_entries**](TimeTrackingEntriesApi.md#get_time_tracking_entries) | **GET** /time_tracking_entries | Get multiple time tracking entries
[**get_time_tracking_entries_for_task**](TimeTrackingEntriesApi.md#get_time_tracking_entries_for_task) | **GET** /tasks/{task_gid}/time_tracking_entries | Get time tracking entries for a task
[**get_time_tracking_entry**](TimeTrackingEntriesApi.md#get_time_tracking_entry) | **GET** /time_tracking_entries/{time_tracking_entry_gid} | Get a time tracking entry
[**update_time_tracking_entry**](TimeTrackingEntriesApi.md#update_time_tracking_entry) | **PUT** /time_tracking_entries/{time_tracking_entry_gid} | Update a time tracking entry

# **create_time_tracking_entry**

Create a time tracking entry

Creates a time tracking entry on a given task.  Returns the record of the newly created time tracking entry.  #### Access requirements  Access to this endpoint has two levels:  - **Endpoint access** requires time tracking to be available through the domain's plan or add-ons. A request from a domain without time tracking access returns a `402 Payment Required` error for every request to this endpoint.  - **Field access** for some request fields requires the Timesheets and Budgets add-on. Fields with this requirement are noted in the request schema. Including one of these fields without the add-on returns a `402 Payment Required` error, even when the rest of the request is valid.  Because the field-level requirement is separate, the same endpoint may return `201` or `402` for the same domain depending on which fields are sent: a request that only uses fields available with endpoint access succeeds on any domain that meets the endpoint requirement, while a request that includes a field requiring the add-on also requires the add-on.

([more information](https://developers.asana.com/reference/createtimetrackingentry))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
time_tracking_entries_api_instance = asana.TimeTrackingEntriesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | Information about the time tracking entry.
task_gid = "321654" # str | The task to operate on.
opts = {
    'opt_fields': "approval_status,attributable_to,attributable_to.name,attributable_to.resource_subtype,billable_status,categories,categories.color,categories.name,created_at,created_by,created_by.name,description,duration_minutes,entered_on,task,task.created_by,task.name,task.resource_subtype", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Create a time tracking entry
    api_response = time_tracking_entries_api_instance.create_time_tracking_entry(body, task_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingEntriesApi->create_time_tracking_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| Information about the time tracking entry. | 
 **task_gid** | **str**| The task to operate on. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_time_tracking_entry**

Delete a time tracking entry

A specific, existing time tracking entry can be deleted by making a `DELETE` request on the URL for that time tracking entry.  Returns an empty data record.  #### Access requirements  This endpoint is available only when time tracking is available through the domain's plan or add-ons. A request from a domain without time tracking access returns a `402 Payment Required` error.

([more information](https://developers.asana.com/reference/deletetimetrackingentry))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
time_tracking_entries_api_instance = asana.TimeTrackingEntriesApi(api_client)
time_tracking_entry_gid = "917392" # str | Globally unique identifier for the time tracking entry.


try:
    # Delete a time tracking entry
    api_response = time_tracking_entries_api_instance.delete_time_tracking_entry(time_tracking_entry_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingEntriesApi->delete_time_tracking_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_entry_gid** | **str**| Globally unique identifier for the time tracking entry. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_time_tracking_entries**

Get multiple time tracking entries

<b>Required scope: </b><code>time_tracking_entries:read</code>  Returns a list of time tracking entries filtered to a task, attributed project, portfolio or user.

([more information](https://developers.asana.com/reference/gettimetrackingentries))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
time_tracking_entries_api_instance = asana.TimeTrackingEntriesApi(api_client)
opts = {
    'task': "12345", # str | Globally unique identifier for the task to filter time tracking entries by.
    'attributable_to': "12345", # str | Globally unique identifier for the project the time tracking entries are attributed to.
    'portfolio': "12345", # str | Globally unique identifier for the portfolio to filter time tracking entries by.
    'user': "12345", # str | Globally unique identifier for the user to filter time tracking entries by.
    'workspace': "98765", # str | Globally unique identifier for the workspace. At least one of `entered_on_start_date` or `entered_on_end_date` must be provided when filtering by workspace.
    'entered_on_start_date': '2025-01-01', # date | The start date for filtering time tracking entries by when they were entered.
    'entered_on_end_date': '2025-12-31', # date | The end date for filtering time tracking entries by when they were entered.
    'timesheet_approval_status': "12345", # str | Globally unique identifier for the timesheet approval status to filter time tracking entries by.
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "attributable_to,attributable_to.name,attributable_to.resource_subtype,categories,categories.color,categories.name,created_by,created_by.name,duration_minutes,entered_on,offset,path,uri", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get multiple time tracking entries
    api_response = time_tracking_entries_api_instance.get_time_tracking_entries(opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling TimeTrackingEntriesApi->get_time_tracking_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task** | **str**| Globally unique identifier for the task to filter time tracking entries by. | [optional] 
 **attributable_to** | **str**| Globally unique identifier for the project the time tracking entries are attributed to. | [optional] 
 **portfolio** | **str**| Globally unique identifier for the portfolio to filter time tracking entries by. | [optional] 
 **user** | **str**| Globally unique identifier for the user to filter time tracking entries by. | [optional] 
 **workspace** | **str**| Globally unique identifier for the workspace. At least one of &#x60;entered_on_start_date&#x60; or &#x60;entered_on_end_date&#x60; must be provided when filtering by workspace. | [optional] 
 **entered_on_start_date** | **date**| The start date for filtering time tracking entries by when they were entered. | [optional] 
 **entered_on_end_date** | **date**| The end date for filtering time tracking entries by when they were entered. | [optional] 
 **timesheet_approval_status** | **str**| Globally unique identifier for the timesheet approval status to filter time tracking entries by. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_time_tracking_entries_for_task**

Get time tracking entries for a task

<b>Required scope: </b><code>time_tracking_entries:read</code>  Returns time tracking entries for a given task.

([more information](https://developers.asana.com/reference/gettimetrackingentriesfortask))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
time_tracking_entries_api_instance = asana.TimeTrackingEntriesApi(api_client)
task_gid = "321654" # str | The task to operate on.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "attributable_to,attributable_to.name,attributable_to.resource_subtype,categories,categories.color,categories.name,created_by,created_by.name,duration_minutes,entered_on,offset,path,uri", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get time tracking entries for a task
    api_response = time_tracking_entries_api_instance.get_time_tracking_entries_for_task(task_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling TimeTrackingEntriesApi->get_time_tracking_entries_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_time_tracking_entry**

Get a time tracking entry

<b>Required scope: </b><code>time_tracking_entries:read</code>  Returns the complete time tracking entry record for a single time tracking entry.

([more information](https://developers.asana.com/reference/gettimetrackingentry))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
time_tracking_entries_api_instance = asana.TimeTrackingEntriesApi(api_client)
time_tracking_entry_gid = "917392" # str | Globally unique identifier for the time tracking entry.
opts = {
    'opt_fields': "approval_status,attributable_to,attributable_to.name,attributable_to.resource_subtype,billable_status,categories,categories.color,categories.name,created_at,created_by,created_by.name,description,duration_minutes,entered_on,task,task.created_by,task.name,task.resource_subtype", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a time tracking entry
    api_response = time_tracking_entries_api_instance.get_time_tracking_entry(time_tracking_entry_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingEntriesApi->get_time_tracking_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_entry_gid** | **str**| Globally unique identifier for the time tracking entry. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_time_tracking_entry**

Update a time tracking entry

A specific, existing time tracking entry can be updated by making a `PUT` request on the URL for that time tracking entry. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the task.  Returns the complete updated time tracking entry record.  #### Access requirements  Access to this endpoint has two levels:  - **Endpoint access** requires time tracking to be available through the domain's plan or add-ons. A request from a domain without time tracking access returns a `402 Payment Required` error for every request to this endpoint.  - **Field access** for some request fields requires the Timesheets and Budgets add-on. Fields with this requirement are noted in the request schema. Including one of these fields without the add-on returns a `402 Payment Required` error, even when the rest of the request is valid.  Because the field-level requirement is separate, the same endpoint may return `200` or `402` for the same domain depending on which fields are sent: a request that only uses fields available with endpoint access succeeds on any domain that meets the endpoint requirement, while a request that includes a field requiring the add-on also requires the add-on.

([more information](https://developers.asana.com/reference/updatetimetrackingentry))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
time_tracking_entries_api_instance = asana.TimeTrackingEntriesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The updated fields for the time tracking entry.
time_tracking_entry_gid = "917392" # str | Globally unique identifier for the time tracking entry.
opts = {
    'opt_fields': "approval_status,attributable_to,attributable_to.name,attributable_to.resource_subtype,billable_status,categories,categories.color,categories.name,created_at,created_by,created_by.name,description,duration_minutes,entered_on,task,task.created_by,task.name,task.resource_subtype", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Update a time tracking entry
    api_response = time_tracking_entries_api_instance.update_time_tracking_entry(body, time_tracking_entry_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingEntriesApi->update_time_tracking_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The updated fields for the time tracking entry. | 
 **time_tracking_entry_gid** | **str**| Globally unique identifier for the time tracking entry. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

