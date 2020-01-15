
class _WorkspaceMemberships:

    def __init__(self, client=None):
        self.client = client

    def get_workspace_membership(self, workspace_membership_path_gid, params={}, **options):
        """Get a workspace membership
        :param str workspace_membership_path_gid: (required)
        [params] : {Object} Parameters for the request
        :return: WorkspaceMembershipResponse
        """
        path = "/workspace_memberships/{workspace_membership_gid}".replace("{workspace_membership_path_gid}", workspace_membership_path_gid)
        return self.client.get(path, params, **options)


    def get_workspace_memberships_for_user(self, user_gid, params={}, **options):
        """Get workspace memberships for a user
        :param str user_gid: Globally unique identifier for the user. (required)
        [params] : {Object} Parameters for the request
        :return: list[WorkspaceMembershipCompact]
        """
        path = "/users/{user_gid}/workspace_memberships".replace("{user_gid}", user_gid)
        return self.client.get(path, params, **options)


    def get_workspace_memberships_for_workspace(self, workspace_gid, params={}, **options):
        """Get the workspace memberships for a workspace
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        [params] : {Object} Parameters for the request
        :return: list[WorkspaceMembershipCompact]
        """
        path = "/workspaces/{workspace_gid}/workspace_memberships".replace("{workspace_gid}", workspace_gid)
        return self.client.get(path, params, **options)

