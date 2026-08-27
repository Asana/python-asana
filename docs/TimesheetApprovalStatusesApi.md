# asana.TimesheetApprovalStatusesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_timesheet_approval_status**](TimesheetApprovalStatusesApi.md#create_timesheet_approval_status) | **POST** /timesheet_approval_statuses | Create a timesheet approval status
[**get_timesheet_approval_status**](TimesheetApprovalStatusesApi.md#get_timesheet_approval_status) | **GET** /timesheet_approval_statuses/{timesheet_approval_status_gid} | Get a timesheet approval status
[**get_timesheet_approval_statuses**](TimesheetApprovalStatusesApi.md#get_timesheet_approval_statuses) | **GET** /timesheet_approval_statuses | Get multiple timesheet approval statuses
[**update_timesheet_approval_status**](TimesheetApprovalStatusesApi.md#update_timesheet_approval_status) | **PUT** /timesheet_approval_statuses/{timesheet_approval_status_gid} | Update a timesheet approval status

# **create_timesheet_approval_status**

Create a timesheet approval status

<b>Required scope: </b><code>timesheet_approval_statuses:write</code>  Creates a new timesheet approval status for a user's timesheet week. The start_date must be a Monday or Sunday, and end_date must be the last day of that week (Sunday for a Monday start, Saturday for a Sunday start). Returns the created timesheet approval status record.

([more information](https://developers.asana.com/reference/createtimesheetapprovalstatus))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
timesheet_approval_statuses_api_instance = asana.TimesheetApprovalStatusesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The timesheet approval status to create.
opts = {
    'opt_fields': "approval_status,created_at,end_date,start_date,user,user.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Create a timesheet approval status
    api_response = timesheet_approval_statuses_api_instance.create_timesheet_approval_status(body, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApprovalStatusesApi->create_timesheet_approval_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The timesheet approval status to create. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_timesheet_approval_status**

Get a timesheet approval status

<b>Required scope: </b><code>timesheet_approval_statuses:read</code>  Returns the complete timesheet approval status record for a single timesheet approval status.

([more information](https://developers.asana.com/reference/gettimesheetapprovalstatus))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
timesheet_approval_statuses_api_instance = asana.TimesheetApprovalStatusesApi(api_client)
timesheet_approval_status_gid = "917392" # str | Globally unique identifier for the timesheet approval status.
opts = {
    'opt_fields': "approval_status,created_at,end_date,start_date,user,user.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a timesheet approval status
    api_response = timesheet_approval_statuses_api_instance.get_timesheet_approval_status(timesheet_approval_status_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApprovalStatusesApi->get_timesheet_approval_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timesheet_approval_status_gid** | **str**| Globally unique identifier for the timesheet approval status. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_timesheet_approval_statuses**

Get multiple timesheet approval statuses

<b>Required scope: </b><code>timesheet_approval_statuses:read</code>  Returns a list of timesheet approval statuses filtered by workspace and optionally by user, date range, or approval status.

([more information](https://developers.asana.com/reference/gettimesheetapprovalstatuses))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
timesheet_approval_statuses_api_instance = asana.TimesheetApprovalStatusesApi(api_client)
workspace = "12345" # str | Globally unique identifier for the workspace.
opts = {
    'user': "67890", # str | Globally unique identifier for the user to filter timesheet approval statuses by.
    'from_date': '2025-11-01', # date | The start date for filtering timesheet approval statuses.
    'to_date': '2025-11-30', # date | The end date for filtering timesheet approval statuses.
    'approval_statuses': "draft", # str | Filter by approval status. Can be one or more of draft, submitted, approved, or rejected.
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "approval_status,created_at,end_date,offset,path,start_date,uri,user,user.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get multiple timesheet approval statuses
    api_response = timesheet_approval_statuses_api_instance.get_timesheet_approval_statuses(workspace, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling TimesheetApprovalStatusesApi->get_timesheet_approval_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Globally unique identifier for the workspace. | 
 **user** | **str**| Globally unique identifier for the user to filter timesheet approval statuses by. | [optional] 
 **from_date** | **date**| The start date for filtering timesheet approval statuses. | [optional] 
 **to_date** | **date**| The end date for filtering timesheet approval statuses. | [optional] 
 **approval_statuses** | **str**| Filter by approval status. Can be one or more of draft, submitted, approved, or rejected. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_timesheet_approval_status**

Update a timesheet approval status

<b>Required scope: </b><code>timesheet_approval_statuses:write</code>  Updates the approval status of a timesheet approval status. The update supports state transitions such as submitting, recalling submission, approving, and rejecting. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged. Invalid transitions will result in a 400 error.

([more information](https://developers.asana.com/reference/updatetimesheetapprovalstatus))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
timesheet_approval_statuses_api_instance = asana.TimesheetApprovalStatusesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The fields to update on the timesheet approval status.
timesheet_approval_status_gid = "917392" # str | Globally unique identifier for the timesheet approval status.
opts = {
    'opt_fields': "approval_status,created_at,end_date,start_date,user,user.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Update a timesheet approval status
    api_response = timesheet_approval_statuses_api_instance.update_timesheet_approval_status(body, timesheet_approval_status_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimesheetApprovalStatusesApi->update_timesheet_approval_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The fields to update on the timesheet approval status. | 
 **timesheet_approval_status_gid** | **str**| Globally unique identifier for the timesheet approval status. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

