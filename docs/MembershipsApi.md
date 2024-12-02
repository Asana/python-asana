# asana.MembershipsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_membership**](MembershipsApi.md#create_membership) | **POST** /memberships | Create a membership
[**delete_membership**](MembershipsApi.md#delete_membership) | **DELETE** /memberships/{membership_gid} | Delete a membership
[**get_membership**](MembershipsApi.md#get_membership) | **GET** /memberships/{membership_gid} | Get a membership
[**get_memberships**](MembershipsApi.md#get_memberships) | **GET** /memberships | Get multiple memberships
[**update_membership**](MembershipsApi.md#update_membership) | **PUT** /memberships/{membership_gid} | Update a membership

# **create_membership**

Create a membership

Creates a new membership in a `goal`, `project`, or `portfolio`. Teams or users can be members of `goals` or `projects`. Portfolios only support `users` as members.  Returns the full record of the newly created membership.

([more information](https://developers.asana.com/reference/createmembership))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
memberships_api_instance = asana.MembershipsApi(api_client)
opts = {
    'body': {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}}, # dict | The updated fields for the membership.
}

try:
    # Create a membership
    api_response = memberships_api_instance.create_membership(opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MembershipsApi->create_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The updated fields for the membership. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_membership**

Delete a membership

A specific, existing membership for a `goal`, `project` and `portfolio` can be deleted by making a `DELETE` request on the URL for that membership.  Returns an empty data record.

([more information](https://developers.asana.com/reference/deletemembership))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
memberships_api_instance = asana.MembershipsApi(api_client)
membership_gid = "12345" # str | Globally unique identifier for the membership.


try:
    # Delete a membership
    api_response = memberships_api_instance.delete_membership(membership_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MembershipsApi->delete_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_gid** | **str**| Globally unique identifier for the membership. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_membership**

Get a membership

Returns compact `project_membership` record for a single membership. `GET` only supports project memberships currently

([more information](https://developers.asana.com/reference/getmembership))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
memberships_api_instance = asana.MembershipsApi(api_client)
membership_gid = "12345" # str | Globally unique identifier for the membership.
opts = {
    'opt_fields': "access_level,member,member.name,parent,parent.name,resource_subtype", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a membership
    api_response = memberships_api_instance.get_membership(membership_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MembershipsApi->get_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_gid** | **str**| Globally unique identifier for the membership. | 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_memberships**

Get multiple memberships

Returns compact `goal_membership`, `project_membership`, or `portfolio_membership` records. The possible types for `parent` in this request are `goal`, `project`, or `portfolio`. An additional member (user GID or team GID) can be passed in to filter to a specific membership. Teams are not supported for portfolios yet.

([more information](https://developers.asana.com/reference/getmemberships))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
memberships_api_instance = asana.MembershipsApi(api_client)
opts = {
    'parent': "159874", # str | Globally unique identifier for `goal`, `project`, or `portfolio`.
    'member': "1061493", # str | Globally unique identifier for `team` or `user`.
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "offset,path,uri", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get multiple memberships
    api_response = memberships_api_instance.get_memberships(opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling MembershipsApi->get_memberships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| Globally unique identifier for &#x60;goal&#x60;, &#x60;project&#x60;, or &#x60;portfolio&#x60;. | [optional] 
 **member** | **str**| Globally unique identifier for &#x60;team&#x60; or &#x60;user&#x60;. | [optional] 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_membership**

Update a membership

An existing membership can be updated by making a `PUT` request on the membership. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged. Memberships on `goals`, `projects` and `portfolios` can be updated.  Returns the full record of the updated membership.

([more information](https://developers.asana.com/reference/updatemembership))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
memberships_api_instance = asana.MembershipsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The membership to update.
membership_gid = "12345" # str | Globally unique identifier for the membership.


try:
    # Update a membership
    api_response = memberships_api_instance.update_membership(body, membership_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MembershipsApi->update_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The membership to update. | 
 **membership_gid** | **str**| Globally unique identifier for the membership. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

