# asana.ProjectPortfolioSettingsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_project_portfolio_setting**](ProjectPortfolioSettingsApi.md#get_project_portfolio_setting) | **GET** /project_portfolio_settings/{project_portfolio_setting_gid} | Get a project portfolio setting
[**get_project_portfolio_settings_for_portfolio**](ProjectPortfolioSettingsApi.md#get_project_portfolio_settings_for_portfolio) | **GET** /portfolios/{portfolio_gid}/project_portfolio_settings | Get project portfolio settings for a portfolio
[**get_project_portfolio_settings_for_project**](ProjectPortfolioSettingsApi.md#get_project_portfolio_settings_for_project) | **GET** /projects/{project_gid}/project_portfolio_settings | Get project portfolio settings for a project
[**update_project_portfolio_setting**](ProjectPortfolioSettingsApi.md#update_project_portfolio_setting) | **PUT** /project_portfolio_settings/{project_portfolio_setting_gid} | Update a project portfolio setting

# **get_project_portfolio_setting**

Get a project portfolio setting

<b>Required scope: </b><code>project_portfolio_settings:read</code>  Returns the complete project portfolio setting record for a single project portfolio setting.

([more information](https://developers.asana.com/reference/getprojectportfoliosetting))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_portfolio_settings_api_instance = asana.ProjectPortfolioSettingsApi(api_client)
project_portfolio_setting_gid = "1331" # str | Globally unique identifier for the project portfolio setting.
opts = {
    'opt_fields': "created_at,is_access_control_inherited,portfolio,project", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a project portfolio setting
    api_response = project_portfolio_settings_api_instance.get_project_portfolio_setting(project_portfolio_setting_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectPortfolioSettingsApi->get_project_portfolio_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_portfolio_setting_gid** | **str**| Globally unique identifier for the project portfolio setting. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_project_portfolio_settings_for_portfolio**

Get project portfolio settings for a portfolio

<b>Required scope: </b><code>project_portfolio_settings:read</code>  Returns a compact representation of all of the project portfolio settings for the given portfolio.

([more information](https://developers.asana.com/reference/getprojectportfoliosettingsforportfolio))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_portfolio_settings_api_instance = asana.ProjectPortfolioSettingsApi(api_client)
portfolio_gid = "12345" # str | Globally unique identifier for the portfolio.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "created_at,is_access_control_inherited,offset,path,portfolio,project,uri", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get project portfolio settings for a portfolio
    api_response = project_portfolio_settings_api_instance.get_project_portfolio_settings_for_portfolio(portfolio_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling ProjectPortfolioSettingsApi->get_project_portfolio_settings_for_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_gid** | **str**| Globally unique identifier for the portfolio. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_project_portfolio_settings_for_project**

Get project portfolio settings for a project

<b>Required scope: </b><code>project_portfolio_settings:read</code>  Returns a compact representation of all of the project portfolio settings for the given project.

([more information](https://developers.asana.com/reference/getprojectportfoliosettingsforproject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_portfolio_settings_api_instance = asana.ProjectPortfolioSettingsApi(api_client)
project_gid = "1331" # str | Globally unique identifier for the project.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "created_at,is_access_control_inherited,offset,path,portfolio,project,uri", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get project portfolio settings for a project
    api_response = project_portfolio_settings_api_instance.get_project_portfolio_settings_for_project(project_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling ProjectPortfolioSettingsApi->get_project_portfolio_settings_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_project_portfolio_setting**

Update a project portfolio setting

<b>Required scope: </b><code>project_portfolio_settings:write</code>  An existing project portfolio setting can be updated by making a PUT request on the URL for that setting. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated project portfolio setting record.

([more information](https://developers.asana.com/reference/updateprojectportfoliosetting))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
project_portfolio_settings_api_instance = asana.ProjectPortfolioSettingsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The updated fields for the project portfolio setting.
project_portfolio_setting_gid = "1331" # str | Globally unique identifier for the project portfolio setting.
opts = {
    'opt_fields': "created_at,is_access_control_inherited,portfolio,project", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Update a project portfolio setting
    api_response = project_portfolio_settings_api_instance.update_project_portfolio_setting(body, project_portfolio_setting_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectPortfolioSettingsApi->update_project_portfolio_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The updated fields for the project portfolio setting. | 
 **project_portfolio_setting_gid** | **str**| Globally unique identifier for the project portfolio setting. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

