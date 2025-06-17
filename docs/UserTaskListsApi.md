# asana.UserTaskListsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_task_list**](UserTaskListsApi.md#get_user_task_list) | **GET** /user_task_lists/{user_task_list_gid} | Get a user task list
[**get_user_task_list_for_user**](UserTaskListsApi.md#get_user_task_list_for_user) | **GET** /users/{user_gid}/user_task_list | Get a user&#x27;s task list

# **get_user_task_list**

Get a user task list

<b>Required scope: </b><code>tasks:read</code>  Returns the full record for a user task list.

([more information](https://developers.asana.com/reference/getusertasklist))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
user_task_lists_api_instance = asana.UserTaskListsApi(api_client)
user_task_list_gid = "12345" # str | Globally unique identifier for the user task list.
opts = {
    'opt_fields': "name,owner,workspace", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a user task list
    api_response = user_task_lists_api_instance.get_user_task_list(user_task_list_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTaskListsApi->get_user_task_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_task_list_gid** | **str**| Globally unique identifier for the user task list. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_user_task_list_for_user**

Get a user&#x27;s task list

<b>Required scope: </b><code>tasks:read</code>  Returns the full record for a user's task list.

([more information](https://developers.asana.com/reference/getusertasklistforuser))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
user_task_lists_api_instance = asana.UserTaskListsApi(api_client)
user_gid = "me" # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
workspace = "1234" # str | The workspace in which to get the user task list.
opts = {
    'opt_fields': "name,owner,workspace", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a user's task list
    api_response = user_task_lists_api_instance.get_user_task_list_for_user(user_gid, workspace, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTaskListsApi->get_user_task_list_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_gid** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | 
 **workspace** | **str**| The workspace in which to get the user task list. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

