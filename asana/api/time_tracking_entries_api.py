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
from asana.pagination.event_iterator import EventIterator
from asana.pagination.page_iterator import PageIterator

class TimeTrackingEntriesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_time_tracking_entry(self, body, task_gid, opts, **kwargs):  # noqa: E501
        """Create a time tracking entry  # noqa: E501

        Creates a time tracking entry on a given task.  Returns the record of the newly created time tracking entry.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_time_tracking_entry(body, task_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict body: Information about the time tracking entry. (required)
        :param str task_gid: The task to operate on. (required)
        :param list[str] opt_fields: This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TimeTrackingEntryBaseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.create_time_tracking_entry_with_http_info(body, task_gid, opts, **kwargs)  # noqa: E501
        else:
            (data) = self.create_time_tracking_entry_with_http_info(body, task_gid, opts, **kwargs)  # noqa: E501
            return data

    def create_time_tracking_entry_with_http_info(self, body, task_gid, opts, **kwargs):  # noqa: E501
        """Create a time tracking entry  # noqa: E501

        Creates a time tracking entry on a given task.  Returns the record of the newly created time tracking entry.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_time_tracking_entry_with_http_info(body, task_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict body: Information about the time tracking entry. (required)
        :param str task_gid: The task to operate on. (required)
        :param list[str] opt_fields: This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TimeTrackingEntryBaseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = []
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('full_payload')
        all_params.append('item_limit')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_time_tracking_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if (body is None):
            raise ValueError("Missing the required parameter `body` when calling `create_time_tracking_entry`")  # noqa: E501
        # verify the required parameter 'task_gid' is set
        if (task_gid is None):
            raise ValueError("Missing the required parameter `task_gid` when calling `create_time_tracking_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['task_gid'] = task_gid  # noqa: E501

        query_params = {}
        query_params = opts


        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = body

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['personalAccessToken']  # noqa: E501

        # hard checking for True boolean value because user can provide full_payload or async_req with any data type
        if kwargs.get("full_payload", False) is True or kwargs.get('async_req', False) is True:
            return self.api_client.call_api(
                '/tasks/{task_gid}/time_tracking_entries', 'POST',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
        elif self.api_client.configuration.return_page_iterator:
            (data) = self.api_client.call_api(
                '/tasks/{task_gid}/time_tracking_entries', 'POST',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
            if params.get('_return_http_data_only') == False:
                return data
            return data["data"] if data else data
        else:
            return self.api_client.call_api(
            '/tasks/{task_gid}/time_tracking_entries', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=object,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_time_tracking_entry(self, time_tracking_entry_gid, **kwargs):  # noqa: E501
        """Delete a time tracking entry  # noqa: E501

        A specific, existing time tracking entry can be deleted by making a `DELETE` request on the URL for that time tracking entry.  Returns an empty data record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_time_tracking_entry(time_tracking_entry_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str time_tracking_entry_gid: Globally unique identifier for the time tracking entry. (required)
        :return: EmptyResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.delete_time_tracking_entry_with_http_info(time_tracking_entry_gid, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_time_tracking_entry_with_http_info(time_tracking_entry_gid, **kwargs)  # noqa: E501
            return data

    def delete_time_tracking_entry_with_http_info(self, time_tracking_entry_gid, **kwargs):  # noqa: E501
        """Delete a time tracking entry  # noqa: E501

        A specific, existing time tracking entry can be deleted by making a `DELETE` request on the URL for that time tracking entry.  Returns an empty data record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_time_tracking_entry_with_http_info(time_tracking_entry_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str time_tracking_entry_gid: Globally unique identifier for the time tracking entry. (required)
        :return: EmptyResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = []
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('full_payload')
        all_params.append('item_limit')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_time_tracking_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'time_tracking_entry_gid' is set
        if (time_tracking_entry_gid is None):
            raise ValueError("Missing the required parameter `time_tracking_entry_gid` when calling `delete_time_tracking_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['time_tracking_entry_gid'] = time_tracking_entry_gid  # noqa: E501

        query_params = {}


        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['personalAccessToken']  # noqa: E501

        # hard checking for True boolean value because user can provide full_payload or async_req with any data type
        if kwargs.get("full_payload", False) is True or kwargs.get('async_req', False) is True:
            return self.api_client.call_api(
                '/time_tracking_entries/{time_tracking_entry_gid}', 'DELETE',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
        elif self.api_client.configuration.return_page_iterator:
            (data) = self.api_client.call_api(
                '/time_tracking_entries/{time_tracking_entry_gid}', 'DELETE',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
            if params.get('_return_http_data_only') == False:
                return data
            return data["data"] if data else data
        else:
            return self.api_client.call_api(
            '/time_tracking_entries/{time_tracking_entry_gid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=object,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_time_tracking_entries_for_task(self, task_gid, opts, **kwargs):  # noqa: E501
        """Get time tracking entries for a task  # noqa: E501

        Returns time tracking entries for a given task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_time_tracking_entries_for_task(task_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_gid: The task to operate on. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
        :param list[str] opt_fields: This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TimeTrackingEntryCompactArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.get_time_tracking_entries_for_task_with_http_info(task_gid, opts, **kwargs)  # noqa: E501
        else:
            (data) = self.get_time_tracking_entries_for_task_with_http_info(task_gid, opts, **kwargs)  # noqa: E501
            return data

    def get_time_tracking_entries_for_task_with_http_info(self, task_gid, opts, **kwargs):  # noqa: E501
        """Get time tracking entries for a task  # noqa: E501

        Returns time tracking entries for a given task.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_time_tracking_entries_for_task_with_http_info(task_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str task_gid: The task to operate on. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
        :param list[str] opt_fields: This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TimeTrackingEntryCompactArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = []
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('full_payload')
        all_params.append('item_limit')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_time_tracking_entries_for_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_gid' is set
        if (task_gid is None):
            raise ValueError("Missing the required parameter `task_gid` when calling `get_time_tracking_entries_for_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['task_gid'] = task_gid  # noqa: E501

        query_params = {}
        query_params = opts


        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['personalAccessToken']  # noqa: E501

        # hard checking for True boolean value because user can provide full_payload or async_req with any data type
        if kwargs.get("full_payload", False) is True or kwargs.get('async_req', False) is True:
            return self.api_client.call_api(
                '/tasks/{task_gid}/time_tracking_entries', 'GET',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
        elif self.api_client.configuration.return_page_iterator:
            query_params["limit"] = query_params.get("limit", self.api_client.configuration.page_limit)
            return PageIterator(
                self.api_client,
                {
                    "resource_path": '/tasks/{task_gid}/time_tracking_entries',
                    "method": 'GET',
                    "path_params": path_params,
                    "query_params": query_params,
                    "header_params": header_params,
                    "body": body_params,
                    "post_params": form_params,
                    "files": local_var_files,
                    "response_type": object,
                    "auth_settings": auth_settings,
                    "async_req": params.get('async_req'),
                    "_return_http_data_only": params.get('_return_http_data_only'),
                    "_preload_content": params.get('_preload_content', True),
                    "_request_timeout": params.get('_request_timeout'),
                    "collection_formats": collection_formats
                },
                **kwargs
            ).items()
        else:
            return self.api_client.call_api(
            '/tasks/{task_gid}/time_tracking_entries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=object,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_time_tracking_entry(self, time_tracking_entry_gid, opts, **kwargs):  # noqa: E501
        """Get a time tracking entry  # noqa: E501

        Returns the complete time tracking entry record for a single time tracking entry.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_time_tracking_entry(time_tracking_entry_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str time_tracking_entry_gid: Globally unique identifier for the time tracking entry. (required)
        :param list[str] opt_fields: This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TimeTrackingEntryBaseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.get_time_tracking_entry_with_http_info(time_tracking_entry_gid, opts, **kwargs)  # noqa: E501
        else:
            (data) = self.get_time_tracking_entry_with_http_info(time_tracking_entry_gid, opts, **kwargs)  # noqa: E501
            return data

    def get_time_tracking_entry_with_http_info(self, time_tracking_entry_gid, opts, **kwargs):  # noqa: E501
        """Get a time tracking entry  # noqa: E501

        Returns the complete time tracking entry record for a single time tracking entry.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_time_tracking_entry_with_http_info(time_tracking_entry_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str time_tracking_entry_gid: Globally unique identifier for the time tracking entry. (required)
        :param list[str] opt_fields: This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TimeTrackingEntryBaseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = []
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('full_payload')
        all_params.append('item_limit')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_time_tracking_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'time_tracking_entry_gid' is set
        if (time_tracking_entry_gid is None):
            raise ValueError("Missing the required parameter `time_tracking_entry_gid` when calling `get_time_tracking_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['time_tracking_entry_gid'] = time_tracking_entry_gid  # noqa: E501

        query_params = {}
        query_params = opts


        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['personalAccessToken']  # noqa: E501

        # hard checking for True boolean value because user can provide full_payload or async_req with any data type
        if kwargs.get("full_payload", False) is True or kwargs.get('async_req', False) is True:
            return self.api_client.call_api(
                '/time_tracking_entries/{time_tracking_entry_gid}', 'GET',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
        elif self.api_client.configuration.return_page_iterator:
            (data) = self.api_client.call_api(
                '/time_tracking_entries/{time_tracking_entry_gid}', 'GET',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
            if params.get('_return_http_data_only') == False:
                return data
            return data["data"] if data else data
        else:
            return self.api_client.call_api(
            '/time_tracking_entries/{time_tracking_entry_gid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=object,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_time_tracking_entry(self, body, time_tracking_entry_gid, opts, **kwargs):  # noqa: E501
        """Update a time tracking entry  # noqa: E501

        A specific, existing time tracking entry can be updated by making a `PUT` request on the URL for that time tracking entry. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the task.  Returns the complete updated time tracking entry record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_time_tracking_entry(body, time_tracking_entry_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict body: The updated fields for the time tracking entry. (required)
        :param str time_tracking_entry_gid: Globally unique identifier for the time tracking entry. (required)
        :param list[str] opt_fields: This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TimeTrackingEntryBaseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.update_time_tracking_entry_with_http_info(body, time_tracking_entry_gid, opts, **kwargs)  # noqa: E501
        else:
            (data) = self.update_time_tracking_entry_with_http_info(body, time_tracking_entry_gid, opts, **kwargs)  # noqa: E501
            return data

    def update_time_tracking_entry_with_http_info(self, body, time_tracking_entry_gid, opts, **kwargs):  # noqa: E501
        """Update a time tracking entry  # noqa: E501

        A specific, existing time tracking entry can be updated by making a `PUT` request on the URL for that time tracking entry. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged.  When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the task.  Returns the complete updated time tracking entry record.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_time_tracking_entry_with_http_info(body, time_tracking_entry_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param dict body: The updated fields for the time tracking entry. (required)
        :param str time_tracking_entry_gid: Globally unique identifier for the time tracking entry. (required)
        :param list[str] opt_fields: This endpoint returns a resource which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TimeTrackingEntryBaseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = []
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('full_payload')
        all_params.append('item_limit')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_time_tracking_entry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if (body is None):
            raise ValueError("Missing the required parameter `body` when calling `update_time_tracking_entry`")  # noqa: E501
        # verify the required parameter 'time_tracking_entry_gid' is set
        if (time_tracking_entry_gid is None):
            raise ValueError("Missing the required parameter `time_tracking_entry_gid` when calling `update_time_tracking_entry`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['time_tracking_entry_gid'] = time_tracking_entry_gid  # noqa: E501

        query_params = {}
        query_params = opts


        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = body

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['personalAccessToken']  # noqa: E501

        # hard checking for True boolean value because user can provide full_payload or async_req with any data type
        if kwargs.get("full_payload", False) is True or kwargs.get('async_req', False) is True:
            return self.api_client.call_api(
                '/time_tracking_entries/{time_tracking_entry_gid}', 'PUT',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
        elif self.api_client.configuration.return_page_iterator:
            (data) = self.api_client.call_api(
                '/time_tracking_entries/{time_tracking_entry_gid}', 'PUT',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
            if params.get('_return_http_data_only') == False:
                return data
            return data["data"] if data else data
        else:
            return self.api_client.call_api(
            '/time_tracking_entries/{time_tracking_entry_gid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=object,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
