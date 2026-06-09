# asana.OooEntriesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ooo_entry**](OooEntriesApi.md#create_ooo_entry) | **POST** /ooo_entries | Create an OOO entry
[**delete_ooo_entry**](OooEntriesApi.md#delete_ooo_entry) | **DELETE** /ooo_entries/{ooo_entry_gid} | Delete an OOO entry
[**get_ooo_entries**](OooEntriesApi.md#get_ooo_entries) | **GET** /ooo_entries | Get OOO entries for a user
[**get_ooo_entry**](OooEntriesApi.md#get_ooo_entry) | **GET** /ooo_entries/{ooo_entry_gid} | Get an OOO entry
[**update_ooo_entry**](OooEntriesApi.md#update_ooo_entry) | **PUT** /ooo_entries/{ooo_entry_gid} | Update an OOO entry

# **create_ooo_entry**

Create an OOO entry

<b>Required scope: </b><code>ooo_entries:write</code>  Creates a new OOO entry.  Returns the full record of the newly created OOO entry.

([more information](https://developers.asana.com/reference/createoooentry))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
ooo_entries_api_instance = asana.OooEntriesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The OOO entry to create.
opts = {
    'opt_fields': "created_by,created_by.name,end_date,start_date,user,user.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Create an OOO entry
    api_response = ooo_entries_api_instance.create_ooo_entry(body, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OooEntriesApi->create_ooo_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The OOO entry to create. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_ooo_entry**

Delete an OOO entry

<b>Required scope: </b><code>ooo_entries:delete</code>  A specific, existing OOO entry can be deleted by making a DELETE request on the URL for that OOO entry.  Returns an empty data record.

([more information](https://developers.asana.com/reference/deleteoooentry))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
ooo_entries_api_instance = asana.OooEntriesApi(api_client)
ooo_entry_gid = "12345" # str | Globally unique identifier for the OOO entry.


try:
    # Delete an OOO entry
    api_response = ooo_entries_api_instance.delete_ooo_entry(ooo_entry_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OooEntriesApi->delete_ooo_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ooo_entry_gid** | **str**| Globally unique identifier for the OOO entry. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_ooo_entries**

Get OOO entries for a user

<b>Required scope: </b><code>ooo_entries:read</code>  Returns a list of OOO entries for the specified user.

([more information](https://developers.asana.com/reference/getoooentries))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
ooo_entries_api_instance = asana.OooEntriesApi(api_client)
user = "12345" # str | Globally unique identifier for the user to filter OOO entries by.
workspace = "98765" # str | Globally unique identifier for the workspace.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'start_date': '2025-01-01', # date | An ISO 8601 date string. Filters to OOO entries that overlap with or end after this date.
    'end_date': '2025-12-31', # date | An ISO 8601 date string. Filters to OOO entries that overlap with or start before this date.
    'opt_fields': "created_by,created_by.name,end_date,offset,path,start_date,uri,user,user.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get OOO entries for a user
    api_response = ooo_entries_api_instance.get_ooo_entries(user, workspace, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling OooEntriesApi->get_ooo_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| Globally unique identifier for the user to filter OOO entries by. | 
 **workspace** | **str**| Globally unique identifier for the workspace. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **start_date** | **date**| An ISO 8601 date string. Filters to OOO entries that overlap with or end after this date. | [optional] 
 **end_date** | **date**| An ISO 8601 date string. Filters to OOO entries that overlap with or start before this date. | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_ooo_entry**

Get an OOO entry

<b>Required scope: </b><code>ooo_entries:read</code>  Returns the complete OOO entry record for a single OOO entry.

([more information](https://developers.asana.com/reference/getoooentry))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
ooo_entries_api_instance = asana.OooEntriesApi(api_client)
ooo_entry_gid = "12345" # str | Globally unique identifier for the OOO entry.
opts = {
    'opt_fields': "created_by,created_by.name,end_date,start_date,user,user.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get an OOO entry
    api_response = ooo_entries_api_instance.get_ooo_entry(ooo_entry_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OooEntriesApi->get_ooo_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ooo_entry_gid** | **str**| Globally unique identifier for the OOO entry. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_ooo_entry**

Update an OOO entry

<b>Required scope: </b><code>ooo_entries:write</code>  An existing OOO entry can be updated by making a PUT request on the URL for that OOO entry. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated OOO entry record.

([more information](https://developers.asana.com/reference/updateoooentry))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
ooo_entries_api_instance = asana.OooEntriesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The updated fields for the OOO entry.
ooo_entry_gid = "12345" # str | Globally unique identifier for the OOO entry.
opts = {
    'opt_fields': "created_by,created_by.name,end_date,start_date,user,user.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Update an OOO entry
    api_response = ooo_entries_api_instance.update_ooo_entry(body, ooo_entry_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OooEntriesApi->update_ooo_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The updated fields for the OOO entry. | 
 **ooo_entry_gid** | **str**| Globally unique identifier for the OOO entry. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

