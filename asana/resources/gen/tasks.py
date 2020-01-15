
class _Tasks:

    def __init__(self, client=None):
        self.client = client

    def add_dependencies_for_task(self, task_gid, params={}, **options):
        """Set dependencies for a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: list[TaskCompact]
        """
        path = "/tasks/{task_gid}/addDependencies".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def add_dependents_for_task(self, task_gid, params={}, **options):
        """Set dependents for a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: list[TaskCompact]
        """
        path = "/tasks/{task_gid}/addDependents".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def add_followers_for_task(self, task_gid, params={}, **options):
        """Add followers to a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/tasks/{task_gid}/addFollowers".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def add_project_for_task(self, task_gid, params={}, **options):
        """Add a project to a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/tasks/{task_gid}/addProject".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def add_tag_for_task(self, task_gid, params={}, **options):
        """Add a tag to a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/tasks/{task_gid}/addTag".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def create_subtask_for_task(self, task_gid, params={}, **options):
        """Create a subtask
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: TaskResponse
        """
        path = "/tasks/{task_gid}/subtasks".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def create_task(self, params={}, **options):
        """Create a task
        [params] : {Object} Parameters for the request
        :return: TaskResponse
        """
        path = "/tasks"
        return self.client.get(path, params, **options)


    def delete_task(self, task_gid, params={}, **options):
        """Delete a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/tasks/{task_gid}".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def duplicate_task(self, task_gid, params={}, **options):
        """Duplicate a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: JobResponse
        """
        path = "/tasks/{task_gid}/duplicate".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def get_dependencies_for_task(self, task_gid, params={}, **options):
        """Get dependencies from a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: list[TaskCompact]
        """
        path = "/tasks/{task_gid}/dependencies".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def get_dependents_for_task(self, task_gid, params={}, **options):
        """Get dependents from a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: list[TaskCompact]
        """
        path = "/tasks/{task_gid}/dependents".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def get_subtasks_for_task(self, task_gid, params={}, **options):
        """Get subtasks from a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: list[TaskCompact]
        """
        path = "/tasks/{task_gid}/subtasks".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def get_task(self, task_gid, params={}, **options):
        """Get a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: TaskResponse
        """
        path = "/tasks/{task_gid}".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def get_tasks(self, params={}, **options):
        """Get multiple tasks
        [params] : {Object} Parameters for the request
        :return: list[TaskCompact]
        """
        path = "/tasks"
        return self.client.get(path, params, **options)


    def get_tasks_for_project(self, project_gid, params={}, **options):
        """Get tasks from a project
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: list[TaskCompact]
        """
        path = "/projects/{project_gid}/tasks".replace("{project_gid}", project_gid)
        return self.client.get(path, params, **options)


    def get_tasks_for_section(self, section_gid, params={}, **options):
        """Get tasks from a section
        :param str section_gid: The globally unique identifier for the section. (required)
        [params] : {Object} Parameters for the request
        :return: list[TaskCompact]
        """
        path = "/sections/{section_gid}/tasks".replace("{section_gid}", section_gid)
        return self.client.get(path, params, **options)


    def get_tasks_for_tag(self, tag_gid, params={}, **options):
        """Get tasks from a tag
        :param str tag_gid: Globally unique identifier for the tag. (required)
        [params] : {Object} Parameters for the request
        :return: list[TaskCompact]
        """
        path = "/tags/{tag_gid}/tasks".replace("{tag_gid}", tag_gid)
        return self.client.get(path, params, **options)


    def remove_dependencies_for_task(self, task_gid, params={}, **options):
        """Unlink dependencies from a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: list[TaskCompact]
        """
        path = "/tasks/{task_gid}/removeDependencies".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def remove_dependents_for_task(self, task_gid, params={}, **options):
        """Unlink dependents from a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: list[TaskCompact]
        """
        path = "/tasks/{task_gid}/removeDependents".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def remove_follower_for_task(self, task_gid, params={}, **options):
        """Remove followers from a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/tasks/{task_gid}/removeFollowers".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def remove_project_for_task(self, task_gid, params={}, **options):
        """Remove a project from a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/tasks/{task_gid}/removeProject".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def remove_tag_for_task(self, task_gid, params={}, **options):
        """Remove a tag from a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/tasks/{task_gid}/removeTag".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def search_tasks_for_workspace(self, workspace_gid, params={}, **options):
        """Search tasks in a workspace
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        [params] : {Object} Parameters for the request
        :return: list[TaskCompact]
        """
        path = "/workspaces/{workspace_gid}/tasks/search".replace("{workspace_gid}", workspace_gid)
        return self.client.get(path, params, **options)


    def set_parent_for_task(self, task_gid, params={}, **options):
        """Set the parent of a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: TaskResponse
        """
        path = "/tasks/{task_gid}/setParent".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def update_task(self, task_gid, params={}, **options):
        """Update a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: TaskResponse
        """
        path = "/tasks/{task_gid}".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)

