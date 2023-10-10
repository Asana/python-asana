# coding=utf-8
class _UserTaskLists:

    def __init__(self, client=None):
        self.client = client

    def get_user_task_list(self, user_task_list_gid, params=None, **options):
        """Get a user task list
        :param str user_task_list_gid: (required) Globally unique identifier for the user task list.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/user_task_lists/{user_task_list_gid}".replace("{user_task_list_gid}", user_task_list_gid)
        return self.client.get(path, params, **options)

    def get_user_task_list_for_user(self, user_gid, params=None, **options):
        """Get a user's task list
        :param str user_gid: (required) A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
        :param Object params: Parameters for the request
            - workspace {str}:  (required) The workspace in which to get the user task list.
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/users/{user_gid}/user_task_list".replace("{user_gid}", user_gid)
        return self.client.get(path, params, **options)
