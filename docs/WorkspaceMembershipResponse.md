# WorkspaceMembershipResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**user** | [**CustomFieldResponsePeopleValue**](CustomFieldResponsePeopleValue.md) |  | [optional] 
**workspace** | [**GoalResponseWorkspace**](GoalResponseWorkspace.md) |  | [optional] 
**user_task_list** | [**WorkspaceMembershipResponseUserTaskList**](WorkspaceMembershipResponseUserTaskList.md) |  | [optional] 
**is_active** | **bool** | Reflects if this user still a member of the workspace. | [optional] 
**is_admin** | **bool** | Reflects if this user is an admin of the workspace. | [optional] 
**is_guest** | **bool** | Reflects if this user is a guest of the workspace. | [optional] 
**vacation_dates** | [**WorkspaceMembershipResponseVacationDates**](WorkspaceMembershipResponseVacationDates.md) |  | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

