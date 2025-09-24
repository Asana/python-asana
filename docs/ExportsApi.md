# asana.ExportsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_graph_export**](ExportsApi.md#create_graph_export) | **POST** /exports/graph | Initiate a graph export
[**create_resource_export**](ExportsApi.md#create_resource_export) | **POST** /exports/resource | Initiate a resource export

# **create_graph_export**

Initiate a graph export

Initiates a graph export job for a given parent object (goal, team, portfolio, or project). The export will be processed asynchronously. Once initiated, use the [jobs](/reference/getjob) endpoint to monitor progress.  **Export Caching:** When exporting more than 1,000 tasks, the results are cached for 4 hours. Any new export requests made within this 4-hour window will return the same cached results rather than generating a fresh export.

([more information](https://developers.asana.com/reference/creategraphexport))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
exports_api_instance = asana.ExportsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | A JSON payload specifying the parent object to export.


try:
    # Initiate a graph export
    api_response = exports_api_instance.create_graph_export(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->create_graph_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| A JSON payload specifying the parent object to export. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_resource_export**

Initiate a resource export

Initiates a bulk export of resources for a workspace. The export will be processed asynchronously. Once the export has been requested, its progress can be monitored using the [jobs](/reference/getjob) endpoint.  ## Supported resource types This endpoint currently supports exporting tasks, teams and messages within a workspace. Resources can be requested to be part of the export by providing the `export_request_parameters` parameter. The following resource types are supported:  ### Tasks: Tasks are formatted for exports with some differences from their documented [schema](/reference/tasks):   - `attachments` are included by default and returns an array of associated attachments.   - Attachment objects do not include `download_url` or `view_url`. The `attachments` [endpoint](/reference/attachment) should be queried for up-to-date URLs.   - `stories` are included by default and returns an array of comments and other changes made to a task  ### Teams: Teams are formatted for exports with these differences from their documented [schema](/reference/teams):   - `members` are included by default and returns an array of Users that are members of the team   - Filtering is not supported for teams.  ### Messages: The returned schema encompasses both default messages and status updates and is similar to the status update schema. The available fields for messages are:   - `gid` - The globally unique identifier for the message.   - `resource_type` - The type of resource, which is always \"message\".   - `resource_subtype` - Optional. The subtype of the message, which can be \"default\" or \"status_update\".   - `status_type` - The type associated with the status update. This can be one of: “on_track”, “at_risk”, “off_track”, “on_hold”, “complete”, “achieved”, “partial”, “missed”, “dropped”   - `created_by` - The user who created the message.   - `created_at` - The time at which this resource was created and sent available to other users.   - `modified_at` - The time at which this resource was last modified.   - `title` - The title of the message.   - `text` - The text content of the message.   - `html_notes` - The text content of the message with formatting as HTML. Not included by default. Can be included by using “fields” in the initial request.   - `num_likes` - The number of users who have liked this message.   - `likes` - An array of users who have liked this message.   - `stories` - Optional. Array of stories applied to the message.   - `attachments` - Optional. Array of attachments added to the message.   - `followers` - Optional. Array of users currently following the message. Users that were sent the message are treated as followers.   - `parents` - Array of objects the message was sent to. Can be a Project, Portfolio, Team or Goal. Limited to a single object for status updates.   ## Export file The final export file will be in JSON Lines format and compressed in a gzip container.  Objects are formatted according to their corresponding API schema, or limited to the fields included in the `fields` parameter. Exports currently include undeleted objects.  An object in the export will be up to date anywhere between the exports `created_at` and `completed_at`. There is no guaranteed ordering of objects in the export.  Access to the export file expires 30 days after its completion.  ## Exporting specific fields By default, each object in an export includes a predefined set of fields based on its schema. If a more limited set of fields or fields not included by default are required, the Export API allows for specifying which fields to include in the requested export.  Fields can be specified using the `fields` parameter. The fields parameter conforms to the fields optional parameter available for all Asana endpoints which is documented [here](https://developers.asana.com/docs/inputoutput-options).  Utilizing the `fields` parameter is recommended if the full object is not required, especially when a large number of objects are being exported, to reduce the overall export time.  ## Filtering resources A disjunction of two or more filters can be achieved by providing multiple `export_request_parameters` for the same resource, each with different filters. However, this approach may result in duplicate resources being returned.  ## Rate Limits A workspace is currently limited to *one* in progress export request at a given time. The request will return with a 403 Forbidden status code if the limit is exceeded.

([more information](https://developers.asana.com/reference/createresourceexport))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
exports_api_instance = asana.ExportsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | A JSON payload specifying the resources to export, including filters to apply and fields to be exported.


try:
    # Initiate a resource export
    api_response = exports_api_instance.create_resource_export(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->create_resource_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| A JSON payload specifying the resources to export, including filters to apply and fields to be exported. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

