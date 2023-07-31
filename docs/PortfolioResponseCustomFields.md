# PortfolioResponseCustomFields

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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

