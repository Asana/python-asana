# GoalRelationshipCompact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] 
**supporting_resource** | [**GoalRelationshipBaseSupportingResource**](GoalRelationshipBaseSupportingResource.md) |  | [optional] 
**contribution_weight** | **float** | The weight that the supporting resource&#x27;s progress contributes to the supported goal&#x27;s progress. This can only be 0 or 1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

