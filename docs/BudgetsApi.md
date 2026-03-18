# asana.BudgetsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_budget**](BudgetsApi.md#create_budget) | **POST** /budgets | Create a budget
[**delete_budget**](BudgetsApi.md#delete_budget) | **DELETE** /budgets/{budget_gid} | Delete a budget
[**get_budget**](BudgetsApi.md#get_budget) | **GET** /budgets/{budget_gid} | Get a budget
[**get_budgets**](BudgetsApi.md#get_budgets) | **GET** /budgets | Get all budgets
[**update_budget**](BudgetsApi.md#update_budget) | **PUT** /budgets/{budget_gid} | Update a budget

# **create_budget**

Create a budget

Creates a new budget.

([more information](https://developers.asana.com/reference/createbudget))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
budgets_api_instance = asana.BudgetsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The budget to create.


try:
    # Create a budget
    api_response = budgets_api_instance.create_budget(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->create_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The budget to create. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_budget**

Delete a budget

A specific, existing budget can be deleted by making a DELETE request on the URL for that budget.  Returns an empty data record.

([more information](https://developers.asana.com/reference/deletebudget))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
budgets_api_instance = asana.BudgetsApi(api_client)
budget_gid = "12345" # str | Globally unique identifier for the budget.


try:
    # Delete a budget
    api_response = budgets_api_instance.delete_budget(budget_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->delete_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_gid** | **str**| Globally unique identifier for the budget. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_budget**

Get a budget

Returns the complete budget record for a single budget.

([more information](https://developers.asana.com/reference/getbudget))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
budgets_api_instance = asana.BudgetsApi(api_client)
budget_gid = "12345" # str | Globally unique identifier for the budget.
opts = {
    'opt_fields': "actual,actual.billable_status_filter,actual.units,actual.value,budget_type,estimate,estimate.billable_status_filter,estimate.enabled,estimate.source,estimate.units,estimate.value,parent,parent.name,total,total.enabled,total.units,total.value", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a budget
    api_response = budgets_api_instance.get_budget(budget_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->get_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_gid** | **str**| Globally unique identifier for the budget. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_budgets**

Get all budgets

Gets all budgets for a given *parent*. This will at most return a list of size 1 for a given *parent*.

([more information](https://developers.asana.com/reference/getbudgets))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
budgets_api_instance = asana.BudgetsApi(api_client)
parent = "1331" # str | Globally unique identifier for the budget's parent object. This currently can only be a `project`.


try:
    # Get all budgets
    api_response = budgets_api_instance.get_budgets(parent)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling BudgetsApi->get_budgets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| Globally unique identifier for the budget&#x27;s parent object. This currently can only be a &#x60;project&#x60;. | 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_budget**

Update a budget

An existing budget can be updated by making a PUT request on the URL for that budget. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.

([more information](https://developers.asana.com/reference/updatebudget))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
budgets_api_instance = asana.BudgetsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The budget to update.
budget_gid = "12345" # str | Globally unique identifier for the budget.
opts = {
    'opt_fields': "actual,actual.billable_status_filter,actual.units,actual.value,budget_type,estimate,estimate.billable_status_filter,estimate.enabled,estimate.source,estimate.units,estimate.value,parent,parent.name,total,total.enabled,total.units,total.value", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Update a budget
    api_response = budgets_api_instance.update_budget(body, budget_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BudgetsApi->update_budget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The budget to update. | 
 **budget_gid** | **str**| Globally unique identifier for the budget. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

