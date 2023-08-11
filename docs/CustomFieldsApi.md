# asana.CustomFieldsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_field**](CustomFieldsApi.md#create_custom_field) | **POST** /custom_fields | Create a custom field
[**create_enum_option_for_custom_field**](CustomFieldsApi.md#create_enum_option_for_custom_field) | **POST** /custom_fields/{custom_field_gid}/enum_options | Create an enum option
[**delete_custom_field**](CustomFieldsApi.md#delete_custom_field) | **DELETE** /custom_fields/{custom_field_gid} | Delete a custom field
[**get_custom_field**](CustomFieldsApi.md#get_custom_field) | **GET** /custom_fields/{custom_field_gid} | Get a custom field
[**get_custom_fields_for_workspace**](CustomFieldsApi.md#get_custom_fields_for_workspace) | **GET** /workspaces/{workspace_gid}/custom_fields | Get a workspace&#x27;s custom fields
[**insert_enum_option_for_custom_field**](CustomFieldsApi.md#insert_enum_option_for_custom_field) | **POST** /custom_fields/{custom_field_gid}/enum_options/insert | Reorder a custom field&#x27;s enum
[**update_custom_field**](CustomFieldsApi.md#update_custom_field) | **PUT** /custom_fields/{custom_field_gid} | Update a custom field
[**update_enum_option**](CustomFieldsApi.md#update_enum_option) | **PUT** /enum_options/{enum_option_gid} | Update an enum option

# **create_custom_field**
> CustomFieldResponseData create_custom_field(body, opt_fields=opt_fields)

Create a custom field

Creates a new custom field in a workspace. Every custom field is required to be created in a specific workspace, and this workspace cannot be changed once set.  A custom field’s name must be unique within a workspace and not conflict with names of existing task properties such as `Due Date` or `Assignee`. A custom field’s type must be one of `text`, `enum`, `multi_enum`, `number`, `date`, or `people`.  Returns the full record of the newly created custom field.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.CustomFieldsApi(api_client)
body = asana.CustomFieldsBody({"param1": "value1", "param2": "value2",}) # CustomFieldsBody | The custom field object to create.
opt_fields = ["asana_created_field","created_by","created_by.name","currency_code","custom_label","custom_label_position","date_value","date_value.date","date_value.date_time","description","display_value","enabled","enum_options","enum_options.color","enum_options.enabled","enum_options.name","enum_value","enum_value.color","enum_value.enabled","enum_value.name","format","has_notifications_enabled","is_formula_field","is_global_to_workspace","is_value_read_only","multi_enum_values","multi_enum_values.color","multi_enum_values.enabled","multi_enum_values.name","name","number_value","people_value","people_value.name","precision","resource_subtype","text_value","type"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Create a custom field
    api_response = api_instance.create_custom_field(body, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->create_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomFieldsBody**](CustomFieldsBody.md)| The custom field object to create. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CustomFieldResponseData**](CustomFieldResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_enum_option_for_custom_field**
> EnumOptionData create_enum_option_for_custom_field(custom_field_gid, body=body, opt_fields=opt_fields)

Create an enum option

Creates an enum option and adds it to this custom field’s list of enum options. A custom field can have at most 500 enum options (including disabled options). By default new enum options are inserted at the end of a custom field’s list. Locked custom fields can only have enum options added by the user who locked the field. Returns the full record of the newly created enum option.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.CustomFieldsApi(api_client)
custom_field_gid = '12345' # str | Globally unique identifier for the custom field.
body = asana.CustomFieldGidEnumOptionsBody({"param1": "value1", "param2": "value2",}) # CustomFieldGidEnumOptionsBody | The enum option object to create. (optional)
opt_fields = ["color","enabled","name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Create an enum option
    api_response = api_instance.create_enum_option_for_custom_field(custom_field_gid, body=body, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->create_enum_option_for_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_gid** | **str**| Globally unique identifier for the custom field. | 
 **body** | [**CustomFieldGidEnumOptionsBody**](CustomFieldGidEnumOptionsBody.md)| The enum option object to create. | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**EnumOptionData**](EnumOptionData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field**
> EmptyResponseData delete_custom_field(custom_field_gid)

Delete a custom field

A specific, existing custom field can be deleted by making a DELETE request on the URL for that custom field. Locked custom fields can only be deleted by the user who locked the field. Returns an empty data record.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.CustomFieldsApi(api_client)
custom_field_gid = '12345' # str | Globally unique identifier for the custom field.

try:
    # Delete a custom field
    api_response = api_instance.delete_custom_field(custom_field_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->delete_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_gid** | **str**| Globally unique identifier for the custom field. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field**
> CustomFieldResponseData get_custom_field(custom_field_gid, opt_fields=opt_fields)

Get a custom field

Get the complete definition of a custom field’s metadata.  Since custom fields can be defined for one of a number of types, and these types have different data and behaviors, there are fields that are relevant to a particular type. For instance, as noted above, enum_options is only relevant for the enum type and defines the set of choices that the enum could represent. The examples below show some of these type-specific custom field definitions.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.CustomFieldsApi(api_client)
custom_field_gid = '12345' # str | Globally unique identifier for the custom field.
opt_fields = ["asana_created_field","created_by","created_by.name","currency_code","custom_label","custom_label_position","date_value","date_value.date","date_value.date_time","description","display_value","enabled","enum_options","enum_options.color","enum_options.enabled","enum_options.name","enum_value","enum_value.color","enum_value.enabled","enum_value.name","format","has_notifications_enabled","is_formula_field","is_global_to_workspace","is_value_read_only","multi_enum_values","multi_enum_values.color","multi_enum_values.enabled","multi_enum_values.name","name","number_value","people_value","people_value.name","precision","resource_subtype","text_value","type"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a custom field
    api_response = api_instance.get_custom_field(custom_field_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->get_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_gid** | **str**| Globally unique identifier for the custom field. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CustomFieldResponseData**](CustomFieldResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_fields_for_workspace**
> CustomFieldResponseArray get_custom_fields_for_workspace(workspace_gid, limit=limit, offset=offset, opt_fields=opt_fields)

Get a workspace's custom fields

Returns a list of the compact representation of all of the custom fields in a workspace.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.CustomFieldsApi(api_client)
workspace_gid = '12345' # str | Globally unique identifier for the workspace or organization.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["asana_created_field","created_by","created_by.name","currency_code","custom_label","custom_label_position","date_value","date_value.date","date_value.date_time","description","display_value","enabled","enum_options","enum_options.color","enum_options.enabled","enum_options.name","enum_value","enum_value.color","enum_value.enabled","enum_value.name","format","has_notifications_enabled","is_formula_field","is_global_to_workspace","is_value_read_only","multi_enum_values","multi_enum_values.color","multi_enum_values.enabled","multi_enum_values.name","name","number_value","offset","path","people_value","people_value.name","precision","resource_subtype","text_value","type","uri"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a workspace's custom fields
    api_response = api_instance.get_custom_fields_for_workspace(workspace_gid, limit=limit, offset=offset, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->get_custom_fields_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CustomFieldResponseArray**](CustomFieldResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_enum_option_for_custom_field**
> EnumOptionData insert_enum_option_for_custom_field(custom_field_gid, body=body, opt_fields=opt_fields)

Reorder a custom field's enum

Moves a particular enum option to be either before or after another specified enum option in the custom field. Locked custom fields can only be reordered by the user who locked the field.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.CustomFieldsApi(api_client)
custom_field_gid = '12345' # str | Globally unique identifier for the custom field.
body = asana.EnumOptionsInsertBody({"param1": "value1", "param2": "value2",}) # EnumOptionsInsertBody | The enum option object to create. (optional)
opt_fields = ["color","enabled","name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Reorder a custom field's enum
    api_response = api_instance.insert_enum_option_for_custom_field(custom_field_gid, body=body, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->insert_enum_option_for_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_gid** | **str**| Globally unique identifier for the custom field. | 
 **body** | [**EnumOptionsInsertBody**](EnumOptionsInsertBody.md)| The enum option object to create. | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**EnumOptionData**](EnumOptionData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field**
> CustomFieldResponseData update_custom_field(custom_field_gid, body=body, opt_fields=opt_fields)

Update a custom field

A specific, existing custom field can be updated by making a PUT request on the URL for that custom field. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the custom field. A custom field’s `type` cannot be updated. An enum custom field’s `enum_options` cannot be updated with this endpoint. Instead see “Work With Enum Options” for information on how to update `enum_options`. Locked custom fields can only be updated by the user who locked the field. Returns the complete updated custom field record.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.CustomFieldsApi(api_client)
custom_field_gid = '12345' # str | Globally unique identifier for the custom field.
body = asana.CustomFieldsCustomFieldGidBody({"param1": "value1", "param2": "value2",}) # CustomFieldsCustomFieldGidBody | The custom field object with all updated properties. (optional)
opt_fields = ["asana_created_field","created_by","created_by.name","currency_code","custom_label","custom_label_position","date_value","date_value.date","date_value.date_time","description","display_value","enabled","enum_options","enum_options.color","enum_options.enabled","enum_options.name","enum_value","enum_value.color","enum_value.enabled","enum_value.name","format","has_notifications_enabled","is_formula_field","is_global_to_workspace","is_value_read_only","multi_enum_values","multi_enum_values.color","multi_enum_values.enabled","multi_enum_values.name","name","number_value","people_value","people_value.name","precision","resource_subtype","text_value","type"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Update a custom field
    api_response = api_instance.update_custom_field(custom_field_gid, body=body, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->update_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_field_gid** | **str**| Globally unique identifier for the custom field. | 
 **body** | [**CustomFieldsCustomFieldGidBody**](CustomFieldsCustomFieldGidBody.md)| The custom field object with all updated properties. | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CustomFieldResponseData**](CustomFieldResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_enum_option**
> EnumOptionData update_enum_option(enum_option_gid, body=body, opt_fields=opt_fields)

Update an enum option

Updates an existing enum option. Enum custom fields require at least one enabled enum option. Locked custom fields can only be updated by the user who locked the field. Returns the full record of the updated enum option.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
api_instance = asana.CustomFieldsApi(api_client)
enum_option_gid = '124578' # str | Globally unique identifier for the enum option.
body = asana.EnumOptionsEnumOptionGidBody({"param1": "value1", "param2": "value2",}) # EnumOptionsEnumOptionGidBody | The enum option object to update (optional)
opt_fields = ["color","enabled","name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Update an enum option
    api_response = api_instance.update_enum_option(enum_option_gid, body=body, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldsApi->update_enum_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enum_option_gid** | **str**| Globally unique identifier for the enum option. | 
 **body** | [**EnumOptionsEnumOptionGidBody**](EnumOptionsEnumOptionGidBody.md)| The enum option object to update | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**EnumOptionData**](EnumOptionData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

