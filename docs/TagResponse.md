# TagResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**name** | **str** | Name of the tag. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. | [optional] 
**color** | **str** | Color of the tag. | [optional] 
**notes** | **str** | Free-form textual information associated with the tag (i.e. its description). | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] 
**followers** | [**list[CustomFieldResponsePeopleValue]**](CustomFieldResponsePeopleValue.md) | Array of users following this tag. | [optional] 
**workspace** | [**GoalResponseWorkspace**](GoalResponseWorkspace.md) |  | [optional] 
**permalink_url** | **str** | A url that points directly to the object within Asana. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

