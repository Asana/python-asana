# asana.ReactionsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reactions_on_object**](ReactionsApi.md#get_reactions_on_object) | **GET** /reactions | Get reactions with an emoji base on an object.

# **get_reactions_on_object**

Get reactions with an emoji base on an object.

Returns the reactions with a specified emoji base character on the object.

([more information](https://developers.asana.com/reference/getreactionsonobject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
reactions_api_instance = asana.ReactionsApi(api_client)
target = "159874" # str | Globally unique identifier for object to fetch reactions from. Must be a GID for a status update or story.
emoji_base = "👍" # str | Only return reactions with this emoji base character.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
}

try:
    # Get reactions with an emoji base on an object.
    api_response = reactions_api_instance.get_reactions_on_object(target, emoji_base, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling ReactionsApi->get_reactions_on_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| Globally unique identifier for object to fetch reactions from. Must be a GID for a status update or story. | 
 **emoji_base** | **str**| Only return reactions with this emoji base character. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

