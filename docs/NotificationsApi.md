# asana.NotificationsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_notifications_for_user**](NotificationsApi.md#get_notifications_for_user) | **GET** /users/{user_gid}/notifications | Get notifications for a user
[**mark_notifications_read_for_user**](NotificationsApi.md#mark_notifications_read_for_user) | **POST** /users/{user_gid}/notifications/markRead | Mark notifications as read
[**mark_notifications_unread_for_user**](NotificationsApi.md#mark_notifications_unread_for_user) | **POST** /users/{user_gid}/notifications/markUnread | Mark notifications as unread

# **get_notifications_for_user**

Get notifications for a user

<b>Required scope: </b><code>notifications:read</code>  Returns a paginated collection of active, unarchived notifications for the current user in newest-first Inbox order. A user may only list their own notifications. The default page size is 50 notifications.

([more information](https://developers.asana.com/reference/getnotificationsforuser))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
notifications_api_instance = asana.NotificationsApi(api_client)
user_gid = "me" # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
workspace = "31326" # str | GID of the workspace from which to return notifications.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "created_at,created_by,created_by.name,is_read,offset,path,priority_classification,story,story_resource_subtype,uri,work_objects,work_objects.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Get notifications for a user
    api_response = notifications_api_instance.get_notifications_for_user(user_gid, workspace, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling NotificationsApi->get_notifications_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_gid** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | 
 **workspace** | **str**| GID of the workspace from which to return notifications. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **mark_notifications_read_for_user**

Mark notifications as read

<b>Required scope: </b><code>notifications:write</code>  Marks only the given notifications as read for the authenticated user. A user may only mark their own notifications. GIDs that don't exist, don't belong to the caller, or have been deleted are reported in failed_gids rather than failing the whole request.

([more information](https://developers.asana.com/reference/marknotificationsreadforuser))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
notifications_api_instance = asana.NotificationsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | 
user_gid = "me" # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
opts = {
    'opt_fields': "failed_gids", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Mark notifications as read
    api_response = notifications_api_instance.mark_notifications_read_for_user(body, user_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->mark_notifications_read_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**|  | 
 **user_gid** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **mark_notifications_unread_for_user**

Mark notifications as unread

<b>Required scope: </b><code>notifications:write</code>  Marks only the given notifications as unread for the authenticated user. A notification that is archived is also unarchived and moves to the top of Inbox, matching the Inbox UI's unarchive action. Notifications already in Inbox keep their existing position. A user may only mark their own notifications. GIDs that don't exist, don't belong to the caller, or have been deleted are reported in failed_gids rather than failing the whole request.

([more information](https://developers.asana.com/reference/marknotificationsunreadforuser))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
notifications_api_instance = asana.NotificationsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | 
user_gid = "me" # str | A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
opts = {
    'opt_fields': "failed_gids", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Mark notifications as unread
    api_response = notifications_api_instance.mark_notifications_unread_for_user(body, user_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationsApi->mark_notifications_unread_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**|  | 
 **user_gid** | **str**| A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

