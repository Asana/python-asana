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


class BatchAPIApi(object):
"""NOTE: This class is auto generated by the swagger code generator program.

Do not edit the class manually.
Ref: https://github.com/swagger-api/swagger-codegen
"""

def __init__(self, api_client=None):
    if api_client is None:
        api_client = ApiClient()
    self.api_client = api_client

def create_batch_request(self, body, **kwargs):  # noqa: E501
    """Submit parallel requests  # noqa: E501

    Make multiple requests in parallel to Asana's API.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.create_batch_request(body, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param BatchBody body: The requests to batch together via the Batch API. (required)
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: BatchResponseArray
                If the method is called asynchronously,
                returns the request thread.
    """
    kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
    if kwargs.get('async_req'):
        return self.create_batch_request_with_http_info(body, **kwargs)  # noqa: E501
    else:
        (data) = self.create_batch_request_with_http_info(body, **kwargs)  # noqa: E501
        return data

def create_batch_request_with_http_info(self, body, **kwargs):  # noqa: E501
    """Submit parallel requests  # noqa: E501

    Make multiple requests in parallel to Asana's API.  # noqa: E501
    This method makes a synchronous HTTP request by default. To make an
    asynchronous HTTP request, please pass async_req=True
    >>> thread = api.create_batch_request_with_http_info(body, async_req=True)
    >>> result = thread.get()

    :param async_req bool
    :param BatchBody body: The requests to batch together via the Batch API. (required)
    :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
    :return: BatchResponseArray
                If the method is called asynchronously,
                returns the request thread.
    """

    all_params = ['body', 'opt_fields']  # noqa: E501
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
                " to method create_batch_request" % key
            )
        params[key] = val
    del params['kwargs']
    # verify the required parameter 'body' is set
    if ('body' not in params or
            params['body'] is None):
        raise ValueError("Missing the required parameter `body` when calling `create_batch_request`")  # noqa: E501

    collection_formats = {}

    path_params = {}

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
        '/batch', 'POST',
        path_params,
        query_params,
        header_params,
        body=body_params,
        post_params=form_params,
        files=local_var_files,
        response_type='BatchResponseArray',  # noqa: E501
        auth_settings=auth_settings,
        async_req=params.get('async_req'),
        _return_http_data_only=params.get('_return_http_data_only'),
        _preload_content=params.get('_preload_content', True),
        _request_timeout=params.get('_request_timeout'),
        collection_formats=collection_formats)