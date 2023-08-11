# asana.StatusUpdatesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_status_for_object**](StatusUpdatesApi.md#create_status_for_object) | **POST** /status_updates | Create a status update
[**delete_status**](StatusUpdatesApi.md#delete_status) | **DELETE** /status_updates/{status_update_gid} | Delete a status update
[**get_status**](StatusUpdatesApi.md#get_status) | **GET** /status_updates/{status_update_gid} | Get a status update
[**get_statuses_for_object**](StatusUpdatesApi.md#get_statuses_for_object) | **GET** /status_updates | Get status updates from an object

# **create_status_for_object**
> StatusUpdateResponseData create_status_for_object(body, limit=limit, offset=offset, opt_fields=opt_fields)

Create a status update

Creates a new status update on an object. Returns the full record of the newly created status update.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.StatusUpdatesApi(api_client)
body = asana.StatusUpdatesBody({"param1": "value1", "param2": "value2",}) # StatusUpdatesBody | The status update to create.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["author","author.name","created_at","created_by","created_by.name","hearted","hearts","hearts.user","hearts.user.name","html_text","liked","likes","likes.user","likes.user.name","modified_at","num_hearts","num_likes","parent","parent.name","resource_subtype","status_type","text","title"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Create a status update
    api_response = api_instance.create_status_for_object(body, limit=limit, offset=offset, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusUpdatesApi->create_status_for_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusUpdatesBody**](StatusUpdatesBody.md)| The status update to create. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**StatusUpdateResponseData**](StatusUpdateResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_status**
> EmptyResponseData delete_status(status_update_gid)

Delete a status update

Deletes a specific, existing status update.  Returns an empty data record.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.StatusUpdatesApi(api_client)
status_update_gid = '321654' # str | The status update to get.

try:
    # Delete a status update
    api_response = api_instance.delete_status(status_update_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusUpdatesApi->delete_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_update_gid** | **str**| The status update to get. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> StatusUpdateResponseData get_status(status_update_gid, opt_fields=opt_fields)

Get a status update

Returns the complete record for a single status update.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.StatusUpdatesApi(api_client)
status_update_gid = '321654' # str | The status update to get.
opt_fields = ["author","author.name","created_at","created_by","created_by.name","hearted","hearts","hearts.user","hearts.user.name","html_text","liked","likes","likes.user","likes.user.name","modified_at","num_hearts","num_likes","parent","parent.name","resource_subtype","status_type","text","title"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a status update
    api_response = api_instance.get_status(status_update_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusUpdatesApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_update_gid** | **str**| The status update to get. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**StatusUpdateResponseData**](StatusUpdateResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statuses_for_object**
> StatusUpdateResponseArray get_statuses_for_object(parent, limit=limit, offset=offset, created_since=created_since, opt_fields=opt_fields)

Get status updates from an object

Returns the compact status update records for all updates on the object.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.StatusUpdatesApi(api_client)
parent = '159874' # str | Globally unique identifier for object to fetch statuses from. Must be a GID for a project, portfolio, or goal.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
created_since = '2012-02-22T02:06:58.158Z' # datetime | Only return statuses that have been created since the given time. (optional)
opt_fields = ["author","author.name","created_at","created_by","created_by.name","hearted","hearts","hearts.user","hearts.user.name","html_text","liked","likes","likes.user","likes.user.name","modified_at","num_hearts","num_likes","offset","parent","parent.name","path","resource_subtype","status_type","text","title","uri"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get status updates from an object
    api_response = api_instance.get_statuses_for_object(parent, limit=limit, offset=offset, created_since=created_since, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusUpdatesApi->get_statuses_for_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| Globally unique identifier for object to fetch statuses from. Must be a GID for a project, portfolio, or goal. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **created_since** | **datetime**| Only return statuses that have been created since the given time. | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**StatusUpdateResponseArray**](StatusUpdateResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

