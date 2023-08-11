# asana.CustomFieldSettingsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_custom_field_settings_for_portfolio**](CustomFieldSettingsApi.md#get_custom_field_settings_for_portfolio) | **GET** /portfolios/{portfolio_gid}/custom_field_settings | Get a portfolio&#x27;s custom fields
[**get_custom_field_settings_for_project**](CustomFieldSettingsApi.md#get_custom_field_settings_for_project) | **GET** /projects/{project_gid}/custom_field_settings | Get a project&#x27;s custom fields

# **get_custom_field_settings_for_portfolio**
> CustomFieldSettingResponseArray get_custom_field_settings_for_portfolio(portfolio_gid, limit=limit, offset=offset, opt_fields=opt_fields)

Get a portfolio's custom fields

Returns a list of all of the custom fields settings on a portfolio, in compact form.

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
api_instance = asana.CustomFieldSettingsApi(api_client)
portfolio_gid = '12345' # str | Globally unique identifier for the portfolio.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["custom_field","custom_field.asana_created_field","custom_field.created_by","custom_field.created_by.name","custom_field.currency_code","custom_field.custom_label","custom_field.custom_label_position","custom_field.date_value","custom_field.date_value.date","custom_field.date_value.date_time","custom_field.description","custom_field.display_value","custom_field.enabled","custom_field.enum_options","custom_field.enum_options.color","custom_field.enum_options.enabled","custom_field.enum_options.name","custom_field.enum_value","custom_field.enum_value.color","custom_field.enum_value.enabled","custom_field.enum_value.name","custom_field.format","custom_field.has_notifications_enabled","custom_field.is_formula_field","custom_field.is_global_to_workspace","custom_field.is_value_read_only","custom_field.multi_enum_values","custom_field.multi_enum_values.color","custom_field.multi_enum_values.enabled","custom_field.multi_enum_values.name","custom_field.name","custom_field.number_value","custom_field.people_value","custom_field.people_value.name","custom_field.precision","custom_field.resource_subtype","custom_field.text_value","custom_field.type","is_important","offset","parent","parent.name","path","project","project.name","uri"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a portfolio's custom fields
    api_response = api_instance.get_custom_field_settings_for_portfolio(portfolio_gid, limit=limit, offset=offset, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldSettingsApi->get_custom_field_settings_for_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CustomFieldSettingResponseArray**](CustomFieldSettingResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field_settings_for_project**
> CustomFieldSettingResponseArray get_custom_field_settings_for_project(project_gid, limit=limit, offset=offset, opt_fields=opt_fields)

Get a project's custom fields

Returns a list of all of the custom fields settings on a project, in compact form. Note that, as in all queries to collections which return compact representation, `opt_fields` can be used to include more data than is returned in the compact representation. See the [documentation for input/output options](https://developers.asana.com/docs/inputoutput-options) for more information.

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
api_instance = asana.CustomFieldSettingsApi(api_client)
project_gid = '1331' # str | Globally unique identifier for the project.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["custom_field","custom_field.asana_created_field","custom_field.created_by","custom_field.created_by.name","custom_field.currency_code","custom_field.custom_label","custom_field.custom_label_position","custom_field.date_value","custom_field.date_value.date","custom_field.date_value.date_time","custom_field.description","custom_field.display_value","custom_field.enabled","custom_field.enum_options","custom_field.enum_options.color","custom_field.enum_options.enabled","custom_field.enum_options.name","custom_field.enum_value","custom_field.enum_value.color","custom_field.enum_value.enabled","custom_field.enum_value.name","custom_field.format","custom_field.has_notifications_enabled","custom_field.is_formula_field","custom_field.is_global_to_workspace","custom_field.is_value_read_only","custom_field.multi_enum_values","custom_field.multi_enum_values.color","custom_field.multi_enum_values.enabled","custom_field.multi_enum_values.name","custom_field.name","custom_field.number_value","custom_field.people_value","custom_field.people_value.name","custom_field.precision","custom_field.resource_subtype","custom_field.text_value","custom_field.type","is_important","offset","parent","parent.name","path","project","project.name","uri"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a project's custom fields
    api_response = api_instance.get_custom_field_settings_for_project(project_gid, limit=limit, offset=offset, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomFieldSettingsApi->get_custom_field_settings_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**CustomFieldSettingResponseArray**](CustomFieldSettingResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

