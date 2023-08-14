# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from asana.api_client import ApiClient


class AttachmentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

def __init__(self, api_client=None):
    if api_client is None:
        api_client = ApiClient()
    self.api_client = api_client

def create_attachment_for_object(self, **kwargs):  # noqa: E501
    """Upload an attachment  # noqa: E501

    Upload an attachment.  This method uploads an attachment on an object and returns the compact record for the created attachment object. This is possible by either:  - Providing the URL of the external resource being attached, or - Downloading the file content first and then uploading it as any other attachment. Note that it is not possible to attach files from third party services such as Dropbox, Box, Vimeo & Google Drive via the API  The 100MB size limit on attachments in Asana is enforced on this endpoint.  This endpoint expects a multipart/form-data encoded request containing the full contents of the file to be uploaded.  Requests made should follow the HTTP/1.1 specification that line terminators are of the form `CRLF` or `\\r\\n` outlined [here](http://www.w3.org/Protocols/HTTP/1.1/draft-ietf-http-v11-spec-01#Basic-Rules) in order for the server to reliably and properly handle the request.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.create_attachment_for_object(async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str resource_subtype:
    :param str file:
    :param str parent:
    :param str url:
    :param str name:
    :param bool connect_to_app:
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: AttachmentResponseData
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.create_attachment_for_object_with_http_info(**kwargs)  # noqa: E501
    else:
        (data) = self.create_attachment_for_object_with_http_info(**kwargs)  # noqa: E501
        return data

def create_attachment_for_object_with_http_info(self, **kwargs):  # noqa: E501
    """Upload an attachment  # noqa: E501

    Upload an attachment.  This method uploads an attachment on an object and returns the compact record for the created attachment object. This is possible by either:  - Providing the URL of the external resource being attached, or - Downloading the file content first and then uploading it as any other attachment. Note that it is not possible to attach files from third party services such as Dropbox, Box, Vimeo & Google Drive via the API  The 100MB size limit on attachments in Asana is enforced on this endpoint.  This endpoint expects a multipart/form-data encoded request containing the full contents of the file to be uploaded.  Requests made should follow the HTTP/1.1 specification that line terminators are of the form `CRLF` or `\\r\\n` outlined [here](http://www.w3.org/Protocols/HTTP/1.1/draft-ietf-http-v11-spec-01#Basic-Rules) in order for the server to reliably and properly handle the request.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.create_attachment_for_object_with_http_info(async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str resource_subtype:
    :param str file:
    :param str parent:
    :param str url:
    :param str name:
    :param bool connect_to_app:
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: AttachmentResponseData
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['resource_subtype', 'file', 'parent', 'url', 'name', 'connect_to_app', 'opt_fields']  # noqa: E501
    all_params.append('async_req')
    all_params.append('header_params')
    all_params.append('_return_http_data_only')
    all_params.append('_preload_content')
    all_params.append('_request_timeout')

    params = locals()
    for key, val in six.iteritems(params['kwargs']):
        if key not in all_params:
            raise TypeError(
                "Got an unexpected keyword argument '%s'"
                " to method create_attachment_for_object" % key
            )
        params[key] = val
    del params['kwargs']

    collection_formats = {}

    path_params = {}

    query_params = []
    if 'opt_fields' in params:
        query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
        collection_formats['opt_fields'] = 'csv'  # noqa: E501

    header_params = kwargs.get("header_params", {})

    form_params = []
    local_var_files = {}
    if 'resource_subtype' in params:
        form_params.append(('resource_subtype', params['resource_subtype']))  # noqa: E501
    if 'file' in params:
        local_var_files['file'] = params['file']  # noqa: E501
    if 'parent' in params:
        form_params.append(('parent', params['parent']))  # noqa: E501
    if 'url' in params:
        form_params.append(('url', params['url']))  # noqa: E501
    if 'name' in params:
        form_params.append(('name', params['name']))  # noqa: E501
    if 'connect_to_app' in params:
        form_params.append(('connect_to_app', params['connect_to_app']))  # noqa: E501

    body_params = None
    # HTTP header `Accept`
    header_params['Accept'] = self.api_client.select_header_accept(
        ['application/json; charset=UTF-8'])  # noqa: E501

    # HTTP header `Content-Type`
    header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
        ['multipart/form-data'])  # noqa: E501

    # Authentication setting
    auth_settings = ['oauth2']  # noqa: E501

    return self.api_client.call_api(
        '/attachments', 'POST',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='AttachmentResponseData',  # noqa: E501
        auth_settings=auth_settings,
        async_req=params.get('async_req'),
        _return_http_data_only=params.get('_return_http_data_only'),
        _preload_content=params.get('_preload_content', True),
        _request_timeout=params.get('_request_timeout'),
        collection_formats=collection_formats)

def delete_attachment(self, attachment_gid, **kwargs):  # noqa: E501
    """Delete an attachment  # noqa: E501

    Deletes a specific, existing attachment.  Returns an empty data record.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.delete_attachment(attachment_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str attachment_gid: Globally unique identifier for the attachment. (required)
    :return: EmptyResponseData
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.delete_attachment_with_http_info(attachment_gid, **kwargs)  # noqa: E501
    else:
        (data) = self.delete_attachment_with_http_info(attachment_gid, **kwargs)  # noqa: E501
        return data

def delete_attachment_with_http_info(self, attachment_gid, **kwargs):  # noqa: E501
    """Delete an attachment  # noqa: E501

    Deletes a specific, existing attachment.  Returns an empty data record.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.delete_attachment_with_http_info(attachment_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str attachment_gid: Globally unique identifier for the attachment. (required)
    :return: EmptyResponseData
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['attachment_gid']  # noqa: E501
    all_params.append('async_req')
    all_params.append('header_params')
    all_params.append('_return_http_data_only')
    all_params.append('_preload_content')
    all_params.append('_request_timeout')

    params = locals()
    for key, val in six.iteritems(params['kwargs']):
        if key not in all_params:
            raise TypeError(
                "Got an unexpected keyword argument '%s'"
                " to method delete_attachment" % key
            )
        params[key] = val
    del params['kwargs']
    # verify the required parameter 'attachment_gid' is set
    if ('attachment_gid' not in params or
            params['attachment_gid'] is None):
        raise ValueError("Missing the required parameter `attachment_gid` when calling `delete_attachment`")  # noqa: E501

    collection_formats = {}

    path_params = {}
    if 'attachment_gid' in params:
        path_params['attachment_gid'] = params['attachment_gid']  # noqa: E501

    query_params = []

    header_params = kwargs.get("header_params", {})

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params['Accept'] = self.api_client.select_header_accept(
        ['application/json; charset=UTF-8'])  # noqa: E501

    # Authentication setting
    auth_settings = ['oauth2']  # noqa: E501

    return self.api_client.call_api(
        '/attachments/{attachment_gid}', 'DELETE',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='EmptyResponseData',  # noqa: E501
        auth_settings=auth_settings,
        async_req=params.get('async_req'),
        _return_http_data_only=params.get('_return_http_data_only'),
        _preload_content=params.get('_preload_content', True),
        _request_timeout=params.get('_request_timeout'),
        collection_formats=collection_formats)

def get_attachment(self, attachment_gid, **kwargs):  # noqa: E501
    """Get an attachment  # noqa: E501

    Get the full record for a single attachment.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_attachment(attachment_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str attachment_gid: Globally unique identifier for the attachment. (required)
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: AttachmentResponseData
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.get_attachment_with_http_info(attachment_gid, **kwargs)  # noqa: E501
    else:
        (data) = self.get_attachment_with_http_info(attachment_gid, **kwargs)  # noqa: E501
        return data

def get_attachment_with_http_info(self, attachment_gid, **kwargs):  # noqa: E501
    """Get an attachment  # noqa: E501

    Get the full record for a single attachment.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_attachment_with_http_info(attachment_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str attachment_gid: Globally unique identifier for the attachment. (required)
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: AttachmentResponseData
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['attachment_gid', 'opt_fields']  # noqa: E501
    all_params.append('async_req')
    all_params.append('header_params')
    all_params.append('_return_http_data_only')
    all_params.append('_preload_content')
    all_params.append('_request_timeout')

    params = locals()
    for key, val in six.iteritems(params['kwargs']):
        if key not in all_params:
            raise TypeError(
                "Got an unexpected keyword argument '%s'"
                " to method get_attachment" % key
            )
        params[key] = val
    del params['kwargs']
    # verify the required parameter 'attachment_gid' is set
    if ('attachment_gid' not in params or
            params['attachment_gid'] is None):
        raise ValueError("Missing the required parameter `attachment_gid` when calling `get_attachment`")  # noqa: E501

    collection_formats = {}

    path_params = {}
    if 'attachment_gid' in params:
        path_params['attachment_gid'] = params['attachment_gid']  # noqa: E501

    query_params = []
    if 'opt_fields' in params:
        query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
        collection_formats['opt_fields'] = 'csv'  # noqa: E501

    header_params = kwargs.get("header_params", {})

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params['Accept'] = self.api_client.select_header_accept(
        ['application/json; charset=UTF-8'])  # noqa: E501

    # Authentication setting
    auth_settings = ['oauth2']  # noqa: E501

    return self.api_client.call_api(
        '/attachments/{attachment_gid}', 'GET',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='AttachmentResponseData',  # noqa: E501
        auth_settings=auth_settings,
        async_req=params.get('async_req'),
        _return_http_data_only=params.get('_return_http_data_only'),
        _preload_content=params.get('_preload_content', True),
        _request_timeout=params.get('_request_timeout'),
        collection_formats=collection_formats)

def get_attachments_for_object(self, parent, **kwargs):  # noqa: E501
    """Get attachments from an object  # noqa: E501

    Returns the compact records for all attachments on the object.  There are three possible `parent` values for this request: `project`, `project_brief`, and `task`. For a project, an attachment refers to a file uploaded to the \"Key resources\" section in the project Overview. For a project brief, an attachment refers to inline files in the project brief itself. For a task, an attachment refers to a file directly associated to that task.  Note that within the Asana app, inline images in the task description do not appear in the index of image thumbnails nor as stories in the task. However, requests made to `GET /attachments` for a task will return all of the images in the task, including inline images.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_attachments_for_object(parent, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str parent: Globally unique identifier for object to fetch statuses from. Must be a GID for a `project`, `project_brief`, or `task`. (required)
    :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: AttachmentResponseArray
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.get_attachments_for_object_with_http_info(parent, **kwargs)  # noqa: E501
    else:
        (data) = self.get_attachments_for_object_with_http_info(parent, **kwargs)  # noqa: E501
        return data

def get_attachments_for_object_with_http_info(self, parent, **kwargs):  # noqa: E501
    """Get attachments from an object  # noqa: E501

    Returns the compact records for all attachments on the object.  There are three possible `parent` values for this request: `project`, `project_brief`, and `task`. For a project, an attachment refers to a file uploaded to the \"Key resources\" section in the project Overview. For a project brief, an attachment refers to inline files in the project brief itself. For a task, an attachment refers to a file directly associated to that task.  Note that within the Asana app, inline images in the task description do not appear in the index of image thumbnails nor as stories in the task. However, requests made to `GET /attachments` for a task will return all of the images in the task, including inline images.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_attachments_for_object_with_http_info(parent, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str parent: Globally unique identifier for object to fetch statuses from. Must be a GID for a `project`, `project_brief`, or `task`. (required)
    :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: AttachmentResponseArray
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['parent', 'limit', 'offset', 'opt_fields']  # noqa: E501
    all_params.append('async_req')
    all_params.append('header_params')
    all_params.append('_return_http_data_only')
    all_params.append('_preload_content')
    all_params.append('_request_timeout')

    params = locals()
    for key, val in six.iteritems(params['kwargs']):
        if key not in all_params:
            raise TypeError(
                "Got an unexpected keyword argument '%s'"
                " to method get_attachments_for_object" % key
            )
        params[key] = val
    del params['kwargs']
    # verify the required parameter 'parent' is set
    if ('parent' not in params or
            params['parent'] is None):
        raise ValueError("Missing the required parameter `parent` when calling `get_attachments_for_object`")  # noqa: E501

    collection_formats = {}

    path_params = {}

    query_params = []
    if 'limit' in params:
        query_params.append(('limit', params['limit']))  # noqa: E501
    if 'offset' in params:
        query_params.append(('offset', params['offset']))  # noqa: E501
    if 'parent' in params:
        query_params.append(('parent', params['parent']))  # noqa: E501
    if 'opt_fields' in params:
        query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
        collection_formats['opt_fields'] = 'csv'  # noqa: E501

    header_params = kwargs.get("header_params", {})

    form_params = []
    local_var_files = {}

    body_params = None
    # HTTP header `Accept`
    header_params['Accept'] = self.api_client.select_header_accept(
        ['application/json; charset=UTF-8'])  # noqa: E501

    # Authentication setting
    auth_settings = ['oauth2']  # noqa: E501

    return self.api_client.call_api(
        '/attachments', 'GET',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='AttachmentResponseArray',  # noqa: E501
        auth_settings=auth_settings,
        async_req=params.get('async_req'),
        _return_http_data_only=params.get('_return_http_data_only'),
        _preload_content=params.get('_preload_content', True),
        _request_timeout=params.get('_request_timeout'),
        collection_formats=collection_formats)
