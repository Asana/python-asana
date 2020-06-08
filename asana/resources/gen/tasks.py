# coding=utf-8
class _Tasks:

    def __init__(self, client=None):
        self.client = client

    def add_dependencies_for_task(self, task_gid, params=None, **options):
        """Set dependencies for a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/addDependencies".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)

    def add_dependents_for_task(self, task_gid, params=None, **options):
        """Set dependents for a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/addDependents".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)

    def add_followers_for_task(self, task_gid, params=None, **options):
        """Add followers to a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/addFollowers".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)

    def add_project_for_task(self, task_gid, params=None, **options):
        """Add a project to a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/addProject".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)

    def add_tag_for_task(self, task_gid, params=None, **options):
        """Add a tag to a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/addTag".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)

    def create_subtask_for_task(self, task_gid, params=None, **options):
        """Create a subtask
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/subtasks".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)

    def create_task(self, params=None, **options):
        """Create a task
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks"
        return self.client.post(path, params, **options)

    def delete_task(self, task_gid, params=None, **options):
        """Delete a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}".replace("{task_gid}", task_gid)
        return self.client.delete(path, params, **options)

    def duplicate_task(self, task_gid, params=None, **options):
        """Duplicate a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/duplicate".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)

    def get_dependencies_for_task(self, task_gid, params=None, **options):
        """Get dependencies from a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/dependencies".replace("{task_gid}", task_gid)
        return self.client.get_collection(path, params, **options)

    def get_dependents_for_task(self, task_gid, params=None, **options):
        """Get dependents from a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/dependents".replace("{task_gid}", task_gid)
        return self.client.get_collection(path, params, **options)

    def get_subtasks_for_task(self, task_gid, params=None, **options):
        """Get subtasks from a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/subtasks".replace("{task_gid}", task_gid)
        return self.client.get_collection(path, params, **options)

    def get_task(self, task_gid, params=None, **options):
        """Get a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)

    def get_tasks(self, params=None, **options):
        """Get multiple tasks
        :param Object params: Parameters for the request
            - assignee {str}:  The assignee to filter tasks on. *Note: If you specify `assignee`, you must also specify the `workspace` to filter on.*
            - project {str}:  The project to filter tasks on.
            - section {str}:  The section to filter tasks on. *Note: Currently, this is only supported in board views.*
            - workspace {str}:  The workspace to filter tasks on. *Note: If you specify `workspace`, you must also specify the `assignee` to filter on.*
            - completed_since {datetime}:  Only return tasks that are either incomplete or that have been completed since this time.
            - modified_since {datetime}:  Only return tasks that have been modified since the given time.  *Note: A task is considered “modified” if any of its properties change, or associations between it and other objects are modified (e.g.  a task being added to a project). A task is not considered modified just because another object it is associated with (e.g. a subtask) is modified. Actions that count as modifying the task include assigning, renaming, completing, and adding stories.*
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks"
        return self.client.get_collection(path, params, **options)

    def get_tasks_for_project(self, project_gid, params=None, **options):
        """Get tasks from a project
        :param str project_gid: (required) Globally unique identifier for the project.
        :param Object params: Parameters for the request
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/projects/{project_gid}/tasks".replace("{project_gid}", project_gid)
        return self.client.get_collection(path, params, **options)

    def get_tasks_for_section(self, section_gid, params=None, **options):
        """Get tasks from a section
        :param str section_gid: (required) The globally unique identifier for the section.
        :param Object params: Parameters for the request
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/sections/{section_gid}/tasks".replace("{section_gid}", section_gid)
        return self.client.get_collection(path, params, **options)

    def get_tasks_for_tag(self, tag_gid, params=None, **options):
        """Get tasks from a tag
        :param str tag_gid: (required) Globally unique identifier for the tag.
        :param Object params: Parameters for the request
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tags/{tag_gid}/tasks".replace("{tag_gid}", tag_gid)
        return self.client.get_collection(path, params, **options)

    def get_tasks_for_user_task_list(self, user_task_list_gid, params=None, **options):
        """Get tasks from a user task list
        :param str user_task_list_gid: (required) Globally unique identifier for the user task list.
        :param Object params: Parameters for the request
            - completed_since {str}:  Only return tasks that are either incomplete or that have been completed since this time. Accepts a date-time string or the keyword *now*. 
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/user_task_lists/{user_task_list_gid}/tasks".replace("{user_task_list_gid}", user_task_list_gid)
        return self.client.get_collection(path, params, **options)

    def remove_dependencies_for_task(self, task_gid, params=None, **options):
        """Unlink dependencies from a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/removeDependencies".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)

    def remove_dependents_for_task(self, task_gid, params=None, **options):
        """Unlink dependents from a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/removeDependents".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)

    def remove_follower_for_task(self, task_gid, params=None, **options):
        """Remove followers from a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/removeFollowers".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)

    def remove_project_for_task(self, task_gid, params=None, **options):
        """Remove a project from a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/removeProject".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)

    def remove_tag_for_task(self, task_gid, params=None, **options):
        """Remove a tag from a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/removeTag".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)

    def search_tasks_for_workspace(self, workspace_gid, params=None, **options):
        """Search tasks in a workspace
        :param str workspace_gid: (required) Globally unique identifier for the workspace or organization.
        :param Object params: Parameters for the request
            - text {str}:  Performs full-text search on both task name and description
            - resource_subtype {str}:  Filters results by the task's resource_subtype
            - assignee_any {str}:  Comma-separated list of user identifiers
            - assignee_not {str}:  Comma-separated list of user identifiers
            - assignee_status {str}:  One of `inbox`, `today`, `upcoming`, or `later`
            - portfolios_any {str}:  Comma-separated list of portfolio IDs
            - projects_any {str}:  Comma-separated list of project IDs
            - projects_not {str}:  Comma-separated list of project IDs
            - projects_all {str}:  Comma-separated list of project IDs
            - sections_any {str}:  Comma-separated list of section or column IDs
            - sections_not {str}:  Comma-separated list of section or column IDs
            - sections_all {str}:  Comma-separated list of section or column IDs
            - tags_any {str}:  Comma-separated list of tag IDs
            - tags_not {str}:  Comma-separated list of tag IDs
            - tags_all {str}:  Comma-separated list of tag IDs
            - teams_any {str}:  Comma-separated list of team IDs
            - followers_any {str}:  Comma-separated list of user identifiers
            - followers_not {str}:  Comma-separated list of user identifiers
            - created_by_any {str}:  Comma-separated list of user identifiers
            - created_by_not {str}:  Comma-separated list of user identifiers
            - assigned_by_any {str}:  Comma-separated list of user identifiers
            - assigned_by_not {str}:  Comma-separated list of user identifiers
            - liked_by_any {str}:  Comma-separated list of user identifiers
            - liked_by_not {str}:  Comma-separated list of user identifiers
            - commented_on_by_any {str}:  Comma-separated list of user identifiers
            - commented_on_by_not {str}:  Comma-separated list of user identifiers
            - due_on_before {date}:  ISO 8601 date string
            - due_on_after {date}:  ISO 8601 date string
            - due_on {date}:  ISO 8601 date string or `null`
            - due_at_before {datetime}:  ISO 8601 datetime string
            - due_at_after {datetime}:  ISO 8601 datetime string
            - start_on_before {date}:  ISO 8601 date string
            - start_on_after {date}:  ISO 8601 date string
            - start_on {date}:  ISO 8601 date string or `null`
            - created_on_before {date}:  ISO 8601 date string
            - created_on_after {date}:  ISO 8601 date string
            - created_on {date}:  ISO 8601 date string or `null`
            - created_at_before {datetime}:  ISO 8601 datetime string
            - created_at_after {datetime}:  ISO 8601 datetime string
            - completed_on_before {date}:  ISO 8601 date string
            - completed_on_after {date}:  ISO 8601 date string
            - completed_on {date}:  ISO 8601 date string or `null`
            - completed_at_before {datetime}:  ISO 8601 datetime string
            - completed_at_after {datetime}:  ISO 8601 datetime string
            - modified_on_before {date}:  ISO 8601 date string
            - modified_on_after {date}:  ISO 8601 date string
            - modified_on {date}:  ISO 8601 date string or `null`
            - modified_at_before {datetime}:  ISO 8601 datetime string
            - modified_at_after {datetime}:  ISO 8601 datetime string
            - is_blocking {bool}:  Filter to incomplete tasks with dependents
            - is_blocked {bool}:  Filter to tasks with incomplete dependencies
            - has_attachment {bool}:  Filter to tasks with attachments
            - completed {bool}:  Filter to completed tasks
            - is_subtask {bool}:  Filter to subtasks
            - sort_by {str}:  One of `due_date`, `created_at`, `completed_at`, `likes`, or `modified_at`, defaults to `modified_at`
            - sort_ascending {bool}:  Default `false`
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/workspaces/{workspace_gid}/tasks/search".replace("{workspace_gid}", workspace_gid)
        return self.client.get_collection(path, params, **options)

    def set_parent_for_task(self, task_gid, params=None, **options):
        """Set the parent of a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/setParent".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)

    def update_task(self, task_gid, params=None, **options):
        """Update a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}".replace("{task_gid}", task_gid)
        return self.client.put(path, params, **options)
