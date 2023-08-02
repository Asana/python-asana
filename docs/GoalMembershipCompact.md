# GoalMembershipCompact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**resource_subtype** | **str** | The type of membership. | [optional] 
**member** | [**MembershipCompactMember**](MembershipCompactMember.md) |  | [optional] 
**parent** | [**MembershipCompactParent**](MembershipCompactParent.md) |  | [optional] 
**role** | **str** | Describes if the member is a commenter or editor in goal. | [optional] 
**goal** | [**MembershipCompactGoal**](MembershipCompactGoal.md) |  | [optional] 
**is_commenter** | **bool** | *Deprecated: new integrations should prefer the &#x60;role&#x60; field.* Describes if the member is comment only in goal. | [optional] 
**is_editor** | **bool** | *Deprecated: new integrations should prefer the &#x60;role&#x60; field.* Describes if the member is editor in goal. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

