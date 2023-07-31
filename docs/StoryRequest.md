# StoryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] 
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] 
**text** | **str** | The plain text of the comment to add. Cannot be used with html_text. | [optional] 
**html_text** | **str** | [Opt In](/docs/inputoutput-options). HTML formatted text for a comment. This will not include the name of the creator. | [optional] 
**is_pinned** | **bool** | *Conditional*. Whether the story should be pinned on the resource. | [optional] 
**sticker_name** | **str** | The name of the sticker in this story. &#x60;null&#x60; if there is no sticker. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

