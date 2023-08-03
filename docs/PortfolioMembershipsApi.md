# asana.PortfolioMembershipsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_portfolio_membership**](PortfolioMembershipsApi.md#get_portfolio_membership) | **GET** /portfolio_memberships/{portfolio_membership_gid} | Get a portfolio membership
[**get_portfolio_memberships**](PortfolioMembershipsApi.md#get_portfolio_memberships) | **GET** /portfolio_memberships | Get multiple portfolio memberships
[**get_portfolio_memberships_for_portfolio**](PortfolioMembershipsApi.md#get_portfolio_memberships_for_portfolio) | **GET** /portfolios/{portfolio_gid}/portfolio_memberships | Get memberships from a portfolio

# **get_portfolio_membership**
> PortfolioMembershipResponseData get_portfolio_membership(portfolio_membership_gid, opt_fields=opt_fields)

Get a portfolio membership

Returns the complete portfolio record for a single portfolio membership.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.PortfolioMembershipsApi(asana.ApiClient(configuration))
portfolio_membership_gid = '1331' # str | 
opt_fields = ["portfolio","portfolio.name","user","user.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get a portfolio membership
  api_response = api_instance.get_portfolio_membership(portfolio_membership_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling PortfolioMembershipsApi->get_portfolio_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_membership_gid** | **str**|  | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**PortfolioMembershipResponseData**](PortfolioMembershipResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_memberships**
> PortfolioMembershipResponseArray get_portfolio_memberships(portfolio=portfolio, workspace=workspace, user=user, limit=limit, offset=offset, opt_fields=opt_fields)

Get multiple portfolio memberships

Returns a list of portfolio memberships in compact representation. You must specify `portfolio`, `portfolio` and `user`, or `workspace` and `user`.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.PortfolioMembershipsApi(asana.ApiClient(configuration))
portfolio = '12345' # str | The portfolio to filter results on. (optional)
workspace = '12345' # str | The workspace to filter results on. (optional)
user = 'me' # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. (optional)
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["offset","path","portfolio","portfolio.name","uri","user","user.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get multiple portfolio memberships
  api_response = api_instance.get_portfolio_memberships(portfolio=portfolio, workspace=workspace, user=user, limit=limit, offset=offset, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling PortfolioMembershipsApi->get_portfolio_memberships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio** | **str**| The portfolio to filter results on. | [optional] 
 **workspace** | **str**| The workspace to filter results on. | [optional] 
 **user** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**PortfolioMembershipResponseArray**](PortfolioMembershipResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_memberships_for_portfolio**
> PortfolioMembershipResponseArray get_portfolio_memberships_for_portfolio(portfolio_gid, user=user, limit=limit, offset=offset, opt_fields=opt_fields)

Get memberships from a portfolio

Returns the compact portfolio membership records for the portfolio.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.PortfolioMembershipsApi(asana.ApiClient(configuration))
portfolio_gid = '12345' # str | Globally unique identifier for the portfolio.
user = 'me' # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. (optional)
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["offset","path","portfolio","portfolio.name","uri","user","user.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get memberships from a portfolio
  api_response = api_instance.get_portfolio_memberships_for_portfolio(portfolio_gid, user=user, limit=limit, offset=offset, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling PortfolioMembershipsApi->get_portfolio_memberships_for_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
 **user** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**PortfolioMembershipResponseArray**](PortfolioMembershipResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

