# asana.AllocationsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_allocation**](AllocationsApi.md#create_allocation) | **POST** /allocations | Create an allocation
[**delete_allocation**](AllocationsApi.md#delete_allocation) | **DELETE** /allocations/{allocation_gid} | Delete an allocation
[**get_allocation**](AllocationsApi.md#get_allocation) | **GET** /allocations/{allocation_gid} | Get an allocation
[**get_allocations**](AllocationsApi.md#get_allocations) | **GET** /allocations | Get multiple allocations
[**update_allocation**](AllocationsApi.md#update_allocation) | **PUT** /allocations/{allocation_gid} | Update an allocation

# **create_allocation**

Create an allocation

Creates a new allocation.  Returns the full record of the newly created allocation.

([more information](https://developers.asana.com/reference/createallocation))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
allocations_api_instance = asana.AllocationsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The allocation to create.
opts = {
    'opt_fields': "assignee,assignee.name,created_by,created_by.name,effort,effort.type,effort.value,end_date,parent,parent.name,resource_subtype,start_date", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Create an allocation
    api_response = allocations_api_instance.create_allocation(body, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AllocationsApi->create_allocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The allocation to create. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_allocation**

Delete an allocation

A specific, existing allocation can be deleted by making a DELETE request on the URL for that allocation.  Returns an empty data record.

([more information](https://developers.asana.com/reference/deleteallocation))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
allocations_api_instance = asana.AllocationsApi(api_client)
allocation_gid = "77688" # str | Globally unique identifier for the allocation.


try:
    # Delete an allocation
    api_response = allocations_api_instance.delete_allocation(allocation_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AllocationsApi->delete_allocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocation_gid** | **str**| Globally unique identifier for the allocation. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_allocation**

Get an allocation

Returns the complete allocation record for a single allocation.

([more information](https://developers.asana.com/reference/getallocation))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
allocations_api_instance = asana.AllocationsApi(api_client)
allocation_gid = "77688" # str | Globally unique identifier for the allocation.
opts = {
    'opt_fields': "assignee,assignee.name,created_by,created_by.name,effort,effort.type,effort.value,end_date,parent,parent.name,resource_subtype,start_date", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get an allocation
    api_response = allocations_api_instance.get_allocation(allocation_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AllocationsApi->get_allocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocation_gid** | **str**| Globally unique identifier for the allocation. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_allocations**

Get multiple allocations

Returns a list of allocations filtered to a specific project, user or placeholder.

([more information](https://developers.asana.com/reference/getallocations))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
allocations_api_instance = asana.AllocationsApi(api_client)
opts = {
    'parent': "77688", # str | Globally unique identifier for the project to filter allocations by.
    'assignee': "12345", # str | Globally unique identifier for the user or placeholder the allocation is assigned to.
    'workspace': "98765", # str | Globally unique identifier for the workspace.
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "assignee,assignee.name,created_by,created_by.name,effort,effort.type,effort.value,end_date,offset,parent,parent.name,path,resource_subtype,start_date,uri", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get multiple allocations
    api_response = allocations_api_instance.get_allocations(opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling AllocationsApi->get_allocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| Globally unique identifier for the project to filter allocations by. | [optional] 
 **assignee** | **str**| Globally unique identifier for the user or placeholder the allocation is assigned to. | [optional] 
 **workspace** | **str**| Globally unique identifier for the workspace. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_allocation**

Update an allocation

An existing allocation can be updated by making a PUT request on the URL for that allocation. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated allocation record.

([more information](https://developers.asana.com/reference/updateallocation))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
allocations_api_instance = asana.AllocationsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The updated fields for the allocation.
allocation_gid = "77688" # str | Globally unique identifier for the allocation.
opts = {
    'opt_fields': "assignee,assignee.name,created_by,created_by.name,effort,effort.type,effort.value,end_date,parent,parent.name,resource_subtype,start_date", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Update an allocation
    api_response = allocations_api_instance.update_allocation(body, allocation_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AllocationsApi->update_allocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The updated fields for the allocation. | 
 **allocation_gid** | **str**| Globally unique identifier for the allocation. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

