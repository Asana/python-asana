# asana.AccessRequestsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_access_request**](AccessRequestsApi.md#approve_access_request) | **POST** /access_requests/{access_request_gid}/approve | Approve an access request
[**create_access_request**](AccessRequestsApi.md#create_access_request) | **POST** /access_requests | Create an access request
[**get_access_requests**](AccessRequestsApi.md#get_access_requests) | **GET** /access_requests | Get access requests
[**reject_access_request**](AccessRequestsApi.md#reject_access_request) | **POST** /access_requests/{access_request_gid}/reject | Reject an access request

# **approve_access_request**

Approve an access request

Approves an access request for a target object.

([more information](https://developers.asana.com/reference/approveaccessrequest))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
access_requests_api_instance = asana.AccessRequestsApi(api_client)
access_request_gid = "12345" # str | Globally unique identifier for the access request.


try:
    # Approve an access request
    api_response = access_requests_api_instance.approve_access_request(access_request_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessRequestsApi->approve_access_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_request_gid** | **str**| Globally unique identifier for the access request. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_access_request**

Create an access request

Submits a new access request for a private object. Currently supports projects and portfolios.

([more information](https://developers.asana.com/reference/createaccessrequest))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
access_requests_api_instance = asana.AccessRequestsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | 


try:
    # Create an access request
    api_response = access_requests_api_instance.create_access_request(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessRequestsApi->create_access_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**|  | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_access_requests**

Get access requests

Returns the pending access requests for a target object or a target object filtered by user.

([more information](https://developers.asana.com/reference/getaccessrequests))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
access_requests_api_instance = asana.AccessRequestsApi(api_client)
target = "1331" # str | Globally unique identifier for the target object.
opts = {
    'user': "me", # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
    'opt_fields': "approval_status,message,requester,requester.name,target", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get access requests
    api_response = access_requests_api_instance.get_access_requests(target, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling AccessRequestsApi->get_access_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| Globally unique identifier for the target object. | 
 **user** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **reject_access_request**

Reject an access request

Rejects an access request for a target object.

([more information](https://developers.asana.com/reference/rejectaccessrequest))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
access_requests_api_instance = asana.AccessRequestsApi(api_client)
access_request_gid = "12345" # str | Globally unique identifier for the access request.


try:
    # Reject an access request
    api_response = access_requests_api_instance.reject_access_request(access_request_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessRequestsApi->reject_access_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_request_gid** | **str**| Globally unique identifier for the access request. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

