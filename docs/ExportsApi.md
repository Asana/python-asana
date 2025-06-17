# asana.ExportsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_graph_export**](ExportsApi.md#create_graph_export) | **POST** /exports/graph | Initiate graph export

# **create_graph_export**

Initiate graph export

Initiates a graph export job for a given parent object (team, portfolio, or project). The export will be processed asynchronously. Once initiated, use the [jobs](/reference/getjob) endpoint to monitor progress.  **Export Caching:** When exporting more than 1,000 tasks, the results are cached for 4 hours. Any new export requests made within this 4-hour window will return the same cached results rather than generating a fresh export.

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
    # Initiate graph export
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

