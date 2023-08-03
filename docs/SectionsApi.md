# asana.SectionsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_task_for_section**](SectionsApi.md#add_task_for_section) | **POST** /sections/{section_gid}/addTask | Add task to section
[**create_section_for_project**](SectionsApi.md#create_section_for_project) | **POST** /projects/{project_gid}/sections | Create a section in a project
[**delete_section**](SectionsApi.md#delete_section) | **DELETE** /sections/{section_gid} | Delete a section
[**get_section**](SectionsApi.md#get_section) | **GET** /sections/{section_gid} | Get a section
[**get_sections_for_project**](SectionsApi.md#get_sections_for_project) | **GET** /projects/{project_gid}/sections | Get sections in a project
[**insert_section_for_project**](SectionsApi.md#insert_section_for_project) | **POST** /projects/{project_gid}/sections/insert | Move or Insert sections
[**update_section**](SectionsApi.md#update_section) | **PUT** /sections/{section_gid} | Update a section

# **add_task_for_section**
> EmptyResponseData add_task_for_section(section_gid, body=body)

Add task to section

Add a task to a specific, existing section. This will remove the task from other sections of the project.  The task will be inserted at the top of a section unless an insert_before or insert_after parameter is declared.  This does not work for separators (tasks with the resource_subtype of section).

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.SectionsApi(asana.ApiClient(configuration))
section_gid = '321654' # str | The globally unique identifier for the section.
body = asana.SectionGidAddTaskBody({"param1": "value1", "param2": "value2",}) # SectionGidAddTaskBody | The task and optionally the insert location. (optional)

try:
  # Add task to section
  api_response = api_instance.add_task_for_section(section_gid, body=body)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling SectionsApi->add_task_for_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_gid** | **str**| The globally unique identifier for the section. | 
 **body** | [**SectionGidAddTaskBody**](SectionGidAddTaskBody.md)| The task and optionally the insert location. | [optional] 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_section_for_project**
> SectionResponseData create_section_for_project(project_gid, body=body, opt_fields=opt_fields)

Create a section in a project

Creates a new section in a project. Returns the full record of the newly created section.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.SectionsApi(asana.ApiClient(configuration))
project_gid = '1331' # str | Globally unique identifier for the project.
body = asana.ProjectGidSectionsBody({"param1": "value1", "param2": "value2",}) # ProjectGidSectionsBody | The section to create. (optional)
opt_fields = ["created_at","name","project","project.name","projects","projects.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Create a section in a project
  api_response = api_instance.create_section_for_project(project_gid, body=body, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling SectionsApi->create_section_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **body** | [**ProjectGidSectionsBody**](ProjectGidSectionsBody.md)| The section to create. | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**SectionResponseData**](SectionResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_section**
> EmptyResponseData delete_section(section_gid)

Delete a section

A specific, existing section can be deleted by making a DELETE request on the URL for that section.  Note that sections must be empty to be deleted.  The last remaining section cannot be deleted.  Returns an empty data block.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.SectionsApi(asana.ApiClient(configuration))
section_gid = '321654' # str | The globally unique identifier for the section.

try:
  # Delete a section
  api_response = api_instance.delete_section(section_gid)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling SectionsApi->delete_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_gid** | **str**| The globally unique identifier for the section. | 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section**
> SectionResponseData get_section(section_gid, opt_fields=opt_fields)

Get a section

Returns the complete record for a single section.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.SectionsApi(asana.ApiClient(configuration))
section_gid = '321654' # str | The globally unique identifier for the section.
opt_fields = ["created_at","name","project","project.name","projects","projects.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get a section
  api_response = api_instance.get_section(section_gid, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling SectionsApi->get_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_gid** | **str**| The globally unique identifier for the section. | 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**SectionResponseData**](SectionResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sections_for_project**
> SectionResponseArray get_sections_for_project(project_gid, limit=limit, offset=offset, opt_fields=opt_fields)

Get sections in a project

Returns the compact records for all sections in the specified project.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.SectionsApi(asana.ApiClient(configuration))
project_gid = '1331' # str | Globally unique identifier for the project.
limit = 50 # int | Results per page. The number of objects to return per page. The value must be between 1 and 100. (optional)
offset = 'eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9' # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.' (optional)
opt_fields = ["created_at","name","offset","path","project","project.name","projects","projects.name","uri"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Get sections in a project
  api_response = api_instance.get_sections_for_project(project_gid, limit=limit, offset=offset, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling SectionsApi->get_sections_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#x27;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#x27; | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**SectionResponseArray**](SectionResponseArray.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_section_for_project**
> EmptyResponseData insert_section_for_project(project_gid, body=body)

Move or Insert sections

Move sections relative to each other. One of `before_section` or `after_section` is required.  Sections cannot be moved between projects.  Returns an empty data block.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.SectionsApi(asana.ApiClient(configuration))
project_gid = '1331' # str | Globally unique identifier for the project.
body = asana.SectionsInsertBody({"param1": "value1", "param2": "value2",}) # SectionsInsertBody | The section's move action. (optional)

try:
  # Move or Insert sections
  api_response = api_instance.insert_section_for_project(project_gid, body=body)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling SectionsApi->insert_section_for_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_gid** | **str**| Globally unique identifier for the project. | 
 **body** | [**SectionsInsertBody**](SectionsInsertBody.md)| The section&#x27;s move action. | [optional] 

### Return type

[**EmptyResponseData**](EmptyResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_section**
> SectionResponseData update_section(section_gid, body=body, opt_fields=opt_fields)

Update a section

A specific, existing section can be updated by making a PUT request on the URL for that project. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged. (note that at this time, the only field that can be updated is the `name` field.)  When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the task.  Returns the complete updated section record.

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = asana.Configuration()
configuration.access_token = '<YOUR_PERSONAL_ACCESS_TOKEN>'

# create an instance of the API class
api_instance = asana.SectionsApi(asana.ApiClient(configuration))
section_gid = '321654' # str | The globally unique identifier for the section.
body = asana.SectionsSectionGidBody({"param1": "value1", "param2": "value2",}) # SectionsSectionGidBody | The section to create. (optional)
opt_fields = ["created_at","name","project","project.name","projects","projects.name"] # list[str] | This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. (optional)

try:
  # Update a section
  api_response = api_instance.update_section(section_gid, body=body, opt_fields=opt_fields)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling SectionsApi->update_section: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_gid** | **str**| The globally unique identifier for the section. | 
 **body** | [**SectionsSectionGidBody**](SectionsSectionGidBody.md)| The section to create. | [optional] 
 **opt_fields** | [**list[str]**](str.md)| This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

[**SectionResponseData**](SectionResponseData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json; charset=UTF-8
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

