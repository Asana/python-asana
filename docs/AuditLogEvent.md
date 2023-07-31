# AuditLogEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the &#x60;AuditLogEvent&#x60;, as a string. | [optional] 
**created_at** | **datetime** | The time the event was created. | [optional] 
**event_type** | **str** | The type of the event. | [optional] 
**event_category** | **str** | The category that this &#x60;event_type&#x60; belongs to. | [optional] 
**actor** | [**AuditLogEventActor**](AuditLogEventActor.md) |  | [optional] 
**resource** | [**AuditLogEventResource**](AuditLogEventResource.md) |  | [optional] 
**details** | **object** | Event specific details. The schema will vary depending on the &#x60;event_type&#x60;. | [optional] 
**context** | [**AuditLogEventContext**](AuditLogEventContext.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

