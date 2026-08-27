# asana.AIStudioUsageAPIApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ai_studio_runs**](AIStudioUsageAPIApi.md#get_ai_studio_runs) | **GET** /workspaces/{workspace_gid}/ai_studio/runs | Get AI Studio credit utilization
[**get_ai_studio_seats**](AIStudioUsageAPIApi.md#get_ai_studio_seats) | **GET** /workspaces/{workspace_gid}/ai_studio/seats | Get AI Studio seats

# **get_ai_studio_runs**

Get AI Studio credit utilization

Returns one row per AI Studio run (rule execution) for the workspace, in ascending order (oldest first) so that incremental consumers can poll forward. Each row describes what ran, who it is attributed to, the model used, and the credits consumed.  Credit data is available from January 8th, 2025 onward, and is queryable for the full history since then (there is no limit on how far back you can query). A `start_at` earlier than January 8th, 2025 is silently clamped; it is not an error.  The list is always [paginated](/docs/pagination). When more results exist, the response includes a `next_page` with an `offset` that can be used to retrieve the next set of rows. The row `gid` is stable and can be used to de-duplicate rows across incremental loads.  This endpoint is restricted to [service accounts](https://help.asana.com/s/article/service-accounts) in organizations licensed for AI Studio.

([more information](https://developers.asana.com/reference/getaistudioruns))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
ai_studio_usage_api_api_instance = asana.AIStudioUsageAPIApi(api_client)
workspace_gid = "12345" # str | Globally unique identifier for the workspace or organization.
opts = {
    'start_at': '2013-10-20T19:20:30+01:00', # datetime | Inclusive lower bound. Runs are ordered and filtered by when their usage was recorded (the monotonic timestamp used for incremental polling), not by `run_started_at`. Omitted ⇒ the 2025-01-08 floor — no credit data exists before then, and there is no limit on how far back you can query. A value earlier than 2025-01-08 is treated as 2025-01-08 (not rejected), matching the audit log.
    'end_at': '2013-10-20T19:20:30+01:00', # datetime | Filter to runs whose usage was recorded before this time (exclusive) — by when the run's credit usage was recorded, not by `run_started_at`. Defaults to the time of the request.
    'division_gid': "division_gid_example", # str | Scope results to a single division (its gid). Omitted ⇒ the org's first licensed division. Use this to retrieve only one division's slice (e.g. for a division-level admin or billing owner) rather than the whole organization.
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
}

try:
    # Get AI Studio credit utilization
    api_response = ai_studio_usage_api_api_instance.get_ai_studio_runs(workspace_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling AIStudioUsageAPIApi->get_ai_studio_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **start_at** | **datetime**| Inclusive lower bound. Runs are ordered and filtered by when their usage was recorded (the monotonic timestamp used for incremental polling), not by &#x60;run_started_at&#x60;. Omitted ⇒ the 2025-01-08 floor — no credit data exists before then, and there is no limit on how far back you can query. A value earlier than 2025-01-08 is treated as 2025-01-08 (not rejected), matching the audit log. | [optional] 
 **end_at** | **datetime**| Filter to runs whose usage was recorded before this time (exclusive) — by when the run&#x27;s credit usage was recorded, not by &#x60;run_started_at&#x60;. Defaults to the time of the request. | [optional] 
 **division_gid** | **str**| Scope results to a single division (its gid). Omitted ⇒ the org&#x27;s first licensed division. Use this to retrieve only one division&#x27;s slice (e.g. for a division-level admin or billing owner) rather than the whole organization. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_ai_studio_seats**

Get AI Studio seats

Returns a current snapshot of AI Studio seat allocations for the workspace — who has access, at what license tier, and the state of each seat. This is a point-in-time snapshot; customers build their own history tables on top of periodic pulls.  The list is always [paginated](/docs/pagination). When more results exist, the response includes a `next_page` with an `offset` that can be used to retrieve the next set of rows.  This endpoint is restricted to [service accounts](https://help.asana.com/s/article/service-accounts) in organizations licensed for AI Studio.

([more information](https://developers.asana.com/reference/getaistudioseats))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
ai_studio_usage_api_api_instance = asana.AIStudioUsageAPIApi(api_client)
workspace_gid = "12345" # str | Globally unique identifier for the workspace or organization.
opts = {
    'state': "state_example", # str | Filter seats to this state.
    'division_gid': "division_gid_example", # str | Scope results to a single division (its gid). Omitted ⇒ the org's first licensed division. Use this to retrieve only one division's slice (e.g. for a division-level admin or billing owner) rather than the whole organization.
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
}

try:
    # Get AI Studio seats
    api_response = ai_studio_usage_api_api_instance.get_ai_studio_seats(workspace_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling AIStudioUsageAPIApi->get_ai_studio_seats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **state** | **str**| Filter seats to this state. | [optional] 
 **division_gid** | **str**| Scope results to a single division (its gid). Omitted ⇒ the org&#x27;s first licensed division. Use this to retrieve only one division&#x27;s slice (e.g. for a division-level admin or billing owner) rather than the whole organization. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

