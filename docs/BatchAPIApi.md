# asana.BatchAPIApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_batch_request**](BatchAPIApi.md#create_batch_request) | **POST** /batch | Submit parallel requests

# **create_batch_request**
> BatchResponseArray create_batch_request(body, opt_fields=opt_fields)

Submit parallel requests

Make multiple requests in parallel to Asana's API.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.BatchAPIApi(asana.ApiClient(configuration))
body = asana.BatchBody({"param1": "value1", "param2": "value2",}) # BatchBody | The requests to batch together via the Batch API.
opt_fields = ["body","headers","status_code"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Submit parallel requests
  api_response = api_instance.create_batch_request(body, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling BatchAPIApi->create_batch_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchBody**](BatchBody.md)| The requests to batch together via the Batch API. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**BatchResponseArray**](BatchResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

