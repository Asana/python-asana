# StatusUpdateResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**title** | **str** | The title of the status update. | [optional] 
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. The &#x60;resource_subtype&#x60;s for &#x60;status&#x60; objects represent the type of their parent. | [optional] 
**text** | **str** | The text content of the status update. | 
**html_text** | **str** | [Opt In](/docs/inputoutput-options). The text content of the status update with formatting as HTML. | [optional] 
**status_type** | **str** | The type associated with the status update. This represents the current state of the object this object is on. | 
**author** | [**CustomFieldResponsePeopleValue**](CustomFieldResponsePeopleValue.md) |  | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] 
**created_by** | [**CustomFieldResponsePeopleValue**](CustomFieldResponsePeopleValue.md) |  | [optional] 
**hearted** | **bool** | *Deprecated - please use liked instead* True if the status is hearted by the authorized user, false if not. | [optional] 
**hearts** | [**list[GoalResponseLikes]**](GoalResponseLikes.md) | *Deprecated - please use likes instead* Array of likes for users who have hearted this status. | [optional] 
**liked** | **bool** | True if the status is liked by the authorized user, false if not. | [optional] 
**likes** | [**list[GoalResponseLikes]**](GoalResponseLikes.md) | Array of likes for users who have liked this status. | [optional] 
**modified_at** | **datetime** | The time at which this project status was last modified. *Note: This does not currently reflect any changes in associations such as comments that may have been added or removed from the status.* | [optional] 
**num_hearts** | **int** | *Deprecated - please use likes instead* The number of users who have hearted this status. | [optional] 
**num_likes** | **int** | The number of users who have liked this status. | [optional] 
**parent** | [**StatusUpdateResponseParent**](StatusUpdateResponseParent.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

