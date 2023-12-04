# asana.PortfolioMembershipsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_portfolio_membership**](PortfolioMembershipsApi.md#get_portfolio_membership) | **GET** /portfolio_memberships/{portfolio_membership_gid} | Get a portfolio membership
[**get_portfolio_memberships**](PortfolioMembershipsApi.md#get_portfolio_memberships) | **GET** /portfolio_memberships | Get multiple portfolio memberships
[**get_portfolio_memberships_for_portfolio**](PortfolioMembershipsApi.md#get_portfolio_memberships_for_portfolio) | **GET** /portfolios/{portfolio_gid}/portfolio_memberships | Get memberships from a portfolio

# **get_portfolio_membership**

Get a portfolio membership

Returns the complete portfolio record for a single portfolio membership.

([more information](https://developers.asana.com/reference/getportfoliomembership))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
portfolio_memberships_api_instance = asana.PortfolioMembershipsApi(api_client)
portfolio_membership_gid = "1331" # str | 
opts = { 
    'opt_fields': "portfolio,portfolio.name,user,user.name" # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a portfolio membership
    api_response = portfolio_memberships_api_instance.get_portfolio_membership(portfolio_membership_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfolioMembershipsApi->get_portfolio_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_membership_gid** | **str**|  | 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_portfolio_memberships**

Get multiple portfolio memberships

Returns a list of portfolio memberships in compact representation. You must specify `portfolio`, `portfolio` and `user`, or `workspace` and `user`.

([more information](https://developers.asana.com/reference/getportfoliomemberships))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
portfolio_memberships_api_instance = asana.PortfolioMembershipsApi(api_client)
opts = { 
    'portfolio': "12345", # str | The portfolio to filter results on.
    'workspace': "12345", # str | The workspace to filter results on.
    'user': "me", # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    'opt_fields': "offset,path,portfolio,portfolio.name,uri,user,user.name" # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get multiple portfolio memberships
    api_response = portfolio_memberships_api_instance.get_portfolio_memberships(opts)
    for data in api_response:
        pprint(data)
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
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_portfolio_memberships_for_portfolio**

Get memberships from a portfolio

Returns the compact portfolio membership records for the portfolio.

([more information](https://developers.asana.com/reference/getportfoliomembershipsforportfolio))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
portfolio_memberships_api_instance = asana.PortfolioMembershipsApi(api_client)
portfolio_gid = "12345" # str | Globally unique identifier for the portfolio.
opts = { 
    'user': "me", # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    'opt_fields': "offset,path,portfolio,portfolio.name,uri,user,user.name" # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get memberships from a portfolio
    api_response = portfolio_memberships_api_instance.get_portfolio_memberships_for_portfolio(portfolio_gid, opts)
    for data in api_response:
        pprint(data)
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
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

