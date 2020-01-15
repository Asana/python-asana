
class _Projects:

    def __init__(self, client=None):
        self.client = client

    def add_custom_field_setting_for_project(self, project_gid, params={}, **options):
        """Add a custom field to a project
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/projects/{project_gid}/addCustomFieldSetting".replace("project_gid", project_gid)
        return self.client.get(path, params, **options)


    def create_project(self, params={}, **options):
        """Create a project
        [params] : {Object} Parameters for the request
        :return: ProjectResponse
        """
        path = "/projects"
        return self.client.get(path, params, **options)


    def create_project_for_team(self, team_gid, params={}, **options):
        """Create a project in a team
        :param str team_gid: Globally unique identifier for the team. (required)
        [params] : {Object} Parameters for the request
        :return: ProjectResponse
        """
        path = "/teams/{team_gid}/projects".replace("team_gid", team_gid)
        return self.client.get(path, params, **options)


    def create_project_for_workspace(self, workspace_gid, params={}, **options):
        """Create a project in a workspace
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        [params] : {Object} Parameters for the request
        :return: ProjectResponse
        """
        path = "/workspaces/{workspace_gid}/projects".replace("workspace_gid", workspace_gid)
        return self.client.get(path, params, **options)


    def delete_project(self, project_gid, params={}, **options):
        """Delete a project
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/projects/{project_gid}".replace("project_gid", project_gid)
        return self.client.get(path, params, **options)


    def duplicate_project(self, project_gid, params={}, **options):
        """Duplicate a project
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: JobResponse
        """
        path = "/projects/{project_gid}/duplicate".replace("project_gid", project_gid)
        return self.client.get(path, params, **options)


    def get_project(self, project_gid, params={}, **options):
        """Get a project
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: ProjectResponse
        """
        path = "/projects/{project_gid}".replace("project_gid", project_gid)
        return self.client.get(path, params, **options)


    def get_projects(self, params={}, **options):
        """Get multiple projects
        [params] : {Object} Parameters for the request
        :return: list[ProjectCompact]
        """
        path = "/projects"
        return self.client.get(path, params, **options)


    def get_projects_for_task(self, task_gid, params={}, **options):
        """Get projects a task is in
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: list[ProjectCompact]
        """
        path = "/tasks/{task_gid}/projects".replace("task_gid", task_gid)
        return self.client.get(path, params, **options)


    def get_projects_for_team(self, team_gid, params={}, **options):
        """Get a team's projects
        :param str team_gid: Globally unique identifier for the team. (required)
        [params] : {Object} Parameters for the request
        :return: list[ProjectCompact]
        """
        path = "/teams/{team_gid}/projects".replace("team_gid", team_gid)
        return self.client.get(path, params, **options)


    def get_projects_for_workspace(self, workspace_gid, params={}, **options):
        """Get all projects in a workspace
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        [params] : {Object} Parameters for the request
        :return: list[ProjectCompact]
        """
        path = "/workspaces/{workspace_gid}/projects".replace("workspace_gid", workspace_gid)
        return self.client.get(path, params, **options)


    def get_task_counts_for_project(self, project_gid, params={}, **options):
        """Get task count of a project
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: TaskCountResponse
        """
        path = "/projects/{project_gid}/task_counts".replace("project_gid", project_gid)
        return self.client.get(path, params, **options)


    def remove_custom_field_setting_for_project(self, project_gid, params={}, **options):
        """Remove a custom field from a project
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/projects/{project_gid}/removeCustomFieldSetting".replace("project_gid", project_gid)
        return self.client.get(path, params, **options)


    def update_project(self, project_gid, params={}, **options):
        """Update a project
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: ProjectResponse
        """
        path = "/projects/{project_gid}".replace("project_gid", project_gid)
        return self.client.get(path, params, **options)

