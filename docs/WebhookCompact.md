# WebhookCompact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**active** | **bool** | If true, the webhook will send events - if false it is considered inactive and will not generate events. | [optional] 
**resource** | [**WebhookCompactResource**](WebhookCompactResource.md) |  | [optional] 
**target** | **str** | The URL to receive the HTTP POST. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

