# WebhookResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**active** | **bool** | If true, the webhook will send events - if false it is considered inactive and will not generate events. | [optional] 
**resource** | [**WebhookCompactResource**](WebhookCompactResource.md) |  | [optional] 
**target** | **str** | The URL to receive the HTTP POST. | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] 
**last_failure_at** | **datetime** | The timestamp when the webhook last received an error when sending an event to the target. | [optional] 
**last_failure_content** | **str** | The contents of the last error response sent to the webhook when attempting to deliver events to the target. | [optional] 
**last_success_at** | **datetime** | The timestamp when the webhook last successfully sent an event to the target. | [optional] 
**filters** | [**list[WebhookRequestFilters]**](WebhookRequestFilters.md) | Whitelist of filters to apply to events from this webhook. If a webhook event passes any of the filters the event will be delivered; otherwise no event will be sent to the receiving server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

