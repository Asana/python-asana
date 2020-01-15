
class _Workspaces:

    def __init__(self, client=None):
        self.client = client

    def add_user_for_workspace(self, workspace_gid, params={}, **options):
        """Add a user to a workspace or organization
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        [params] : {Object} Parameters for the request
        :return: UserResponse
        """
        path = "/workspaces/{workspace_gid}/addUser".replace("workspace_gid", workspace_gid)
        return self.client.get(path, params, **options)


    def get_workspace(self, workspace_gid, params={}, **options):
        """Get a workspace
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        [params] : {Object} Parameters for the request
        :return: WorkspaceResponse
        """
        path = "/workspaces/{workspace_gid}".replace("workspace_gid", workspace_gid)
        return self.client.get(path, params, **options)


    def get_workspaces(self, params={}, **options):
        """Get multiple workspaces
        [params] : {Object} Parameters for the request
        :return: list[WorkspaceCompact]
        """
        path = "/workspaces"
        return self.client.get(path, params, **options)


    def remove_user_for_workspace(self, workspace_gid, params={}, **options):
        """Remove a user from a workspace or organization
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/workspaces/{workspace_gid}/removeUser".replace("workspace_gid", workspace_gid)
        return self.client.get(path, params, **options)


    def update_workspace(self, workspace_gid, params={}, **options):
        """Update a workspace
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        [params] : {Object} Parameters for the request
        :return: WorkspaceResponse
        """
        path = "/workspaces/{workspace_gid}".replace("workspace_gid", workspace_gid)
        return self.client.get(path, params, **options)

