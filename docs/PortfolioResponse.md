# PortfolioResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**name** | **str** | The name of the portfolio. | [optional] 
**color** | **str** | Color of the portfolio. | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] 
**created_by** | [**CustomFieldResponsePeopleValue**](CustomFieldResponsePeopleValue.md) |  | [optional] 
**custom_field_settings** | [**list[PortfolioResponseCustomFieldSettings]**](PortfolioResponseCustomFieldSettings.md) | Array of custom field settings applied to the portfolio. | [optional] 
**current_status_update** | [**PortfolioResponseCurrentStatusUpdate**](PortfolioResponseCurrentStatusUpdate.md) |  | [optional] 
**due_on** | **date** | The localized day on which this portfolio is due. This takes a date with format YYYY-MM-DD. | [optional] 
**custom_fields** | [**list[PortfolioResponseCustomFields]**](PortfolioResponseCustomFields.md) | Array of Custom Fields. | [optional] 
**members** | [**list[CustomFieldResponsePeopleValue]**](CustomFieldResponsePeopleValue.md) |  | [optional] 
**owner** | [**CustomFieldResponsePeopleValue**](CustomFieldResponsePeopleValue.md) |  | [optional] 
**start_on** | **date** | The day on which work for this portfolio begins, or null if the portfolio has no start date. This takes a date with &#x60;YYYY-MM-DD&#x60; format. *Note: &#x60;due_on&#x60; must be present in the request when setting or unsetting the &#x60;start_on&#x60; parameter. Additionally, &#x60;start_on&#x60; and &#x60;due_on&#x60; cannot be the same date.* | [optional] 
**workspace** | [**PortfolioResponseWorkspace**](PortfolioResponseWorkspace.md) |  | [optional] 
**permalink_url** | **str** | A url that points directly to the object within Asana. | [optional] 
**public** | **bool** | True if the portfolio is public to its workspace members. | [optional] 
**project_templates** | [**list[JobBaseNewProjectTemplate]**](JobBaseNewProjectTemplate.md) | Array of project templates that are in the portfolio | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

