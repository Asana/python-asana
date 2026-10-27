# asana.TablesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_field_setting_for_table**](TablesApi.md#add_custom_field_setting_for_table) | **POST** /tables/{table_gid}/addCustomFieldSetting | Add a custom field to a table
[**create_table**](TablesApi.md#create_table) | **POST** /tables | Create a table
[**delete_table**](TablesApi.md#delete_table) | **DELETE** /tables/{table_gid} | Delete a table
[**get_custom_field_settings_for_table**](TablesApi.md#get_custom_field_settings_for_table) | **GET** /tables/{table_gid}/custom_field_settings | Get a table&#x27;s custom field settings
[**get_custom_field_settings_for_table_legacy**](TablesApi.md#get_custom_field_settings_for_table_legacy) | **GET** /tables/{table_gid}/getCustomFieldSettings | Get a table&#x27;s custom field settings
[**get_table**](TablesApi.md#get_table) | **GET** /tables/{table_gid} | Get a table
[**get_tables_for_workspace**](TablesApi.md#get_tables_for_workspace) | **GET** /workspaces/{workspace_gid}/tables | Get tables in a workspace
[**remove_custom_field_setting_for_table**](TablesApi.md#remove_custom_field_setting_for_table) | **POST** /tables/{table_gid}/removeCustomFieldSetting | Remove a custom field from a table
[**update_table**](TablesApi.md#update_table) | **PUT** /tables/{table_gid} | Update a table

# **add_custom_field_setting_for_table**

Add a custom field to a table

<b>Required scope: </b><code>tables:write</code>  Custom fields are associated with tables by way of custom field settings. This method creates a setting for the table. Unlike projects and portfolios, tables only support custom fields that are global (published) to the workspace. Reusing a non-global custom field, or creating a new field inline that isn't global, will fail with a `403 Forbidden` error.

([more information](https://developers.asana.com/reference/addcustomfieldsettingfortable))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tables_api_instance = asana.TablesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | Information about the custom field setting.
table_gid = "1337" # str | Globally unique identifier for the table.
opts = {
    'opt_fields': "custom_field,custom_field.date_value,custom_field.date_value.date,custom_field.date_value.date_time,custom_field.display_value,custom_field.enabled,custom_field.enum_options,custom_field.enum_options.color,custom_field.enum_options.enabled,custom_field.enum_options.name,custom_field.enum_value,custom_field.enum_value.color,custom_field.enum_value.enabled,custom_field.enum_value.name,custom_field.id_prefix,custom_field.input_restrictions,custom_field.is_formula_field,custom_field.is_lookup_field,custom_field.multi_enum_values,custom_field.multi_enum_values.color,custom_field.multi_enum_values.enabled,custom_field.multi_enum_values.name,custom_field.name,custom_field.number_value,custom_field.representation_type,custom_field.text_value,custom_field.type,is_important", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Add a custom field to a table
    api_response = tables_api_instance.add_custom_field_setting_for_table(body, table_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TablesApi->add_custom_field_setting_for_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| Information about the custom field setting. | 
 **table_gid** | **str**| Globally unique identifier for the table. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **create_table**

Create a table

<b>Required scope: </b><code>tables:write</code>  Creates a new table in a workspace.  Returns the full record of the newly created table.

([more information](https://developers.asana.com/reference/createtable))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tables_api_instance = asana.TablesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The table to create.
opts = {
    'opt_fields': "created_at,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_lookup_field,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,modified_at,name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Create a table
    api_response = tables_api_instance.create_table(body, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TablesApi->create_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The table to create. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_table**

Delete a table

<b>Required scope: </b><code>tables:delete</code>  A specific, existing table can be deleted by making a DELETE request on the URL for that table.  Returns an empty data record.

([more information](https://developers.asana.com/reference/deletetable))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tables_api_instance = asana.TablesApi(api_client)
table_gid = "1337" # str | Globally unique identifier for the table.


try:
    # Delete a table
    api_response = tables_api_instance.delete_table(table_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TablesApi->delete_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_gid** | **str**| Globally unique identifier for the table. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_custom_field_settings_for_table**

Get a table&#x27;s custom field settings

<b>Required scope: </b><code>tables:read</code>  Returns a paginated list of the custom field settings for the given table.

([more information](https://developers.asana.com/reference/getcustomfieldsettingsfortable))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tables_api_instance = asana.TablesApi(api_client)
table_gid = "1337" # str | Globally unique identifier for the table.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "custom_field,custom_field.date_value,custom_field.date_value.date,custom_field.date_value.date_time,custom_field.display_value,custom_field.enabled,custom_field.enum_options,custom_field.enum_options.color,custom_field.enum_options.enabled,custom_field.enum_options.name,custom_field.enum_value,custom_field.enum_value.color,custom_field.enum_value.enabled,custom_field.enum_value.name,custom_field.id_prefix,custom_field.input_restrictions,custom_field.is_formula_field,custom_field.is_lookup_field,custom_field.multi_enum_values,custom_field.multi_enum_values.color,custom_field.multi_enum_values.enabled,custom_field.multi_enum_values.name,custom_field.name,custom_field.number_value,custom_field.representation_type,custom_field.text_value,custom_field.type,is_important,offset,path,uri", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Get a table's custom field settings
    api_response = tables_api_instance.get_custom_field_settings_for_table(table_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling TablesApi->get_custom_field_settings_for_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_gid** | **str**| Globally unique identifier for the table. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_custom_field_settings_for_table_legacy**

Get a table&#x27;s custom field settings

<b>Required scope: </b><code>tables:read</code>  Returns a paginated list of the custom field settings for the given table.  Deprecated in favor of [Get a table's custom field settings](/reference/getcustomfieldsettingsfortable), which is otherwise identical. Kept for existing callers; new integrations should use the other endpoint instead.

([more information](https://developers.asana.com/reference/getcustomfieldsettingsfortablelegacy))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tables_api_instance = asana.TablesApi(api_client)
table_gid = "1337" # str | Globally unique identifier for the table.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "custom_field,custom_field.date_value,custom_field.date_value.date,custom_field.date_value.date_time,custom_field.display_value,custom_field.enabled,custom_field.enum_options,custom_field.enum_options.color,custom_field.enum_options.enabled,custom_field.enum_options.name,custom_field.enum_value,custom_field.enum_value.color,custom_field.enum_value.enabled,custom_field.enum_value.name,custom_field.id_prefix,custom_field.input_restrictions,custom_field.is_formula_field,custom_field.is_lookup_field,custom_field.multi_enum_values,custom_field.multi_enum_values.color,custom_field.multi_enum_values.enabled,custom_field.multi_enum_values.name,custom_field.name,custom_field.number_value,custom_field.representation_type,custom_field.text_value,custom_field.type,is_important,offset,path,uri", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Get a table's custom field settings
    api_response = tables_api_instance.get_custom_field_settings_for_table_legacy(table_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling TablesApi->get_custom_field_settings_for_table_legacy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_gid** | **str**| Globally unique identifier for the table. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_table**

Get a table

<b>Required scope: </b><code>tables:read</code>  Returns the complete table record for a single table.

([more information](https://developers.asana.com/reference/gettable))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tables_api_instance = asana.TablesApi(api_client)
table_gid = "1337" # str | Globally unique identifier for the table.
opts = {
    'opt_fields': "created_at,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_lookup_field,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,modified_at,name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Get a table
    api_response = tables_api_instance.get_table(table_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TablesApi->get_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_gid** | **str**| Globally unique identifier for the table. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_tables_for_workspace**

Get tables in a workspace

<b>Required scope: </b><code>tables:read</code>  Returns the compact table records for all tables in the given workspace.

([more information](https://developers.asana.com/reference/gettablesforworkspace))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tables_api_instance = asana.TablesApi(api_client)
workspace_gid = "12345" # str | Globally unique identifier for the workspace or organization.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "created_at,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_lookup_field,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,modified_at,name,offset,path,uri,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Get tables in a workspace
    api_response = tables_api_instance.get_tables_for_workspace(workspace_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling TablesApi->get_tables_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **remove_custom_field_setting_for_table**

Remove a custom field from a table

<b>Required scope: </b><code>tables:write</code>  Removes a custom field setting from a table.

([more information](https://developers.asana.com/reference/removecustomfieldsettingfortable))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tables_api_instance = asana.TablesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | Information about the custom field setting being removed.
table_gid = "1337" # str | Globally unique identifier for the table.


try:
    # Remove a custom field from a table
    api_response = tables_api_instance.remove_custom_field_setting_for_table(body, table_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TablesApi->remove_custom_field_setting_for_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| Information about the custom field setting being removed. | 
 **table_gid** | **str**| Globally unique identifier for the table. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_table**

Update a table

<b>Required scope: </b><code>tables:write</code>  A specific, existing table can be updated by making a PUT request on the URL for that table. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated table record.

([more information](https://developers.asana.com/reference/updatetable))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
tables_api_instance = asana.TablesApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The updated fields for the table.
table_gid = "1337" # str | Globally unique identifier for the table.
opts = {
    'opt_fields': "created_at,custom_field_settings,custom_field_settings.custom_field,custom_field_settings.custom_field.date_value,custom_field_settings.custom_field.date_value.date,custom_field_settings.custom_field.date_value.date_time,custom_field_settings.custom_field.display_value,custom_field_settings.custom_field.enabled,custom_field_settings.custom_field.enum_options,custom_field_settings.custom_field.enum_options.color,custom_field_settings.custom_field.enum_options.enabled,custom_field_settings.custom_field.enum_options.name,custom_field_settings.custom_field.enum_value,custom_field_settings.custom_field.enum_value.color,custom_field_settings.custom_field.enum_value.enabled,custom_field_settings.custom_field.enum_value.name,custom_field_settings.custom_field.id_prefix,custom_field_settings.custom_field.input_restrictions,custom_field_settings.custom_field.is_formula_field,custom_field_settings.custom_field.is_lookup_field,custom_field_settings.custom_field.multi_enum_values,custom_field_settings.custom_field.multi_enum_values.color,custom_field_settings.custom_field.multi_enum_values.enabled,custom_field_settings.custom_field.multi_enum_values.name,custom_field_settings.custom_field.name,custom_field_settings.custom_field.number_value,custom_field_settings.custom_field.representation_type,custom_field_settings.custom_field.text_value,custom_field_settings.custom_field.type,custom_field_settings.is_important,modified_at,name,workspace,workspace.name", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields).
}

try:
    # Update a table
    api_response = tables_api_instance.update_table(body, table_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TablesApi->update_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The updated fields for the table. | 
 **table_gid** | **str**| Globally unique identifier for the table. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. Properties can include nested fields. To learn more, see the [input/output options guide](/docs/inputoutput-options#selecting-nested-fields). | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

