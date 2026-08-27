# asana.TimeTrackingCategoriesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_time_tracking_category**](TimeTrackingCategoriesApi.md#create_time_tracking_category) | **POST** /time_tracking_categories | Create a time tracking category
[**delete_time_tracking_category**](TimeTrackingCategoriesApi.md#delete_time_tracking_category) | **DELETE** /time_tracking_categories/{time_tracking_category_gid} | Delete a time tracking category
[**get_time_tracking_categories**](TimeTrackingCategoriesApi.md#get_time_tracking_categories) | **GET** /time_tracking_categories | Get time tracking categories for a workspace
[**get_time_tracking_category**](TimeTrackingCategoriesApi.md#get_time_tracking_category) | **GET** /time_tracking_categories/{time_tracking_category_gid} | Get a time tracking category
[**get_time_tracking_entries_for_time_tracking_category**](TimeTrackingCategoriesApi.md#get_time_tracking_entries_for_time_tracking_category) | **GET** /time_tracking_categories/{time_tracking_category_gid}/time_tracking_entries | Get time tracking entries for a time tracking category
[**update_time_tracking_category**](TimeTrackingCategoriesApi.md#update_time_tracking_category) | **PUT** /time_tracking_categories/{time_tracking_category_gid} | Update a time tracking category

# **create_time_tracking_category**

Create a time tracking category

<b>Required scope: </b><code>time_tracking_categories:write</code>  Creates a new time tracking category in a given workspace.  Returns the record of the newly created time tracking category.

([more information](https://developers.asana.com/reference/createtimetrackingcategory))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
time_tracking_categories_api_instance = asana.TimeTrackingCategoriesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | Information about the time tracking category.
opts = {
    'opt_fields': "color,is_archived,name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Create a time tracking category
    api_response = time_tracking_categories_api_instance.create_time_tracking_category(body, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingCategoriesApi->create_time_tracking_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| Information about the time tracking category. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_time_tracking_category**

Delete a time tracking category

<b>Required scope: </b><code>time_tracking_categories:delete</code>  Deletes a specific, existing time tracking category.  Returns an empty data record.

([more information](https://developers.asana.com/reference/deletetimetrackingcategory))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
time_tracking_categories_api_instance = asana.TimeTrackingCategoriesApi(api_client)
time_tracking_category_gid = "917392" # str | Globally unique identifier for the time tracking category.


try:
    # Delete a time tracking category
    api_response = time_tracking_categories_api_instance.delete_time_tracking_category(time_tracking_category_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingCategoriesApi->delete_time_tracking_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_category_gid** | **str**| Globally unique identifier for the time tracking category. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_time_tracking_categories**

Get time tracking categories for a workspace

<b>Required scope: </b><code>time_tracking_categories:read</code>  Returns a paginated list of time tracking categories for a given workspace.

([more information](https://developers.asana.com/reference/gettimetrackingcategories))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
time_tracking_categories_api_instance = asana.TimeTrackingCategoriesApi(api_client)
workspace = "12345" # str | Globally unique identifier for the workspace.
opts = {
    'is_archived': False, # bool | Filter by archived status. If not provided, defaults to returning non-archived categories.
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "color,is_archived,name,offset,path,uri", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get time tracking categories for a workspace
    api_response = time_tracking_categories_api_instance.get_time_tracking_categories(workspace, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling TimeTrackingCategoriesApi->get_time_tracking_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Globally unique identifier for the workspace. | 
 **is_archived** | **bool**| Filter by archived status. If not provided, defaults to returning non-archived categories. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_time_tracking_category**

Get a time tracking category

<b>Required scope: </b><code>time_tracking_categories:read</code>  Returns the complete time tracking category record for a single time tracking category.

([more information](https://developers.asana.com/reference/gettimetrackingcategory))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
time_tracking_categories_api_instance = asana.TimeTrackingCategoriesApi(api_client)
time_tracking_category_gid = "917392" # str | Globally unique identifier for the time tracking category.
opts = {
    'opt_fields': "color,is_archived,name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a time tracking category
    api_response = time_tracking_categories_api_instance.get_time_tracking_category(time_tracking_category_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingCategoriesApi->get_time_tracking_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_category_gid** | **str**| Globally unique identifier for the time tracking category. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_time_tracking_entries_for_time_tracking_category**

Get time tracking entries for a time tracking category

<b>Required scope: </b><code>time_tracking_categories:read</code>  Returns a paginated list of time tracking entries filtered by a given time tracking category.

([more information](https://developers.asana.com/reference/gettimetrackingentriesfortimetrackingcategory))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
time_tracking_categories_api_instance = asana.TimeTrackingCategoriesApi(api_client)
time_tracking_category_gid = "917392" # str | Globally unique identifier for the time tracking category.
opts = {
    'start_date': '2025-01-01', # date | The start date for filtering time tracking entries by their entry date.
    'end_date': '2025-12-31', # date | The end date for filtering time tracking entries by their entry date.
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "attributable_to,attributable_to.name,attributable_to.resource_subtype,categories,categories.color,categories.name,created_by,created_by.name,duration_minutes,entered_on,offset,path,uri", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get time tracking entries for a time tracking category
    api_response = time_tracking_categories_api_instance.get_time_tracking_entries_for_time_tracking_category(time_tracking_category_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling TimeTrackingCategoriesApi->get_time_tracking_entries_for_time_tracking_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_tracking_category_gid** | **str**| Globally unique identifier for the time tracking category. | 
 **start_date** | **date**| The start date for filtering time tracking entries by their entry date. | [optional] 
 **end_date** | **date**| The end date for filtering time tracking entries by their entry date. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_time_tracking_category**

Update a time tracking category

<b>Required scope: </b><code>time_tracking_categories:write</code>  Updates the properties of a time tracking category. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated time tracking category record.

([more information](https://developers.asana.com/reference/updatetimetrackingcategory))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
time_tracking_categories_api_instance = asana.TimeTrackingCategoriesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The updated fields for the time tracking category.
time_tracking_category_gid = "917392" # str | Globally unique identifier for the time tracking category.
opts = {
    'opt_fields': "color,is_archived,name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Update a time tracking category
    api_response = time_tracking_categories_api_instance.update_time_tracking_category(body, time_tracking_category_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TimeTrackingCategoriesApi->update_time_tracking_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The updated fields for the time tracking category. | 
 **time_tracking_category_gid** | **str**| Globally unique identifier for the time tracking category. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

