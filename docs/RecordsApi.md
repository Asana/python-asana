# asana.RecordsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_record**](RecordsApi.md#create_record) | **POST** /records | Create a record
[**delete_record**](RecordsApi.md#delete_record) | **DELETE** /records/{record_gid} | Delete a record
[**get_record**](RecordsApi.md#get_record) | **GET** /records/{record_gid} | Get a record
[**get_records_for_table**](RecordsApi.md#get_records_for_table) | **GET** /tables/{table_gid}/records | Get records in a table
[**search_records_for_workspace**](RecordsApi.md#search_records_for_workspace) | **GET** /workspaces/{workspace_gid}/records/search | Search records in a workspace
[**update_record**](RecordsApi.md#update_record) | **PUT** /records/{record_gid} | Update a record

# **create_record**

Create a record

<b>Required scope: </b><code>records:write</code>  Creates a new record in a table.  Returns the full record of the newly created record.

([more information](https://developers.asana.com/reference/createrecord))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
records_api_instance = asana.RecordsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The record to create.
opts = {
    'opt_fields': "comment_count,created_at,created_by,created_by.name,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.default_access_level,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.html_text_value,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_lookup_field,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.privacy_setting,custom_fields.reference_value,custom_fields.reference_value.name,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,deleted_at,is_in_archived_table,modified_at,name,permalink_url,table,table.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Create a record
    api_response = records_api_instance.create_record(body, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->create_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The record to create. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_record**

Delete a record

<b>Required scope: </b><code>records:delete</code>  A specific, existing record can be deleted by making a DELETE request on the URL for that record.  Returns an empty data record.

([more information](https://developers.asana.com/reference/deleterecord))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
records_api_instance = asana.RecordsApi(api_client)
record_gid = "7331" # str | Globally unique identifier for the record.


try:
    # Delete a record
    api_response = records_api_instance.delete_record(record_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->delete_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_gid** | **str**| Globally unique identifier for the record. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_record**

Get a record

<b>Required scope: </b><code>records:read</code>  Returns the complete record for a single record.

([more information](https://developers.asana.com/reference/getrecord))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
records_api_instance = asana.RecordsApi(api_client)
record_gid = "7331" # str | Globally unique identifier for the record.
opts = {
    'opt_fields': "comment_count,created_at,created_by,created_by.name,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.default_access_level,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.html_text_value,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_lookup_field,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.privacy_setting,custom_fields.reference_value,custom_fields.reference_value.name,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,deleted_at,is_in_archived_table,modified_at,name,permalink_url,table,table.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Get a record
    api_response = records_api_instance.get_record(record_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->get_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_gid** | **str**| Globally unique identifier for the record. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_records_for_table**

Get records in a table

<b>Required scope: </b><code>records:read</code>  Returns the compact records for all records in the given table.

([more information](https://developers.asana.com/reference/getrecordsfortable))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
records_api_instance = asana.RecordsApi(api_client)
table_gid = "1337" # str | Globally unique identifier for the table.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'modified_since': '2012-02-22T02:06:58.147Z', # datetime | Only return records that have been modified since the given time.
    'sort_by': "created_at", # str | Sort order for the records returned. If omitted, records are returned in their default order.
    'opt_fields': "comment_count,created_at,created_by,created_by.name,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.default_access_level,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.html_text_value,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_lookup_field,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.privacy_setting,custom_fields.reference_value,custom_fields.reference_value.name,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,deleted_at,is_in_archived_table,modified_at,name,offset,path,permalink_url,table,table.name,uri,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Get records in a table
    api_response = records_api_instance.get_records_for_table(table_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling RecordsApi->get_records_for_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_gid** | **str**| Globally unique identifier for the table. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **modified_since** | **datetime**| Only return records that have been modified since the given time. | [optional] 
 **sort_by** | **str**| Sort order for the records returned. If omitted, records are returned in their default order. | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **search_records_for_workspace**

Search records in a workspace

<b>Required scope: </b><code>records:read</code>  To mirror the functionality of the Asana web app's advanced search feature, this endpoint allows you to build complex filters to find and retrieve records across all of a workspace's tables. Custom field filters are also supported, using the same `custom_fields.{gid}.*` query parameters documented for [task search](/reference/searchtasksforworkspace). #### Premium access Like task search, this endpoint is only available to premium Asana users. Making a search request using credentials of a non-premium user will result in a `402 Payment Required` error. #### Pagination Search results are not stable; repeating the same query multiple times may return the data in a different order, even if the data do not change. Page sizes are limited to a maximum of 100 items, and can be specified by the `limit` query parameter. #### Eventual consistency Changes in Asana are forwarded to our search infrastructure to be indexed, which can take between 10 and 60 seconds to complete under normal operation. If you need read-your-write behavior, use [Get records in a table](/reference/getrecordsfortable) instead.

([more information](https://developers.asana.com/reference/searchrecordsforworkspace))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
records_api_instance = asana.RecordsApi(api_client)
workspace_gid = "12345" # str | Globally unique identifier for the workspace or organization.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'text': "Renewal", # str | Performs full-text search on the record name
    'teams.any': "12345,23456,34567", # str | Comma-separated list of team IDs
    'followers.any': "12345,23456,34567", # str | Comma-separated list of user identifiers. This can either be the string \"me\", an email, or the gid of a user.
    'followers.not': "12345,23456,34567", # str | Comma-separated list of user identifiers. This can either be the string \"me\", an email, or the gid of a user.
    'tables.any': "12345,23456,34567", # str | Comma-separated list of table IDs
    'tables.not': "12345,23456,34567", # str | Comma-separated list of table IDs
    'tables.all': "12345,23456,34567", # str | Comma-separated list of table IDs
    'created_on.before': '2019-09-15', # date | ISO 8601 date string
    'created_on.after': '2019-09-15', # date | ISO 8601 date string
    'created_on': '2019-09-15', # date | ISO 8601 date string or `null`
    'created_at.before': '2019-04-15T01:01:46.055Z', # datetime | ISO 8601 datetime string
    'created_at.after': '2019-04-15T01:01:46.055Z', # datetime | ISO 8601 datetime string
    'sort_by': "modified_at", # str | One of `created_at` or `modified_at`, defaults to `modified_at`
    'sort_ascending': True, # bool | Default `false`
    'opt_fields': "comment_count,created_at,created_by,created_by.name,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.default_access_level,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.html_text_value,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_lookup_field,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.privacy_setting,custom_fields.reference_value,custom_fields.reference_value.name,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,deleted_at,is_in_archived_table,modified_at,name,permalink_url,table,table.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Search records in a workspace
    api_response = records_api_instance.search_records_for_workspace(workspace_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling RecordsApi->search_records_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **text** | **str**| Performs full-text search on the record name | [optional] 
 **teams.any** | **str**| Comma-separated list of team IDs | [optional] 
 **followers.any** | **str**| Comma-separated list of user identifiers. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 
 **followers.not** | **str**| Comma-separated list of user identifiers. This can either be the string \&quot;me\&quot;, an email, or the gid of a user. | [optional] 
 **tables.any** | **str**| Comma-separated list of table IDs | [optional] 
 **tables.not** | **str**| Comma-separated list of table IDs | [optional] 
 **tables.all** | **str**| Comma-separated list of table IDs | [optional] 
 **created_on.before** | **date**| ISO 8601 date string | [optional] 
 **created_on.after** | **date**| ISO 8601 date string | [optional] 
 **created_on** | **date**| ISO 8601 date string or &#x60;null&#x60; | [optional] 
 **created_at.before** | **datetime**| ISO 8601 datetime string | [optional] 
 **created_at.after** | **datetime**| ISO 8601 datetime string | [optional] 
 **sort_by** | **str**| One of &#x60;created_at&#x60; or &#x60;modified_at&#x60;, defaults to &#x60;modified_at&#x60; | [optional] [default to modified_at]
 **sort_ascending** | **bool**| Default &#x60;false&#x60; | [optional] [default to false]
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_record**

Update a record

<b>Required scope: </b><code>records:write</code>  A specific, existing record can be updated by making a PUT request on the URL for that record. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated record.

([more information](https://developers.asana.com/reference/updaterecord))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
records_api_instance = asana.RecordsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The updated fields for the record.
record_gid = "7331" # str | Globally unique identifier for the record.
opts = {
    'opt_fields': "comment_count,created_at,created_by,created_by.name,custom_fields,custom_fields.asana_created_field,custom_fields.created_by,custom_fields.created_by.name,custom_fields.currency_code,custom_fields.custom_label,custom_fields.custom_label_position,custom_fields.date_value,custom_fields.date_value.date,custom_fields.date_value.date_time,custom_fields.default_access_level,custom_fields.description,custom_fields.display_value,custom_fields.enabled,custom_fields.enum_options,custom_fields.enum_options.color,custom_fields.enum_options.enabled,custom_fields.enum_options.name,custom_fields.enum_value,custom_fields.enum_value.color,custom_fields.enum_value.enabled,custom_fields.enum_value.name,custom_fields.format,custom_fields.has_notifications_enabled,custom_fields.html_text_value,custom_fields.id_prefix,custom_fields.input_restrictions,custom_fields.is_formula_field,custom_fields.is_global_to_workspace,custom_fields.is_lookup_field,custom_fields.is_value_read_only,custom_fields.multi_enum_values,custom_fields.multi_enum_values.color,custom_fields.multi_enum_values.enabled,custom_fields.multi_enum_values.name,custom_fields.name,custom_fields.number_value,custom_fields.people_value,custom_fields.people_value.name,custom_fields.precision,custom_fields.privacy_setting,custom_fields.reference_value,custom_fields.reference_value.name,custom_fields.representation_type,custom_fields.resource_subtype,custom_fields.text_value,custom_fields.type,deleted_at,is_in_archived_table,modified_at,name,permalink_url,table,table.name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Update a record
    api_response = records_api_instance.update_record(body, record_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->update_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The updated fields for the record. | 
 **record_gid** | **str**| Globally unique identifier for the record. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

