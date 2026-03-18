# asana.RatesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rate**](RatesApi.md#create_rate) | **POST** /rates | Create a rate
[**delete_rate**](RatesApi.md#delete_rate) | **DELETE** /rates/{rate_gid} | Delete a rate
[**get_rate**](RatesApi.md#get_rate) | **GET** /rates/{rate_gid} | Get a rate
[**get_rates**](RatesApi.md#get_rates) | **GET** /rates | Get multiple rates
[**update_rate**](RatesApi.md#update_rate) | **PUT** /rates/{rate_gid} | Update a rate

# **create_rate**

Create a rate

Creates a new rate for a `parent` + `resource` combination.

([more information](https://developers.asana.com/reference/createrate))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
rates_api_instance = asana.RatesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The rate to create.
opts = {
    'opt_fields': "created_by,created_by.name,currency_code,parent,parent.name,rate,resource,resource.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Create a rate
    api_response = rates_api_instance.create_rate(body, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->create_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The rate to create. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_rate**

Delete a rate

Deletes a rate.

([more information](https://developers.asana.com/reference/deleterate))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
rates_api_instance = asana.RatesApi(api_client)
rate_gid = "12345" # str | Globally unique identifier for the rate.


try:
    # Delete a rate
    api_response = rates_api_instance.delete_rate(rate_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->delete_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_gid** | **str**| Globally unique identifier for the rate. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_rate**

Get a rate

Returns the complete rate record for a single rate.

([more information](https://developers.asana.com/reference/getrate))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
rates_api_instance = asana.RatesApi(api_client)
rate_gid = "12345" # str | Globally unique identifier for the rate.
opts = {
    'opt_fields': "created_by,created_by.name,currency_code,parent,parent.name,rate,resource,resource.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a rate
    api_response = rates_api_instance.get_rate(rate_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->get_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_gid** | **str**| Globally unique identifier for the rate. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_rates**

Get multiple rates

Returns a list of `rate` records. The possible types for `parent` in this request are `project`. An additional `resource` (`user` GID or `placeholder` GID) can be passed in to filter to a specific rate.  Modifying placeholder rates is only available for Enterprise and Enterprise+ users.

([more information](https://developers.asana.com/reference/getrates))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
rates_api_instance = asana.RatesApi(api_client)
opts = {
    'parent': "159874", # str | Globally unique identifier for `project`.
    'resource': "1061493", # str | Globally unique identifier for `user` or `placeholder`.
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "offset,path,uri", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get multiple rates
    api_response = rates_api_instance.get_rates(opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling RatesApi->get_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| Globally unique identifier for &#x60;project&#x60;. | [optional] 
 **resource** | **str**| Globally unique identifier for &#x60;user&#x60; or &#x60;placeholder&#x60;. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_rate**

Update a rate

An existing rate can be updated by making a PUT request on the URL for that rate. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged. (note that at this time, the only field that can be updated is the `rate` field.)  Returns the complete updated rate record.

([more information](https://developers.asana.com/reference/updaterate))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
rates_api_instance = asana.RatesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The updated fields for the rate.
rate_gid = "12345" # str | Globally unique identifier for the rate.
opts = {
    'opt_fields': "created_by,created_by.name,currency_code,parent,parent.name,rate,resource,resource.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Update a rate
    api_response = rates_api_instance.update_rate(body, rate_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatesApi->update_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The updated fields for the rate. | 
 **rate_gid** | **str**| Globally unique identifier for the rate. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

