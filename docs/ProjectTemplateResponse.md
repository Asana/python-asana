# ProjectTemplateResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**name** | **str** | Name of the project template. | [optional] 
**description** | **str** | Free-form textual information associated with the project template | [optional] 
**html_description** | **str** | The description of the project template with formatting as HTML. | [optional] 
**public** | **bool** | True if the project template is public to its team. | [optional] 
**owner** | **AllOfProjectTemplateResponseOwner** | The current owner of the project template, may be null. | [optional] 
**team** | [**ProjectTemplateBaseTeam**](ProjectTemplateBaseTeam.md) |  | [optional] 
**requested_dates** | [**list[ProjectTemplateBaseRequestedDates]**](ProjectTemplateBaseRequestedDates.md) | Array of date variables in this project template. Calendar dates must be provided for these variables when instantiating a project. | [optional] 
**color** | **str** | Color of the project template. | [optional] 
**requested_roles** | [**list[ProjectTemplateBaseRequestedRoles]**](ProjectTemplateBaseRequestedRoles.md) | Array of template roles in this project template. User Ids can be provided for these variables when instantiating a project to assign template tasks to the user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

