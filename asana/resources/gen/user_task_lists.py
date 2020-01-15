
class _UserTaskLists:

    def __init__(self, client=None):
        self.client = client

    def get_tasks_for_user_task_list(self, user_task_list_gid, params={}, **options):
        """Get tasks from a user task list
        :param str user_task_list_gid: Globally unique identifier for the user task list. (required)
        [params] : {Object} Parameters for the request
        :return: list[TaskCompact]
        """
        path = "/user_task_lists/{user_task_list_gid}/tasks".replace("user_task_list_gid", user_task_list_gid)
        return self.client.get(path, params, **options)


    def get_user_task_list(self, user_task_list_gid, params={}, **options):
        """Get a user task list
        :param str user_task_list_gid: Globally unique identifier for the user task list. (required)
        [params] : {Object} Parameters for the request
        :return: UserTaskListResponse
        """
        path = "/user_task_list/{user_task_list_gid}".replace("user_task_list_gid", user_task_list_gid)
        return self.client.get(path, params, **options)


    def get_user_task_list_for_user(self, user_gid, params={}, **options):
        """Get a user's task list
        :param str user_gid: Globally unique identifier for the user. (required)
        [params] : {Object} Parameters for the request
        :return: UserTaskListResponse
        """
        path = "/users/{user_gid}/user_task_list".replace("user_gid", user_gid)
        return self.client.get(path, params, **options)

