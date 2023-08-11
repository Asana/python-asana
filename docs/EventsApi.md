# asana.EventsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_events**](EventsApi.md#get_events) | **GET** /events | Get events on a resource

# **get_events**
> EventResponseArray get_events(resource, sync=sync, opt_fields=opt_fields)

Get events on a resource

Returns the full record for all events that have occurred since the sync token was created.  A `GET` request to the endpoint `/[path_to_resource]/events` can be made in lieu of including the resource ID in the data for the request.  Asana limits a single sync token to 100 events. If more than 100 events exist for a given resource, `has_more: true` will be returned in the response, indicating that there are more events to pull.  *Note: The resource returned will be the resource that triggered the event. This may be different from the one that the events were requested for. For example, a subscription to a project will contain events for tasks contained within the project.*

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
api_instance = asana.EventsApi(api_client)
resource = '12345' # str | A resource ID to subscribe to. The resource can be a task or project.
sync = 'de4774f6915eae04714ca93bb2f5ee81' # str | A sync token received from the last request, or none on first sync. Events will be returned from the point in time that the sync token was generated. *Note: On your first request, omit the sync token. The response will be the same as for an expired sync token, and will include a new valid sync token.If the sync token is too old (which may happen from time to time) the API will return a `412 Precondition Failed` error, and include a fresh sync token in the response.* (optional)
opt_fields = ["action","change","change.action","change.added_value","change.field","change.new_value","change.removed_value","created_at","parent","parent.name","resource","resource.name","type","user","user.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get events on a resource
    api_response = api_instance.get_events(resource, sync=sync, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**| A resource ID to subscribe to. The resource can be a task or project. | 
 **sync** | **str**| A sync token received from the last request, or none on first sync. Events will be returned from the point in time that the sync token was generated. *Note: On your first request, omit the sync token. The response will be the same as for an expired sync token, and will include a new valid sync token.If the sync token is too old (which may happen from time to time) the API will return a &#x60;412 Precondition Failed&#x60; error, and include a fresh sync token in the response.* | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**EventResponseArray**](EventResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

