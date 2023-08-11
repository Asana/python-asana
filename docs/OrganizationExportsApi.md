# asana.OrganizationExportsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_export**](OrganizationExportsApi.md#create_organization_export) | **POST** /organization_exports | Create an organization export request
[**get_organization_export**](OrganizationExportsApi.md#get_organization_export) | **GET** /organization_exports/{organization_export_gid} | Get details on an org export request

# **create_organization_export**
> OrganizationExportResponseData create_organization_export(body, opt_fields=opt_fields)

Create an organization export request

This method creates a request to export an Organization. Asana will complete the export at some point after you create the request.

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
api_instance = asana.OrganizationExportsApi(api_client)
body = asana.OrganizationExportsBody({"param1": "value1", "param2": "value2",}) # OrganizationExportsBody | The organization to export.
opt_fields = ["created_at","download_url","organization","organization.name","state"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Create an organization export request
    api_response = api_instance.create_organization_export(body, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationExportsApi->create_organization_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganizationExportsBody**](OrganizationExportsBody.md)| The organization to export. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**OrganizationExportResponseData**](OrganizationExportResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_export**
> OrganizationExportResponseData get_organization_export(organization_export_gid, opt_fields=opt_fields)

Get details on an org export request

Returns details of a previously-requested Organization export.

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
api_instance = asana.OrganizationExportsApi(api_client)
organization_export_gid = '12345' # str | Globally unique identifier for the organization export.
opt_fields = ["created_at","download_url","organization","organization.name","state"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get details on an org export request
    api_response = api_instance.get_organization_export(organization_export_gid, opt_fields=opt_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationExportsApi->get_organization_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_export_gid** | **str**| Globally unique identifier for the organization export. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**OrganizationExportResponseData**](OrganizationExportResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

