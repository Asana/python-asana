# asana.TimePeriodsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_time_period**](TimePeriodsApi.md#get_time_period) | **GET** /time_periods/{time_period_gid} | Get a time period
[**get_time_periods**](TimePeriodsApi.md#get_time_periods) | **GET** /time_periods | Get time periods

# **get_time_period**
> TimePeriodResponseData get_time_period(time_period_gid, opt_fields=opt_fields)

Get a time period

Returns the full record for a single time period.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.TimePeriodsApi(asana.ApiClient(configuration))
time_period_gid = '917392' # str | Globally unique identifier for the time period.
opt_fields = ["display_name","end_on","parent","parent.display_name","parent.end_on","parent.period","parent.start_on","period","start_on"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get a time period
  api_response = api_instance.get_time_period(time_period_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling TimePeriodsApi->get_time_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_period_gid** | **str**| Globally unique identifier for the time period. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TimePeriodResponseData**](TimePeriodResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_periods**
> TimePeriodResponseArray get_time_periods(workspace, limit=limit, offset=offset, start_on=start_on, end_on=end_on, opt_fields=opt_fields)

Get time periods

Returns compact time period records.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.TimePeriodsApi(asana.ApiClient(configuration))
workspace = '31326' # str | Globally unique identifier for the workspace.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
start_on = '2019-09-15' # date | ISO 8601 date string (optional)
end_on = '2019-09-15' # date | ISO 8601 date string (optional)
opt_fields = ["display_name","end_on","offset","parent","parent.display_name","parent.end_on","parent.period","parent.start_on","path","period","start_on","uri"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get time periods
  api_response = api_instance.get_time_periods(workspace, limit=limit, offset=offset, start_on=start_on, end_on=end_on, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling TimePeriodsApi->get_time_periods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Globally unique identifier for the workspace. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **start_on** | **date**| ISO 8601 date string | [optional] 
 **end_on** | **date**| ISO 8601 date string | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**TimePeriodResponseArray**](TimePeriodResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

