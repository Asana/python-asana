# CustomFieldResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**name** | **str** | The name of the custom field. | [optional] 
**resource_subtype** | **str** | The type of the custom field. Must be one of the given values.  | [optional] 
**type** | **str** | *Deprecated: new integrations should prefer the resource_subtype field.* The type of the custom field. Must be one of the given values.  | [optional] 
**enum_options** | [**list[CustomFieldBaseEnumOptions]**](CustomFieldBaseEnumOptions.md) | *Conditional*. Only relevant for custom fields of type &#x60;enum&#x60;. This array specifies the possible values which an &#x60;enum&#x60; custom field can adopt. To modify the enum options, refer to [working with enum options](/reference/createenumoptionforcustomfield). | [optional] 
**enabled** | **bool** | *Conditional*. Determines if the custom field is enabled or not. | [optional] 
**is_formula_field** | **bool** | *Conditional*. This flag describes whether a custom field is a formula custom field. | [optional] 
**date_value** | [**CustomFieldBaseDateValue**](CustomFieldBaseDateValue.md) |  | [optional] 
**enum_value** | [**CustomFieldBaseEnumValue**](CustomFieldBaseEnumValue.md) |  | [optional] 
**multi_enum_values** | [**list[CustomFieldBaseEnumOptions]**](CustomFieldBaseEnumOptions.md) | *Conditional*. Only relevant for custom fields of type &#x60;multi_enum&#x60;. This object is the chosen values of a &#x60;multi_enum&#x60; custom field. | [optional] 
**number_value** | **float** | *Conditional*. This number is the value of a &#x60;number&#x60; custom field. | [optional] 
**text_value** | **str** | *Conditional*. This string is the value of a &#x60;text&#x60; custom field. | [optional] 
**display_value** | **str** | A string representation for the value of the custom field. Integrations that don&#x27;t require the underlying type should use this field to read values. Using this field will future-proof an app against new custom field types. | [optional] 
**description** | **str** | [Opt In](/docs/inputoutput-options). The description of the custom field. | [optional] 
**precision** | **int** | Only relevant for custom fields of type ‘Number’. This field dictates the number of places after the decimal to round to, i.e. 0 is integer values, 1 rounds to the nearest tenth, and so on. Must be between 0 and 6, inclusive. For percentage format, this may be unintuitive, as a value of 0.25 has a precision of 0, while a value of 0.251 has a precision of 1. This is due to 0.25 being displayed as 25%. The identifier format will always have a precision of 0. | [optional] 
**format** | **str** | The format of this custom field. | [optional] 
**currency_code** | **str** | ISO 4217 currency code to format this custom field. This will be null if the &#x60;format&#x60; is not &#x60;currency&#x60;. | [optional] 
**custom_label** | **str** | This is the string that appears next to the custom field value. This will be null if the &#x60;format&#x60; is not &#x60;custom&#x60;. | [optional] 
**custom_label_position** | **str** | Only relevant for custom fields with &#x60;custom&#x60; format. This depicts where to place the custom label. This will be null if the &#x60;format&#x60; is not &#x60;custom&#x60;. | [optional] 
**is_global_to_workspace** | **bool** | This flag describes whether this custom field is available to every container in the workspace. Before project-specific custom fields, this field was always true. | [optional] 
**has_notifications_enabled** | **bool** | *Conditional*. This flag describes whether a follower of a task with this field should receive inbox notifications from changes to this field. | [optional] 
**asana_created_field** | **str** | *Conditional*. A unique identifier to associate this field with the template source of truth. | [optional] 
**is_value_read_only** | **bool** | *Conditional*. This flag describes whether a custom field is read only. | [optional] 
**created_by** | [**CustomFieldResponseCreatedBy**](CustomFieldResponseCreatedBy.md) |  | [optional] 
**people_value** | [**list[CustomFieldResponsePeopleValue]**](CustomFieldResponsePeopleValue.md) | *Conditional*. Only relevant for custom fields of type &#x60;people&#x60;. This array of [compact user](/reference/users) objects reflects the values of a &#x60;people&#x60; custom field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

