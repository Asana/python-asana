# asana.WebhooksApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /webhooks | Establish a webhook
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{webhook_gid} | Delete a webhook
[**get_webhook**](WebhooksApi.md#get_webhook) | **GET** /webhooks/{webhook_gid} | Get a webhook
[**get_webhooks**](WebhooksApi.md#get_webhooks) | **GET** /webhooks | Get multiple webhooks
[**update_webhook**](WebhooksApi.md#update_webhook) | **PUT** /webhooks/{webhook_gid} | Update a webhook

# **create_webhook**
> WebhookResponseData create_webhook(body, opt_fields=opt_fields)

Establish a webhook

Establishing a webhook is a two-part process. First, a simple HTTP POST request initiates the creation similar to creating any other resource.  Next, in the middle of this request comes the confirmation handshake. When a webhook is created, we will send a test POST to the target with an `X-Hook-Secret` header. The target must respond with a `200 OK` or `204 No Content` and a matching `X-Hook-Secret` header to confirm that this webhook subscription is indeed expected. We strongly recommend storing this secret to be used to verify future webhook event signatures.  The POST request to create the webhook will then return with the status of the request. If you do not acknowledge the webhook’s confirmation handshake it will fail to setup, and you will receive an error in response to your attempt to create it. This means you need to be able to receive and complete the webhook *while* the POST request is in-flight (in other words, have a server that can handle requests asynchronously).  Invalid hostnames like localhost will recieve a 403 Forbidden status code.  ``` # Request curl -H \"Authorization: Bearer <personal_access_token>\" \\ -X POST https://app.asana.com/api/1.0/webhooks \\ -d \"resource=8675309\" \\ -d \"target=https://example.com/receive-webhook/7654\" ```  ``` # Handshake sent to https://example.com/ POST /receive-webhook/7654 X-Hook-Secret: b537207f20cbfa02357cf448134da559e8bd39d61597dcd5631b8012eae53e81 ```  ``` # Handshake response sent by example.com HTTP/1.1 200 X-Hook-Secret: b537207f20cbfa02357cf448134da559e8bd39d61597dcd5631b8012eae53e81 ```  ``` # Response HTTP/1.1 201 {   \"data\": {     \"gid\": \"43214\",     \"resource\": {       \"gid\": \"8675309\",       \"name\": \"Bugs\"     },     \"target\": \"https://example.com/receive-webhook/7654\",     \"active\": false,     \"last_success_at\": null,     \"last_failure_at\": null,     \"last_failure_content\": null   } } ```

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.WebhooksApi(asana.ApiClient(configuration))
body = asana.WebhooksBody({"param1": "value1", "param2": "value2",}) # WebhooksBody | The webhook workspace and target.
opt_fields = ["active","created_at","filters","filters.action","filters.fields","filters.resource_subtype","last_failure_at","last_failure_content","last_success_at","resource","resource.name","target"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Establish a webhook
  api_response = api_instance.create_webhook(body, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhooksBody**](WebhooksBody.md)| The webhook workspace and target. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**WebhookResponseData**](WebhookResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> EmptyResponseData delete_webhook(webhook_gid)

Delete a webhook

This method *permanently* removes a webhook. Note that it may be possible to receive a request that was already in flight after deleting the webhook, but no further requests will be issued.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.WebhooksApi(asana.ApiClient(configuration))
webhook_gid = '12345' # str | Globally unique identifier for the webhook.

try:
  # Delete a webhook
  api_response = api_instance.delete_webhook(webhook_gid)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_gid** | **str**| Globally unique identifier for the webhook. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> WebhookResponseData get_webhook(webhook_gid, opt_fields=opt_fields)

Get a webhook

Returns the full record for the given webhook.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.WebhooksApi(asana.ApiClient(configuration))
webhook_gid = '12345' # str | Globally unique identifier for the webhook.
opt_fields = ["active","created_at","filters","filters.action","filters.fields","filters.resource_subtype","last_failure_at","last_failure_content","last_success_at","resource","resource.name","target"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get a webhook
  api_response = api_instance.get_webhook(webhook_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling WebhooksApi->get_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_gid** | **str**| Globally unique identifier for the webhook. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**WebhookResponseData**](WebhookResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**
> WebhookResponseArray get_webhooks(workspace, limit=limit, offset=offset, resource=resource, opt_fields=opt_fields)

Get multiple webhooks

Get the compact representation of all webhooks your app has registered for the authenticated user in the given workspace.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.WebhooksApi(asana.ApiClient(configuration))
workspace = '1331' # str | The workspace to query for webhooks in.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
resource = '51648' # str | Only return webhooks for the given resource. (optional)
opt_fields = ["active","created_at","filters","filters.action","filters.fields","filters.resource_subtype","last_failure_at","last_failure_content","last_success_at","offset","path","resource","resource.name","target","uri"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get multiple webhooks
  api_response = api_instance.get_webhooks(workspace, limit=limit, offset=offset, resource=resource, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling WebhooksApi->get_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace to query for webhooks in. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **resource** | **str**| Only return webhooks for the given resource. | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**WebhookResponseArray**](WebhookResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> WebhookResponseData update_webhook(body, webhook_gid, opt_fields=opt_fields)

Update a webhook

An existing webhook's filters can be updated by making a PUT request on the URL for that webhook. Note that the webhook's previous `filters` array will be completely overwritten by the `filters` sent in the PUT request.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.WebhooksApi(asana.ApiClient(configuration))
body = asana.WebhooksWebhookGidBody({"param1": "value1", "param2": "value2",}) # WebhooksWebhookGidBody | The updated filters for the webhook.
webhook_gid = '12345' # str | Globally unique identifier for the webhook.
opt_fields = ["active","created_at","filters","filters.action","filters.fields","filters.resource_subtype","last_failure_at","last_failure_content","last_success_at","resource","resource.name","target"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Update a webhook
  api_response = api_instance.update_webhook(body, webhook_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhooksWebhookGidBody**](WebhooksWebhookGidBody.md)| The updated filters for the webhook. | 
 **webhook_gid** | **str**| Globally unique identifier for the webhook. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**WebhookResponseData**](WebhookResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

