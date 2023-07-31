# TaskBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | Globally unique identifier of the resource, as a string. | [optional] 
**resource_type** | **str** | The base type of this resource. | [optional] 
**name** | **str** | Name of the task. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer. | [optional] 
**resource_subtype** | **str** | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. The resource_subtype &#x60;milestone&#x60; represent a single moment in time. This means tasks with this subtype cannot have a start_date. | [optional] 
**approval_status** | **str** | *Conditional* Reflects the approval status of this task. This field is kept in sync with &#x60;completed&#x60;, meaning &#x60;pending&#x60; translates to false while &#x60;approved&#x60;, &#x60;rejected&#x60;, and &#x60;changes_requested&#x60; translate to true. If you set completed to true, this field will be set to &#x60;approved&#x60;. | [optional] 
**assignee_status** | **str** | *Deprecated* Scheduling status of this task for the user it is assigned to. This field can only be set if the assignee is non-null. Setting this field to \&quot;inbox\&quot; or \&quot;upcoming\&quot; inserts it at the top of the section, while the other options will insert at the bottom. | [optional] 
**completed** | **bool** | True if the task is currently marked complete, false if not. | [optional] 
**completed_at** | **datetime** | The time at which this task was completed, or null if the task is incomplete. | [optional] 
**completed_by** | [**TaskBaseCompletedBy**](TaskBaseCompletedBy.md) |  | [optional] 
**created_at** | **datetime** | The time at which this resource was created. | [optional] 
**dependencies** | [**list[TaskBaseDependencies]**](TaskBaseDependencies.md) | [Opt In](/docs/inputoutput-options). Array of resources referencing tasks that this task depends on. The objects contain only the gid of the dependency. | [optional] 
**dependents** | [**list[TaskBaseDependencies]**](TaskBaseDependencies.md) | [Opt In](/docs/inputoutput-options). Array of resources referencing tasks that depend on this task. The objects contain only the ID of the dependent. | [optional] 
**due_at** | **datetime** | The UTC date and time on which this task is due, or null if the task has no due time. This takes an ISO 8601 date string in UTC and should not be used together with &#x60;due_on&#x60;. | [optional] 
**due_on** | **date** | The localized date on which this task is due, or null if the task has no due date. This takes a date with &#x60;YYYY-MM-DD&#x60; format and should not be used together with &#x60;due_at&#x60;. | [optional] 
**external** | [**TaskBaseExternal**](TaskBaseExternal.md) |  | [optional] 
**html_notes** | **str** | [Opt In](/docs/inputoutput-options). The notes of the text with formatting as HTML. | [optional] 
**hearted** | **bool** | *Deprecated - please use liked instead* True if the task is hearted by the authorized user, false if not. | [optional] 
**hearts** | [**list[GoalResponseLikes]**](GoalResponseLikes.md) | *Deprecated - please use likes instead* Array of likes for users who have hearted this task. | [optional] 
**is_rendered_as_separator** | **bool** | [Opt In](/docs/inputoutput-options). In some contexts tasks can be rendered as a visual separator; for instance, subtasks can appear similar to [sections](/reference/sections) without being true &#x60;section&#x60; objects. If a &#x60;task&#x60; object is rendered this way in any context it will have the property &#x60;is_rendered_as_separator&#x60; set to &#x60;true&#x60;. | [optional] 
**liked** | **bool** | True if the task is liked by the authorized user, false if not. | [optional] 
**likes** | [**list[GoalResponseLikes]**](GoalResponseLikes.md) | Array of likes for users who have liked this task. | [optional] 
**memberships** | [**list[TaskBaseMemberships]**](TaskBaseMemberships.md) | *Create-only*. Array of projects this task is associated with and the section it is in. At task creation time, this array can be used to add the task to specific sections. After task creation, these associations can be modified using the &#x60;addProject&#x60; and &#x60;removeProject&#x60; endpoints. Note that over time, more types of memberships may be added to this property. | [optional] 
**modified_at** | **datetime** | The time at which this task was last modified.  The following conditions will change &#x60;modified_at&#x60;:  - story is created on a task - story is trashed on a task - attachment is trashed on a task - task is assigned or unassigned - custom field value is changed - the task itself is trashed - Or if any of the following fields are updated:   - completed   - name   - due_date   - description   - attachments   - items   - schedule_status  The following conditions will _not_ change &#x60;modified_at&#x60;:  - moving to a new container (project, portfolio, etc) - comments being added to the task (but the stories they generate   _will_ affect &#x60;modified_at&#x60;) | [optional] 
**notes** | **str** | Free-form textual information associated with the task (i.e. its description). | [optional] 
**num_hearts** | **int** | *Deprecated - please use likes instead* The number of users who have hearted this task. | [optional] 
**num_likes** | **int** | The number of users who have liked this task. | [optional] 
**num_subtasks** | **int** | [Opt In](/docs/inputoutput-options). The number of subtasks on this task.  | [optional] 
**start_at** | **datetime** | Date and time on which work begins for the task, or null if the task has no start time. This takes an ISO 8601 date string in UTC and should not be used together with &#x60;start_on&#x60;. *Note: &#x60;due_at&#x60; must be present in the request when setting or unsetting the &#x60;start_at&#x60; parameter.* | [optional] 
**start_on** | **date** | The day on which work begins for the task , or null if the task has no start date. This takes a date with &#x60;YYYY-MM-DD&#x60; format and should not be used together with &#x60;start_at&#x60;. *Note: &#x60;due_on&#x60; or &#x60;due_at&#x60; must be present in the request when setting or unsetting the &#x60;start_on&#x60; parameter.* | [optional] 
**actual_time_minutes** | **float** | This value represents the sum of all the Time Tracking entries in the Actual Time field on a given Task. It is represented as a nullable long value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

