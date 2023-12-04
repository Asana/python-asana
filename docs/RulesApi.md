# asana.RulesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trigger_rule**](RulesApi.md#trigger_rule) | **POST** /rule_triggers/{rule_trigger_gid}/run | Trigger a rule

# **trigger_rule**

Trigger a rule

Trigger a rule which uses an [\"incoming web request\"](/docs/incoming-web-requests) trigger.

([more information](https://developers.asana.com/reference/triggerrule))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
rules_api_instance = asana.RulesApi(api_client)
body = {"data": {"param1": "value1", "param2": "value2",}} # dict | A dictionary of variables accessible from within the rule.
rule_trigger_gid = "12345" # str | The ID of the incoming web request trigger. This value is a path parameter that is automatically generated for the API endpoint.


try:
    # Trigger a rule
    api_response = rules_api_instance.trigger_rule(body, rule_trigger_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->trigger_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| A dictionary of variables accessible from within the rule. | 
 **rule_trigger_gid** | **str**| The ID of the incoming web request trigger. This value is a path parameter that is automatically generated for the API endpoint. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

