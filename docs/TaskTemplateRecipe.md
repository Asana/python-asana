# TaskTemplateRecipe

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the task that will be created from this template. | [optional] 
**task_resource_subtype** | **str** | The subtype of the task that will be created from this template. | [optional] 
**description** | **str** | Description of the task that will be created from this template. | [optional] 
**html_description** | **str** | HTML description of the task that will be created from this template. | [optional] 
**memberships** | [**list[JobBaseNewProject]**](JobBaseNewProject.md) | Array of projects that the task created from this template will be added to | [optional] 
**relative_start_on** | **int** | The number of days after the task has been instantiated on which that the task will start | [optional] 
**relative_due_on** | **int** | The number of days after the task has been instantiated on which that the task will be due | [optional] 
**due_time** | **str** | The time of day that the task will be due | [optional] 
**dependencies** | [**list[TaskTemplateRecipeDependencies]**](TaskTemplateRecipeDependencies.md) | Array of task templates that the task created from this template will depend on | [optional] 
**dependents** | [**list[TaskTemplateRecipeDependencies]**](TaskTemplateRecipeDependencies.md) | Array of task templates that will depend on the task created from this template | [optional] 
**followers** | [**list[CustomFieldResponsePeopleValue]**](CustomFieldResponsePeopleValue.md) | Array of users that will be added as followers to the task created from this template | [optional] 
**attachments** | [**list[TaskTemplateRecipeAttachments]**](TaskTemplateRecipeAttachments.md) | Array of attachments that will be added to the task created from this template | [optional] 
**subtasks** | [**list[TaskTemplateRecipeDependencies]**](TaskTemplateRecipeDependencies.md) | Array of subtasks that will be added to the task created from this template | [optional] 
**custom_fields** | [**list[PortfolioResponseCustomFields]**](PortfolioResponseCustomFields.md) | Array of custom fields that will be added to the task created from this template | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

