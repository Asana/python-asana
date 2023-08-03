# asana.AuditLogAPIApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audit_log_events**](AuditLogAPIApi.md#get_audit_log_events) | **GET** /workspaces/{workspace_gid}/audit_log_events | Get audit log events

# **get_audit_log_events**
> AuditLogEventArray get_audit_log_events(workspace_gid, start_at=start_at, end_at=end_at, event_type=event_type, actor_type=actor_type, actor_gid=actor_gid, resource_gid=resource_gid, limit=limit, offset=offset)

Get audit log events

Retrieve the audit log events that have been captured in your domain.  This endpoint will return a list of [AuditLogEvent](/reference/audit-log-api) objects, sorted by creation time in ascending order. Note that the Audit Log API captures events from October 8th, 2021 and later. Queries for events before this date will not return results.  There are a number of query parameters (below) that can be used to filter the set of [AuditLogEvent](/reference/audit-log-api) objects that are returned in the response. Any combination of query parameters is valid. When no filters are provided, all of the events that have been captured in your domain will match.  The list of events will always be [paginated](/docs/pagination). The default limit is 1000 events. The next set of events can be retrieved using the `offset` from the previous response. If there are no events that match the provided filters in your domain, the endpoint will return `null` for the `next_page` field. Querying again with the same filters may return new events if they were captured after the last request. Once a response includes a `next_page` with an `offset`, subsequent requests can be made with the latest `offset` to poll for new events that match the provided filters.  *Note: If the filters you provided match events in your domain and `next_page` is present in the response, we will continue to send `next_page` on subsequent requests even when there are no more events that match the filters. This was put in place so that you can implement an audit log stream that will return future events that match these filters. If you are not interested in future events that match the filters you have defined, you can rely on checking empty `data` response for the end of current events that match your filters.*  When no `offset` is provided, the response will begin with the oldest events that match the provided filters. It is important to note that [AuditLogEvent](/reference/audit-log-api) objects will be permanently deleted from our systems after 90 days. If you wish to keep a permanent record of these events, we recommend using a SIEM tool to ingest and store these logs.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.AuditLogAPIApi(asana.ApiClient(configuration))
workspace_gid = '12345' # str | Globally unique identifier for the workspace or organization.
start_at = '2013-10-20T19:20:30+01:00' # datetime | Filter to events created after this time (inclusive). (optional)
end_at = '2013-10-20T19:20:30+01:00' # datetime | Filter to events created before this time (exclusive). (optional)
event_type = 'event_type_example' # str | Filter to events of this type. Refer to the [supported audit log events](/docs/audit-log-events#supported-audit-log-events) for a full list of values. (optional)
actor_type = 'actor_type_example' # str | Filter to events with an actor of this type. This only needs to be included if querying for actor types without an ID. If `actor_gid` is included, this should be excluded. (optional)
actor_gid = 'actor_gid_example' # str | Filter to events triggered by the actor with this ID. (optional)
resource_gid = 'resource_gid_example' # str | Filter to events with this resource ID. (optional)
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)

try:
  # Get audit log events
  api_response = api_instance.get_audit_log_events(workspace_gid, start_at=start_at, end_at=end_at, event_type=event_type, actor_type=actor_type, actor_gid=actor_gid, resource_gid=resource_gid, limit=limit, offset=offset)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling AuditLogAPIApi->get_audit_log_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **start_at** | **datetime**| Filter to events created after this time (inclusive). | [optional] 
 **end_at** | **datetime**| Filter to events created before this time (exclusive). | [optional] 
 **event_type** | **str**| Filter to events of this type. Refer to the [supported audit log events](/docs/audit-log-events#supported-audit-log-events) for a full list of values. | [optional] 
 **actor_type** | **str**| Filter to events with an actor of this type. This only needs to be included if querying for actor types without an ID. If &#x60;actor_gid&#x60; is included, this should be excluded. | [optional] 
 **actor_gid** | **str**| Filter to events triggered by the actor with this ID. | [optional] 
 **resource_gid** | **str**| Filter to events with this resource ID. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 

### Return type

[**AuditLogEventArray**](AuditLogEventArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

