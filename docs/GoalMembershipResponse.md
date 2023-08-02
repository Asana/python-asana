# GoalMembershipResponse

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
**user** | [**GoalMembershipResponseUser**](GoalMembershipResponseUser.md) |  | [optional] 
**workspace** | [**GoalMembershipResponseWorkspace**](GoalMembershipResponseWorkspace.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

