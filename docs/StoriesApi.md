# asana.StoriesApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_story_for_task**](StoriesApi.md#create_story_for_task) | **POST** /tasks/{task_gid}/stories | Create a story on a task
[**delete_story**](StoriesApi.md#delete_story) | **DELETE** /stories/{story_gid} | Delete a story
[**get_stories_for_task**](StoriesApi.md#get_stories_for_task) | **GET** /tasks/{task_gid}/stories | Get stories from a task
[**get_story**](StoriesApi.md#get_story) | **GET** /stories/{story_gid} | Get a story
[**update_story**](StoriesApi.md#update_story) | **PUT** /stories/{story_gid} | Update a story

# **create_story_for_task**
> StoryResponseData create_story_for_task(body, task_gid, opt_fields=opt_fields)

Create a story on a task

Adds a story to a task. This endpoint currently only allows for comment stories to be created. The comment will be authored by the currently authenticated user, and timestamped when the server receives the request.  Returns the full record for the new story added to the task.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.StoriesApi(asana.ApiClient(configuration))
body = asana.TaskGidStoriesBody({"param1": "value1", "param2": "value2",}) # TaskGidStoriesBody | The story to create.
task_gid = '321654' # str | The task to operate on.
opt_fields = ["assignee","assignee.name","created_at","created_by","created_by.name","custom_field","custom_field.date_value","custom_field.date_value.date","custom_field.date_value.date_time","custom_field.display_value","custom_field.enabled","custom_field.enum_options","custom_field.enum_options.color","custom_field.enum_options.enabled","custom_field.enum_options.name","custom_field.enum_value","custom_field.enum_value.color","custom_field.enum_value.enabled","custom_field.enum_value.name","custom_field.is_formula_field","custom_field.multi_enum_values","custom_field.multi_enum_values.color","custom_field.multi_enum_values.enabled","custom_field.multi_enum_values.name","custom_field.name","custom_field.number_value","custom_field.resource_subtype","custom_field.text_value","custom_field.type","dependency","dependency.name","dependency.resource_subtype","duplicate_of","duplicate_of.name","duplicate_of.resource_subtype","duplicated_from","duplicated_from.name","duplicated_from.resource_subtype","follower","follower.name","hearted","hearts","hearts.user","hearts.user.name","html_text","is_editable","is_edited","is_pinned","liked","likes","likes.user","likes.user.name","new_approval_status","new_date_value","new_dates","new_dates.due_at","new_dates.due_on","new_dates.start_on","new_enum_value","new_enum_value.color","new_enum_value.enabled","new_enum_value.name","new_multi_enum_values","new_multi_enum_values.color","new_multi_enum_values.enabled","new_multi_enum_values.name","new_name","new_number_value","new_people_value","new_people_value.name","new_resource_subtype","new_section","new_section.name","new_text_value","num_hearts","num_likes","old_approval_status","old_date_value","old_dates","old_dates.due_at","old_dates.due_on","old_dates.start_on","old_enum_value","old_enum_value.color","old_enum_value.enabled","old_enum_value.name","old_multi_enum_values","old_multi_enum_values.color","old_multi_enum_values.enabled","old_multi_enum_values.name","old_name","old_number_value","old_people_value","old_people_value.name","old_resource_subtype","old_section","old_section.name","old_text_value","previews","previews.fallback","previews.footer","previews.header","previews.header_link","previews.html_text","previews.text","previews.title","previews.title_link","project","project.name","resource_subtype","source","sticker_name","story","story.created_at","story.created_by","story.created_by.name","story.resource_subtype","story.text","tag","tag.name","target","target.name","target.resource_subtype","task","task.name","task.resource_subtype","text","type"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Create a story on a task
    api_response = api_instance.create_story_for_task(body, task_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling StoriesApi->create_story_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TaskGidStoriesBody**](TaskGidStoriesBody.md)| The story to create. | 
 **task_gid** | **str**| The task to operate on. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**StoryResponseData**](StoryResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_story**
> EmptyResponseData delete_story(story_gid)

Delete a story

Deletes a story. A user can only delete stories they have created.  Returns an empty data record.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.StoriesApi(asana.ApiClient(configuration))
story_gid = '35678' # str | Globally unique identifier for the story.

try:
    # Delete a story
    api_response = api_instance.delete_story(story_gid)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling StoriesApi->delete_story: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_gid** | **str**| Globally unique identifier for the story. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stories_for_task**
> StoryResponseArray get_stories_for_task(task_gid, limit=limit, offset=offset, opt_fields=opt_fields)

Get stories from a task

Returns the compact records for all stories on the task.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.StoriesApi(asana.ApiClient(configuration))
task_gid = '321654' # str | The task to operate on.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["assignee","assignee.name","created_at","created_by","created_by.name","custom_field","custom_field.date_value","custom_field.date_value.date","custom_field.date_value.date_time","custom_field.display_value","custom_field.enabled","custom_field.enum_options","custom_field.enum_options.color","custom_field.enum_options.enabled","custom_field.enum_options.name","custom_field.enum_value","custom_field.enum_value.color","custom_field.enum_value.enabled","custom_field.enum_value.name","custom_field.is_formula_field","custom_field.multi_enum_values","custom_field.multi_enum_values.color","custom_field.multi_enum_values.enabled","custom_field.multi_enum_values.name","custom_field.name","custom_field.number_value","custom_field.resource_subtype","custom_field.text_value","custom_field.type","dependency","dependency.name","dependency.resource_subtype","duplicate_of","duplicate_of.name","duplicate_of.resource_subtype","duplicated_from","duplicated_from.name","duplicated_from.resource_subtype","follower","follower.name","hearted","hearts","hearts.user","hearts.user.name","html_text","is_editable","is_edited","is_pinned","liked","likes","likes.user","likes.user.name","new_approval_status","new_date_value","new_dates","new_dates.due_at","new_dates.due_on","new_dates.start_on","new_enum_value","new_enum_value.color","new_enum_value.enabled","new_enum_value.name","new_multi_enum_values","new_multi_enum_values.color","new_multi_enum_values.enabled","new_multi_enum_values.name","new_name","new_number_value","new_people_value","new_people_value.name","new_resource_subtype","new_section","new_section.name","new_text_value","num_hearts","num_likes","offset","old_approval_status","old_date_value","old_dates","old_dates.due_at","old_dates.due_on","old_dates.start_on","old_enum_value","old_enum_value.color","old_enum_value.enabled","old_enum_value.name","old_multi_enum_values","old_multi_enum_values.color","old_multi_enum_values.enabled","old_multi_enum_values.name","old_name","old_number_value","old_people_value","old_people_value.name","old_resource_subtype","old_section","old_section.name","old_text_value","path","previews","previews.fallback","previews.footer","previews.header","previews.header_link","previews.html_text","previews.text","previews.title","previews.title_link","project","project.name","resource_subtype","source","sticker_name","story","story.created_at","story.created_by","story.created_by.name","story.resource_subtype","story.text","tag","tag.name","target","target.name","target.resource_subtype","task","task.name","task.resource_subtype","text","type","uri"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get stories from a task
    api_response = api_instance.get_stories_for_task(task_gid, limit=limit, offset=offset, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling StoriesApi->get_stories_for_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_gid** | **str**| The task to operate on. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**StoryResponseArray**](StoryResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_story**
> StoryResponseData get_story(story_gid, opt_fields=opt_fields)

Get a story

Returns the full record for a single story.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.StoriesApi(asana.ApiClient(configuration))
story_gid = '35678' # str | Globally unique identifier for the story.
opt_fields = ["assignee","assignee.name","created_at","created_by","created_by.name","custom_field","custom_field.date_value","custom_field.date_value.date","custom_field.date_value.date_time","custom_field.display_value","custom_field.enabled","custom_field.enum_options","custom_field.enum_options.color","custom_field.enum_options.enabled","custom_field.enum_options.name","custom_field.enum_value","custom_field.enum_value.color","custom_field.enum_value.enabled","custom_field.enum_value.name","custom_field.is_formula_field","custom_field.multi_enum_values","custom_field.multi_enum_values.color","custom_field.multi_enum_values.enabled","custom_field.multi_enum_values.name","custom_field.name","custom_field.number_value","custom_field.resource_subtype","custom_field.text_value","custom_field.type","dependency","dependency.name","dependency.resource_subtype","duplicate_of","duplicate_of.name","duplicate_of.resource_subtype","duplicated_from","duplicated_from.name","duplicated_from.resource_subtype","follower","follower.name","hearted","hearts","hearts.user","hearts.user.name","html_text","is_editable","is_edited","is_pinned","liked","likes","likes.user","likes.user.name","new_approval_status","new_date_value","new_dates","new_dates.due_at","new_dates.due_on","new_dates.start_on","new_enum_value","new_enum_value.color","new_enum_value.enabled","new_enum_value.name","new_multi_enum_values","new_multi_enum_values.color","new_multi_enum_values.enabled","new_multi_enum_values.name","new_name","new_number_value","new_people_value","new_people_value.name","new_resource_subtype","new_section","new_section.name","new_text_value","num_hearts","num_likes","old_approval_status","old_date_value","old_dates","old_dates.due_at","old_dates.due_on","old_dates.start_on","old_enum_value","old_enum_value.color","old_enum_value.enabled","old_enum_value.name","old_multi_enum_values","old_multi_enum_values.color","old_multi_enum_values.enabled","old_multi_enum_values.name","old_name","old_number_value","old_people_value","old_people_value.name","old_resource_subtype","old_section","old_section.name","old_text_value","previews","previews.fallback","previews.footer","previews.header","previews.header_link","previews.html_text","previews.text","previews.title","previews.title_link","project","project.name","resource_subtype","source","sticker_name","story","story.created_at","story.created_by","story.created_by.name","story.resource_subtype","story.text","tag","tag.name","target","target.name","target.resource_subtype","task","task.name","task.resource_subtype","text","type"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Get a story
    api_response = api_instance.get_story(story_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling StoriesApi->get_story: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **story_gid** | **str**| Globally unique identifier for the story. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**StoryResponseData**](StoryResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_story**
> StoryResponseData update_story(body, story_gid, opt_fields=opt_fields)

Update a story

Updates the story and returns the full record for the updated story. Only comment stories can have their text updated, and only comment stories and attachment stories can be pinned. Only one of `text` and `html_text` can be specified.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.StoriesApi(asana.ApiClient(configuration))
body = asana.StoriesStoryGidBody({"param1": "value1", "param2": "value2",}) # StoriesStoryGidBody | The comment story to update.
story_gid = '35678' # str | Globally unique identifier for the story.
opt_fields = ["assignee","assignee.name","created_at","created_by","created_by.name","custom_field","custom_field.date_value","custom_field.date_value.date","custom_field.date_value.date_time","custom_field.display_value","custom_field.enabled","custom_field.enum_options","custom_field.enum_options.color","custom_field.enum_options.enabled","custom_field.enum_options.name","custom_field.enum_value","custom_field.enum_value.color","custom_field.enum_value.enabled","custom_field.enum_value.name","custom_field.is_formula_field","custom_field.multi_enum_values","custom_field.multi_enum_values.color","custom_field.multi_enum_values.enabled","custom_field.multi_enum_values.name","custom_field.name","custom_field.number_value","custom_field.resource_subtype","custom_field.text_value","custom_field.type","dependency","dependency.name","dependency.resource_subtype","duplicate_of","duplicate_of.name","duplicate_of.resource_subtype","duplicated_from","duplicated_from.name","duplicated_from.resource_subtype","follower","follower.name","hearted","hearts","hearts.user","hearts.user.name","html_text","is_editable","is_edited","is_pinned","liked","likes","likes.user","likes.user.name","new_approval_status","new_date_value","new_dates","new_dates.due_at","new_dates.due_on","new_dates.start_on","new_enum_value","new_enum_value.color","new_enum_value.enabled","new_enum_value.name","new_multi_enum_values","new_multi_enum_values.color","new_multi_enum_values.enabled","new_multi_enum_values.name","new_name","new_number_value","new_people_value","new_people_value.name","new_resource_subtype","new_section","new_section.name","new_text_value","num_hearts","num_likes","old_approval_status","old_date_value","old_dates","old_dates.due_at","old_dates.due_on","old_dates.start_on","old_enum_value","old_enum_value.color","old_enum_value.enabled","old_enum_value.name","old_multi_enum_values","old_multi_enum_values.color","old_multi_enum_values.enabled","old_multi_enum_values.name","old_name","old_number_value","old_people_value","old_people_value.name","old_resource_subtype","old_section","old_section.name","old_text_value","previews","previews.fallback","previews.footer","previews.header","previews.header_link","previews.html_text","previews.text","previews.title","previews.title_link","project","project.name","resource_subtype","source","sticker_name","story","story.created_at","story.created_by","story.created_by.name","story.resource_subtype","story.text","tag","tag.name","target","target.name","target.resource_subtype","task","task.name","task.resource_subtype","text","type"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
    # Update a story
    api_response = api_instance.update_story(body, story_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling StoriesApi->update_story: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StoriesStoryGidBody**](StoriesStoryGidBody.md)| The comment story to update. | 
 **story_gid** | **str**| Globally unique identifier for the story. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**StoryResponseData**](StoryResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

