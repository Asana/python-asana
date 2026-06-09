# asana.AgentsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent**](AgentsApi.md#get_agent) | **GET** /agents/{agent_gid} | Get an agent
[**get_agents_for_workspace**](AgentsApi.md#get_agents_for_workspace) | **GET** /workspaces/{workspace_gid}/agents | Get a list of agents in a workspace

# **get_agent**

Get an agent

Returns the complete record for a single agent (AI Teammate).

([more information](https://developers.asana.com/reference/getagent))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
agents_api_instance = asana.AgentsApi(api_client)
agent_gid = "12345" # str | Globally unique identifier for the agent.
opts = {
    'opt_fields': "behavior_guidance,description,name,photo,photo.image_1024x1024,photo.image_128x128,photo.image_21x21,photo.image_27x27,photo.image_36x36,photo.image_60x60,resource_subtype,workspace", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get an agent
    api_response = agents_api_instance.get_agent(agent_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->get_agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_gid** | **str**| Globally unique identifier for the agent. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_agents_for_workspace**

Get a list of agents in a workspace

Returns the compact records of agents (AI Teammates) configured. Use `opt_fields` to request additional fields in the workspace.

([more information](https://developers.asana.com/reference/getagentsforworkspace))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
agents_api_instance = asana.AgentsApi(api_client)
workspace_gid = "12345" # str | Globally unique identifier for the workspace or organization.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "behavior_guidance,description,name,offset,path,photo,photo.image_1024x1024,photo.image_128x128,photo.image_21x21,photo.image_27x27,photo.image_36x36,photo.image_60x60,resource_subtype,uri,workspace", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a list of agents in a workspace
    api_response = agents_api_instance.get_agents_for_workspace(workspace_gid, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling AgentsApi->get_agents_for_workspace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_gid** | **str**| Globally unique identifier for the workspace or organization. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

