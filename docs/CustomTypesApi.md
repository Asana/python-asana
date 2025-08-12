# asana.CustomTypesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_custom_type**](CustomTypesApi.md#get_custom_type) | **GET** /custom_types/{custom_type_gid} | Get a custom type
[**get_custom_types**](CustomTypesApi.md#get_custom_types) | **GET** /custom_types | Get all custom types associated with an object

# **get_custom_type**

Get a custom type

Returns the complete custom type record for a single custom type.

([more information](https://developers.asana.com/reference/getcustomtype))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
custom_types_api_instance = asana.CustomTypesApi(api_client)
custom_type_gid = "12345" # str | Globally unique identifier for the custom type.
opts = {
    'opt_fields': "name,status_options,status_options.color,status_options.completion_state,status_options.enabled,status_options.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a custom type
    api_response = custom_types_api_instance.get_custom_type(custom_type_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomTypesApi->get_custom_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_type_gid** | **str**| Globally unique identifier for the custom type. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_custom_types**

Get all custom types associated with an object

Returns a list of all of the custom types associated with an object. Currently, only projects are supported. Note that, as in all queries to collections which return compact representation, `opt_fields` can be used to include more data than is returned in the compact representation. See the [documentation for input/output options](https://developers.asana.com/docs/inputoutput-options) for more information.

([more information](https://developers.asana.com/reference/getcustomtypes))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
custom_types_api_instance = asana.CustomTypesApi(api_client)
project = "1331" # str | Globally unique identifier for the project, which is used as a filter when retrieving all custom types.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "name,offset,path,status_options,status_options.color,status_options.completion_state,status_options.enabled,status_options.name,uri", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get all custom types associated with an object
    api_response = custom_types_api_instance.get_custom_types(project, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling CustomTypesApi->get_custom_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Globally unique identifier for the project, which is used as a filter when retrieving all custom types. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

