# asana.BatchAPIApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch_request**](BatchAPIApi.md#create_batch_request) | **POST** /batch | Submit parallel requests

# **create_batch_request**

Submit parallel requests

Make multiple requests in parallel to Asana's API.

([more information](https://developers.asana.com/reference/createbatchrequest))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
batch_api_api_instance = asana.BatchAPIApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The requests to batch together via the Batch API.
opts = {
    'opt_fields': "body,headers,status_code", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Submit parallel requests
    api_response = batch_api_api_instance.create_batch_request(body, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling BatchAPIApi->create_batch_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The requests to batch together via the Batch API. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

