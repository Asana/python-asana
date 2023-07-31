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


class StatusUpdatesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_status_for_object(self, body, **kwargs):  # noqa: E501
        """Create a status update  # noqa: E501

        Creates a new status update on an object. Returns the full record of the newly created status update.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_status_for_object(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StatusUpdatesBody body: The status update to create. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: StatusUpdateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_status_for_object_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_status_for_object_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_status_for_object_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a status update  # noqa: E501

        Creates a new status update on an object. Returns the full record of the newly created status update.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_status_for_object_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StatusUpdatesBody body: The status update to create. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: StatusUpdateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'limit', 'offset', 'opt_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_status_for_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_status_for_object`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'opt_fields' in params:
            query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
            collection_formats['opt_fields'] = 'csv'  # noqa: E501

        header_params = {}

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
            '/status_updates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusUpdateResponseData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_status(self, status_update_gid, **kwargs):  # noqa: E501
        """Delete a status update  # noqa: E501

        Deletes a specific, existing status update.  Returns an empty data record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_status(status_update_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status_update_gid: The status update to get. (required)
        :return: EmptyResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_status_with_http_info(status_update_gid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_status_with_http_info(status_update_gid, **kwargs)  # noqa: E501
            return data

    def delete_status_with_http_info(self, status_update_gid, **kwargs):  # noqa: E501
        """Delete a status update  # noqa: E501

        Deletes a specific, existing status update.  Returns an empty data record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_status_with_http_info(status_update_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status_update_gid: The status update to get. (required)
        :return: EmptyResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status_update_gid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status_update_gid' is set
        if ('status_update_gid' not in params or
                params['status_update_gid'] is None):
            raise ValueError("Missing the required parameter `status_update_gid` when calling `delete_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'status_update_gid' in params:
            path_params['status_update_gid'] = params['status_update_gid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/status_updates/{status_update_gid}', 'DELETE',
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

    def get_status(self, status_update_gid, **kwargs):  # noqa: E501
        """Get a status update  # noqa: E501

        Returns the complete record for a single status update.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status(status_update_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status_update_gid: The status update to get. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: StatusUpdateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_status_with_http_info(status_update_gid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_status_with_http_info(status_update_gid, **kwargs)  # noqa: E501
            return data

    def get_status_with_http_info(self, status_update_gid, **kwargs):  # noqa: E501
        """Get a status update  # noqa: E501

        Returns the complete record for a single status update.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_status_with_http_info(status_update_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str status_update_gid: The status update to get. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: StatusUpdateResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['status_update_gid', 'opt_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'status_update_gid' is set
        if ('status_update_gid' not in params or
                params['status_update_gid'] is None):
            raise ValueError("Missing the required parameter `status_update_gid` when calling `get_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'status_update_gid' in params:
            path_params['status_update_gid'] = params['status_update_gid']  # noqa: E501

        query_params = []
        if 'opt_fields' in params:
            query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
            collection_formats['opt_fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/status_updates/{status_update_gid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusUpdateResponseData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_statuses_for_object(self, parent, **kwargs):  # noqa: E501
        """Get status updates from an object  # noqa: E501

        Returns the compact status update records for all updates on the object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statuses_for_object(parent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str parent: Globally unique identifier for object to fetch statuses from. Must be a GID for a project, portfolio, or goal. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param datetime created_since: Only return statuses that have been created since the given time.
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: StatusUpdateResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_statuses_for_object_with_http_info(parent, **kwargs)  # noqa: E501
        else:
            (data) = self.get_statuses_for_object_with_http_info(parent, **kwargs)  # noqa: E501
            return data

    def get_statuses_for_object_with_http_info(self, parent, **kwargs):  # noqa: E501
        """Get status updates from an object  # noqa: E501

        Returns the compact status update records for all updates on the object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_statuses_for_object_with_http_info(parent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str parent: Globally unique identifier for object to fetch statuses from. Must be a GID for a project, portfolio, or goal. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param datetime created_since: Only return statuses that have been created since the given time.
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: StatusUpdateResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['parent', 'limit', 'offset', 'created_since', 'opt_fields']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_statuses_for_object" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'parent' is set
        if ('parent' not in params or
                params['parent'] is None):
            raise ValueError("Missing the required parameter `parent` when calling `get_statuses_for_object`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'parent' in params:
            query_params.append(('parent', params['parent']))  # noqa: E501
        if 'created_since' in params:
            query_params.append(('created_since', params['created_since']))  # noqa: E501
        if 'opt_fields' in params:
            query_params.append(('opt_fields', params['opt_fields']))  # noqa: E501
            collection_formats['opt_fields'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/status_updates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StatusUpdateResponseArray',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
