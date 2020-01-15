
class _Users:

    def __init__(self, client=None):
        self.client = client

    def get_favorites_for_user(self, user_gid, params={}, **options):
        """Get a user's favorites
        :param str user_gid: Globally unique identifier for the user. (required)
        [params] : {Object} Parameters for the request
        :return: list[AsanaNamedResource]
        """
        path = "/users/{user_gid}/favorites".replace("user_gid", user_gid)
        return self.client.get(path, params, **options)


    def get_user(self, user_gid, params={}, **options):
        """Get a user
        :param str user_gid: Globally unique identifier for the user. (required)
        [params] : {Object} Parameters for the request
        :return: UserResponse
        """
        path = "/users/{user_gid}".replace("user_gid", user_gid)
        return self.client.get(path, params, **options)


    def get_users(self, params={}, **options):
        """Get multiple users
        [params] : {Object} Parameters for the request
        :return: list[UserCompact]
        """
        path = "/users"
        return self.client.get(path, params, **options)


    def get_users_for_team(self, team_gid, params={}, **options):
        """Get users in a team
        :param str team_gid: Globally unique identifier for the team. (required)
        [params] : {Object} Parameters for the request
        :return: list[UserCompact]
        """
        path = "/teams/{team_gid}/users".replace("team_gid", team_gid)
        return self.client.get(path, params, **options)


    def get_users_for_workspace(self, workspace_gid, params={}, **options):
        """Get users in a workspace or organization
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        [params] : {Object} Parameters for the request
        :return: list[UserCompact]
        """
        path = "/workspaces/{workspace_gid}/users".replace("workspace_gid", workspace_gid)
        return self.client.get(path, params, **options)

