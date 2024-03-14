# asana.GoalRelationshipsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_supporting_relationship**](GoalRelationshipsApi.md#add_supporting_relationship) | **POST** /goals/{goal_gid}/addSupportingRelationship | Add a supporting goal relationship
[**get_goal_relationship**](GoalRelationshipsApi.md#get_goal_relationship) | **GET** /goal_relationships/{goal_relationship_gid} | Get a goal relationship
[**get_goal_relationships**](GoalRelationshipsApi.md#get_goal_relationships) | **GET** /goal_relationships | Get goal relationships
[**remove_supporting_relationship**](GoalRelationshipsApi.md#remove_supporting_relationship) | **POST** /goals/{goal_gid}/removeSupportingRelationship | Removes a supporting goal relationship
[**update_goal_relationship**](GoalRelationshipsApi.md#update_goal_relationship) | **PUT** /goal_relationships/{goal_relationship_gid} | Update a goal relationship

# **add_supporting_relationship**

Add a supporting goal relationship

Creates a goal relationship by adding a supporting resource to a given goal.  Returns the newly created goal relationship record.

([more information](https://developers.asana.com/reference/addsupportingrelationship))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
goal_relationships_api_instance = asana.GoalRelationshipsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The supporting resource to be added to the goal
goal_gid = "12345" # str | Globally unique identifier for the goal.
opts = {
    'opt_fields': "contribution_weight,resource_subtype,supported_goal,supported_goal.name,supported_goal.owner,supported_goal.owner.name,supporting_resource,supporting_resource.name", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Add a supporting goal relationship
    api_response = goal_relationships_api_instance.add_supporting_relationship(body, goal_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalRelationshipsApi->add_supporting_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The supporting resource to be added to the goal | 
 **goal_gid** | **str**| Globally unique identifier for the goal. | 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_goal_relationship**

Get a goal relationship

Returns the complete updated goal relationship record for a single goal relationship.

([more information](https://developers.asana.com/reference/getgoalrelationship))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
goal_relationships_api_instance = asana.GoalRelationshipsApi(api_client)
goal_relationship_gid = "12345" # str | Globally unique identifier for the goal relationship.
opts = {
    'opt_fields': "contribution_weight,resource_subtype,supported_goal,supported_goal.name,supported_goal.owner,supported_goal.owner.name,supporting_resource,supporting_resource.name", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get a goal relationship
    api_response = goal_relationships_api_instance.get_goal_relationship(goal_relationship_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalRelationshipsApi->get_goal_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_relationship_gid** | **str**| Globally unique identifier for the goal relationship. | 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_goal_relationships**

Get goal relationships

Returns compact goal relationship records.

([more information](https://developers.asana.com/reference/getgoalrelationships))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
goal_relationships_api_instance = asana.GoalRelationshipsApi(api_client)
supported_goal = "12345" # str | Globally unique identifier for the supported goal in the goal relationship.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    'resource_subtype': "subgoal", # str | If provided, filter to goal relationships with a given resource_subtype.
    'opt_fields': "contribution_weight,offset,path,resource_subtype,supported_goal,supported_goal.name,supported_goal.owner,supported_goal.owner.name,supporting_resource,supporting_resource.name,uri", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get goal relationships
    api_response = goal_relationships_api_instance.get_goal_relationships(supported_goal, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling GoalRelationshipsApi->get_goal_relationships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supported_goal** | **str**| Globally unique identifier for the supported goal in the goal relationship. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **resource_subtype** | **str**| If provided, filter to goal relationships with a given resource_subtype. | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **remove_supporting_relationship**

Removes a supporting goal relationship

Removes a goal relationship for a given parent goal.

([more information](https://developers.asana.com/reference/removesupportingrelationship))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
goal_relationships_api_instance = asana.GoalRelationshipsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The supporting resource to be removed from the goal
goal_gid = "12345" # str | Globally unique identifier for the goal.


try:
    # Removes a supporting goal relationship
    api_response = goal_relationships_api_instance.remove_supporting_relationship(body, goal_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalRelationshipsApi->remove_supporting_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The supporting resource to be removed from the goal | 
 **goal_gid** | **str**| Globally unique identifier for the goal. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **update_goal_relationship**

Update a goal relationship

An existing goal relationship can be updated by making a PUT request on the URL for that goal relationship. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated goal relationship record.

([more information](https://developers.asana.com/reference/updategoalrelationship))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
goal_relationships_api_instance = asana.GoalRelationshipsApi(api_client)
body = {"data": {"<PARAM_1>": "<VALUE_1>", "<PARAM_2>": "<VALUE_2>",}} # dict | The updated fields for the goal relationship.
goal_relationship_gid = "12345" # str | Globally unique identifier for the goal relationship.
opts = {
    'opt_fields': "contribution_weight,resource_subtype,supported_goal,supported_goal.name,supported_goal.owner,supported_goal.owner.name,supporting_resource,supporting_resource.name", # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Update a goal relationship
    api_response = goal_relationships_api_instance.update_goal_relationship(body, goal_relationship_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoalRelationshipsApi->update_goal_relationship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Dict**| The updated fields for the goal relationship. | 
 **goal_relationship_gid** | **str**| Globally unique identifier for the goal relationship. | 
 **opt_fields** | **Dict**| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

