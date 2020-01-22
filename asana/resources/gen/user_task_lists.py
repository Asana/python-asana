# coding=utf-8
class _UserTaskLists:

    def __init__(self, client=None):
        self.client = client

    def get_tasks_for_user_task_list(self, user_task_list_gid, params={}, **options):
        """Get tasks from a user task list
        :param str user_task_list_gid: (required) Globally unique identifier for the user task list.
        :param Object params: Parameters for the request
            - completed_since {str}:  Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*. 
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        path = "/user_task_lists/{user_task_list_gid}/tasks".replace("{user_task_list_gid}", user_task_list_gid)
        return self.client.get_collection(path, params, **options)


    def get_user_task_list(self, user_task_list_gid, params={}, **options):
        """Get a user task list
        :param str user_task_list_gid: (required) Globally unique identifier for the user task list.
        :param Object params: Parameters for the request
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        path = "/user_task_lists/{user_task_list_gid}".replace("{user_task_list_gid}", user_task_list_gid)
        return self.client.get(path, params, **options)


    def get_user_task_list_for_user(self, user_gid, params={}, **options):
        """Get a user's task list
        :param str user_gid: (required) Globally unique identifier for the user.
        :param Object params: Parameters for the request
            - workspace {str}:  (required) The workspace in which to get the user task list.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        path = "/users/{user_gid}/user_task_list".replace("{user_gid}", user_gid)
        return self.client.get(path, params, **options)

