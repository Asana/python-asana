# asana.AttachmentsApi

All URIs are relative to *https://app.asana.com/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_attachment_for_object**](AttachmentsApi.md#create_attachment_for_object) | **POST** /attachments | Upload an attachment
[**delete_attachment**](AttachmentsApi.md#delete_attachment) | **DELETE** /attachments/{attachment_gid} | Delete an attachment
[**get_attachment**](AttachmentsApi.md#get_attachment) | **GET** /attachments/{attachment_gid} | Get an attachment
[**get_attachments_for_object**](AttachmentsApi.md#get_attachments_for_object) | **GET** /attachments | Get attachments from an object

# **create_attachment_for_object**

Upload an attachment

Upload an attachment.  This method uploads an attachment on an object and returns the compact record for the created attachment object. This is possible by either:  - Providing the URL of the external resource being attached, or - Downloading the file content first and then uploading it as any other attachment. Note that it is not possible to attach files from third party services such as Dropbox, Box, Vimeo & Google Drive via the API  The 100MB size limit on attachments in Asana is enforced on this endpoint.  This endpoint expects a multipart/form-data encoded request containing the full contents of the file to be uploaded.  Requests made should follow the HTTP/1.1 specification that line terminators are of the form `CRLF` or `\\r\\n` outlined [here](http://www.w3.org/Protocols/HTTP/1.1/draft-ietf-http-v11-spec-01#Basic-Rules) in order for the server to reliably and properly handle the request.  For file names that contain non-ASCII characters, the file name should be URL-encoded. For example, a file named `résumé.pdf` should be encoded as `r%C3%A9sum%C3%A9.pdf` and the `filename` parameter in the `Content-Disposition` header should be set to the encoded file name.  Below is an example of a cURL request with the `Content-Disposition` header:  ``` export ASANA_PAT=\"<YOUR_ASANA_PERSONAL_ACCESS_TOKEN>\" export PARENT_ID=\"<PARENT_GID>\" export ENCODED_NAME=\"r%C3%A9sum%C3%A9.pdf\" curl --location 'https://app.asana.com/api/1.0/attachments' \\   --header 'Content-Type: multipart/form-data' \\   --header 'Accept: application/json' \\   --header \"Authorization: Bearer $ASANA_PAT\" \\   --form \"parent=$PARENT_ID\" \\   --form \"file=@/Users/exampleUser/Downloads/résumé.pdf;headers=\\\"Content-Disposition: form-data; name=\"file\"; filename=\"$ENCODED_NAME.pdf\"; filename*=UTF-8''$ENCODED_NAME.pdf\\\"\" ```

([more information](https://developers.asana.com/reference/createattachmentforobject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
attachments_api_instance = asana.AttachmentsApi(api_client)
opts = {
    'resource_subtype': "external", # str | 
    'file': "file_example", # str | 
    'parent': "parent_example", # str | 
    'url': "url_example", # str | 
    'name': "name_example", # str | 
    'connect_to_app': True, # bool | 
    'opt_fields': "connected_to_app,created_at,download_url,host,name,parent,parent.created_by,parent.name,parent.resource_subtype,permanent_url,resource_subtype,size,view_url", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Upload an attachment
    api_response = attachments_api_instance.create_attachment_for_object(opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->create_attachment_for_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_subtype** | **str**|  | [optional] 
 **file** | **str**|  | [optional] 
 **parent** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **connect_to_app** | **bool**|  | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **delete_attachment**

Delete an attachment

Deletes a specific, existing attachment.  Returns an empty data record.

([more information](https://developers.asana.com/reference/deleteattachment))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
attachments_api_instance = asana.AttachmentsApi(api_client)
attachment_gid = "12345" # str | Globally unique identifier for the attachment.


try:
    # Delete an attachment
    api_response = attachments_api_instance.delete_attachment(attachment_gid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->delete_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_gid** | **str**| Globally unique identifier for the attachment. | 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_attachment**

Get an attachment

Get the full record for a single attachment.

([more information](https://developers.asana.com/reference/getattachment))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
attachments_api_instance = asana.AttachmentsApi(api_client)
attachment_gid = "12345" # str | Globally unique identifier for the attachment.
opts = {
    'opt_fields': "connected_to_app,created_at,download_url,host,name,parent,parent.created_by,parent.name,parent.resource_subtype,permanent_url,resource_subtype,size,view_url", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get an attachment
    api_response = attachments_api_instance.get_attachment(attachment_gid, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->get_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_gid** | **str**| Globally unique identifier for the attachment. | 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

dict

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

# **get_attachments_for_object**

Get attachments from an object

Returns the compact records for all attachments on the object.  There are three possible `parent` values for this request: `project`, `project_brief`, and `task`. For a project, an attachment refers to a file uploaded to the \"Key resources\" section in the project Overview. For a project brief, an attachment refers to inline files in the project brief itself. For a task, an attachment refers to a file directly associated to that task.  Note that within the Asana app, inline images in the task description do not appear in the index of image thumbnails nor as stories in the task. However, requests made to `GET /attachments` for a task will return all of the images in the task, including inline images.

([more information](https://developers.asana.com/reference/getattachmentsforobject))

### Example
```python
import asana
from asana.rest import ApiException
from pprint import pprint

configuration = asana.Configuration()
configuration.access_token = '<YOUR_ACCESS_TOKEN>'
api_client = asana.ApiClient(configuration)

# create an instance of the API class
attachments_api_instance = asana.AttachmentsApi(api_client)
parent = "159874" # str | Globally unique identifier for object to fetch statuses from. Must be a GID for a `project`, `project_brief`, or `task`.
opts = {
    'limit': 50, # int | Results per page. The number of objects to return per page. The value must be between 1 and 100.
    'offset': "eyJ0eXAiOJiKV1iQLCJhbGciOiJIUzI1NiJ9", # str | Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
    'opt_fields': "connected_to_app,created_at,download_url,host,name,offset,parent,parent.created_by,parent.name,parent.resource_subtype,path,permanent_url,resource_subtype,size,uri,view_url", # list[str] | This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
}

try:
    # Get attachments from an object
    api_response = attachments_api_instance.get_attachments_for_object(parent, opts)
    for data in api_response:
        pprint(data)
except ApiException as e:
    print("Exception when calling AttachmentsApi->get_attachments_for_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| Globally unique identifier for object to fetch statuses from. Must be a GID for a &#x60;project&#x60;, &#x60;project_brief&#x60;, or &#x60;task&#x60;. | 
 **limit** | **int**| Results per page. The number of objects to return per page. The value must be between 1 and 100. | [optional] 
 **offset** | **str**| Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.* | [optional] 
 **opt_fields** | **Dict**| This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include. | [optional] 

### Return type

generator

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

