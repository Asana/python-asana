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


class StoriesApi(object):
"""NOTE: This class is auto generated by the swagger code generator program.

Do not edit the class manually.
Ref: https://github.com/swagger-api/swagger-codegen
"""

def __init__(self, api_client=None):
    if api_client is None:
        api_client = ApiClient()
    self.api_client = api_client

def create_story_for_task(self, body, task_gid, **kwargs):  # noqa: E501
    """Create a story on a task  # noqa: E501

    Adds a story to a task. This endpoint currently only allows for comment stories to be created. The comment will be authored by the currently authenticated user, and timestamped when the server receives the request.  Returns the full record for the new story added to the task.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.create_story_for_task(body, task_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param TaskGidStoriesBody body: The story to create. (required)
    :param str task_gid: The task to operate on. (required)
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: StoryResponseData
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.create_story_for_task_with_http_info(body, task_gid, **kwargs)  # noqa: E501
    else:
        (data) = self.create_story_for_task_with_http_info(body, task_gid, **kwargs)  # noqa: E501
        return data

def create_story_for_task_with_http_info(self, body, task_gid, **kwargs):  # noqa: E501
    """Create a story on a task  # noqa: E501

    Adds a story to a task. This endpoint currently only allows for comment stories to be created. The comment will be authored by the currently authenticated user, and timestamped when the server receives the request.  Returns the full record for the new story added to the task.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.create_story_for_task_with_http_info(body, task_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param TaskGidStoriesBody body: The story to create. (required)
    :param str task_gid: The task to operate on. (required)
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: StoryResponseData
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['body', 'task_gid', 'opt_fields']  # noqa: E501
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
                " to method create_story_for_task" % key
            )
        params[key] = val
    del params['kwargs']
    # verify the required parameter 'body' is set
    if ('body' not in params or
            params['body'] is None):
        raise ValueError("Missing the required parameter `body` when calling `create_story_for_task`")  # noqa: E501
    # verify the required parameter 'task_gid' is set
    if ('task_gid' not in params or
            params['task_gid'] is None):
        raise ValueError("Missing the required parameter `task_gid` when calling `create_story_for_task`")  # noqa: E501

    collection_formats = {}

    path_params = {}
    if 'task_gid' in params:
        path_params['task_gid'] = params['task_gid']  # noqa: E501

    query_params = []
    if 'opt_fields' in params:
        query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
        collection_formats['opt_fields'] = 'csv'  # noqa: E501

    header_params = kwargs.get("header_params", {})

    form_params = []
    local_var_files = {}

    body_params = None
    if 'body' in params:
        body_params = params['body']
    # HTTP header `Accept`
    header_params['Accept'] = self.api_client.select_header_accept(
        ['application/json; charset=UTF-8'])  # noqa: E501

    # HTTP header `Content-Type`
    header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
        ['application/json; charset=UTF-8'])  # noqa: E501

    # Authentication setting
    auth_settings = ['oauth2']  # noqa: E501

    return self.api_client.call_api(
        '/tasks/{task_gid}/stories', 'POST',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='StoryResponseData',  # noqa: E501
        auth_settings=auth_settings,
        async_req=params.get('async_req'),
        _return_http_data_only=params.get('_return_http_data_only'),
        _preload_content=params.get('_preload_content', True),
        _request_timeout=params.get('_request_timeout'),
        collection_formats=collection_formats)

def delete_story(self, story_gid, **kwargs):  # noqa: E501
    """Delete a story  # noqa: E501

    Deletes a story. A user can only delete stories they have created.  Returns an empty data record.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.delete_story(story_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str story_gid: Globally unique identifier for the story. (required)
    :return: EmptyResponseData
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.delete_story_with_http_info(story_gid, **kwargs)  # noqa: E501
    else:
        (data) = self.delete_story_with_http_info(story_gid, **kwargs)  # noqa: E501
        return data

def delete_story_with_http_info(self, story_gid, **kwargs):  # noqa: E501
    """Delete a story  # noqa: E501

    Deletes a story. A user can only delete stories they have created.  Returns an empty data record.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.delete_story_with_http_info(story_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str story_gid: Globally unique identifier for the story. (required)
    :return: EmptyResponseData
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['story_gid']  # noqa: E501
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
                " to method delete_story" % key
            )
        params[key] = val
    del params['kwargs']
    # verify the required parameter 'story_gid' is set
    if ('story_gid' not in params or
            params['story_gid'] is None):
        raise ValueError("Missing the required parameter `story_gid` when calling `delete_story`")  # noqa: E501

    collection_formats = {}

    path_params = {}
    if 'story_gid' in params:
        path_params['story_gid'] = params['story_gid']  # noqa: E501

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
        '/stories/{story_gid}', 'DELETE',
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

def get_stories_for_task(self, task_gid, **kwargs):  # noqa: E501
    """Get stories from a task  # noqa: E501

    Returns the compact records for all stories on the task.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_stories_for_task(task_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str task_gid: The task to operate on. (required)
    :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: StoryResponseArray
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.get_stories_for_task_with_http_info(task_gid, **kwargs)  # noqa: E501
    else:
        (data) = self.get_stories_for_task_with_http_info(task_gid, **kwargs)  # noqa: E501
        return data

def get_stories_for_task_with_http_info(self, task_gid, **kwargs):  # noqa: E501
    """Get stories from a task  # noqa: E501

    Returns the compact records for all stories on the task.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_stories_for_task_with_http_info(task_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str task_gid: The task to operate on. (required)
    :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: StoryResponseArray
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['task_gid', 'limit', 'offset', 'opt_fields']  # noqa: E501
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
                " to method get_stories_for_task" % key
            )
        params[key] = val
    del params['kwargs']
    # verify the required parameter 'task_gid' is set
    if ('task_gid' not in params or
            params['task_gid'] is None):
        raise ValueError("Missing the required parameter `task_gid` when calling `get_stories_for_task`")  # noqa: E501

    collection_formats = {}

    path_params = {}
    if 'task_gid' in params:
        path_params['task_gid'] = params['task_gid']  # noqa: E501

    query_params = []
    if 'limit' in params:
        query_params.append(('limit', params['limit']))  # noqa: E501
    if 'offset' in params:
        query_params.append(('offset', params['offset']))  # noqa: E501
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
        '/tasks/{task_gid}/stories', 'GET',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='StoryResponseArray',  # noqa: E501
        auth_settings=auth_settings,
        async_req=params.get('async_req'),
        _return_http_data_only=params.get('_return_http_data_only'),
        _preload_content=params.get('_preload_content', True),
        _request_timeout=params.get('_request_timeout'),
        collection_formats=collection_formats)

def get_story(self, story_gid, **kwargs):  # noqa: E501
    """Get a story  # noqa: E501

    Returns the full record for a single story.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_story(story_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str story_gid: Globally unique identifier for the story. (required)
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: StoryResponseData
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.get_story_with_http_info(story_gid, **kwargs)  # noqa: E501
    else:
        (data) = self.get_story_with_http_info(story_gid, **kwargs)  # noqa: E501
        return data

def get_story_with_http_info(self, story_gid, **kwargs):  # noqa: E501
    """Get a story  # noqa: E501

    Returns the full record for a single story.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.get_story_with_http_info(story_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param str story_gid: Globally unique identifier for the story. (required)
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: StoryResponseData
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['story_gid', 'opt_fields']  # noqa: E501
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
                " to method get_story" % key
            )
        params[key] = val
    del params['kwargs']
    # verify the required parameter 'story_gid' is set
    if ('story_gid' not in params or
            params['story_gid'] is None):
        raise ValueError("Missing the required parameter `story_gid` when calling `get_story`")  # noqa: E501

    collection_formats = {}

    path_params = {}
    if 'story_gid' in params:
        path_params['story_gid'] = params['story_gid']  # noqa: E501

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
        '/stories/{story_gid}', 'GET',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='StoryResponseData',  # noqa: E501
        auth_settings=auth_settings,
        async_req=params.get('async_req'),
        _return_http_data_only=params.get('_return_http_data_only'),
        _preload_content=params.get('_preload_content', True),
        _request_timeout=params.get('_request_timeout'),
        collection_formats=collection_formats)

def update_story(self, body, story_gid, **kwargs):  # noqa: E501
    """Update a story  # noqa: E501

    Updates the story and returns the full record for the updated story. Only comment stories can have their text updated, and only comment stories and attachment stories can be pinned. Only one of `text` and `html_text` can be specified.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.update_story(body, story_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param StoriesStoryGidBody body: The comment story to update. (required)
    :param str story_gid: Globally unique identifier for the story. (required)
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: StoryResponseData
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.update_story_with_http_info(body, story_gid, **kwargs)  # noqa: E501
    else:
        (data) = self.update_story_with_http_info(body, story_gid, **kwargs)  # noqa: E501
        return data

def update_story_with_http_info(self, body, story_gid, **kwargs):  # noqa: E501
    """Update a story  # noqa: E501

    Updates the story and returns the full record for the updated story. Only comment stories can have their text updated, and only comment stories and attachment stories can be pinned. Only one of `text` and `html_text` can be specified.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.update_story_with_http_info(body, story_gid, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param StoriesStoryGidBody body: The comment story to update. (required)
    :param str story_gid: Globally unique identifier for the story. (required)
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: StoryResponseData
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['body', 'story_gid', 'opt_fields']  # noqa: E501
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
                " to method update_story" % key
            )
        params[key] = val
    del params['kwargs']
    # verify the required parameter 'body' is set
    if ('body' not in params or
            params['body'] is None):
        raise ValueError("Missing the required parameter `body` when calling `update_story`")  # noqa: E501
    # verify the required parameter 'story_gid' is set
    if ('story_gid' not in params or
            params['story_gid'] is None):
        raise ValueError("Missing the required parameter `story_gid` when calling `update_story`")  # noqa: E501

    collection_formats = {}

    path_params = {}
    if 'story_gid' in params:
        path_params['story_gid'] = params['story_gid']  # noqa: E501

    query_params = []
    if 'opt_fields' in params:
        query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
        collection_formats['opt_fields'] = 'csv'  # noqa: E501

    header_params = kwargs.get("header_params", {})

    form_params = []
    local_var_files = {}

    body_params = None
    if 'body' in params:
        body_params = params['body']
    # HTTP header `Accept`
    header_params['Accept'] = self.api_client.select_header_accept(
        ['application/json; charset=UTF-8'])  # noqa: E501

    # HTTP header `Content-Type`
    header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
        ['application/json; charset=UTF-8'])  # noqa: E501

    # Authentication setting
    auth_settings = ['oauth2']  # noqa: E501

    return self.api_client.call_api(
        '/stories/{story_gid}', 'PUT',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='StoryResponseData',  # noqa: E501
        auth_settings=auth_settings,
        async_req=params.get('async_req'),
        _return_http_data_only=params.get('_return_http_data_only'),
        _preload_content=params.get('_preload_content', True),
        _request_timeout=params.get('_request_timeout'),
        collection_formats=collection_formats)