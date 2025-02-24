# asana.OrganizationExportsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_export**](OrganizationExportsApi.md#create_organization_export) | **POST** /organization_exports | Create an organization export request
[**get_organization_export**](OrganizationExportsApi.md#get_organization_export) | **GET** /organization_exports/{organization_export_gid} | Get details on an org export request

# **create_organization_export**

Create an organization export request

This method creates a request to export an Organization. Asana will complete the export at some point after you create the request.

([more information](https://developers.asana.com/reference/createorganizationexport))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
organization_exports_api_instance = asana.OrganizationExportsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The organization to export.
opts = {
    'opt_fields': "created_at,download_url,organization,organization.name,state", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Create an organization export request
    api_response = organization_exports_api_instance.create_organization_export(body, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationExportsApi->create_organization_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The organization to export. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_organization_export**

Get details on an org export request

Returns details of a previously-requested Organization export.

([more information](https://developers.asana.com/reference/getorganizationexport))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
organization_exports_api_instance = asana.OrganizationExportsApi(api_client)
organization_export_gid = "12345" # str | Globally unique identifier for the organization export.
opts = {
    'opt_fields': "created_at,download_url,organization,organization.name,state", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get details on an org export request
    api_response = organization_exports_api_instance.get_organization_export(organization_export_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationExportsApi->get_organization_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_export_gid** | **str**| Globally unique identifier for the organization export. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

