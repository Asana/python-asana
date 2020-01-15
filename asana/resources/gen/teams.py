
class _Teams:

    def __init__(self, client=None):
        self.client = client

    def add_user_for_team(self, team_gid, params={}, **options):
        """Add a user to a team
        :param str team_gid: Globally unique identifier for the team. (required)
        [params] : {Object} Parameters for the request
        :return: UserResponse
        """
        path = "/teams/{team_gid}/addUser".replace("{team_gid}", team_gid)
        return self.client.get(path, params, **options)


    def get_team(self, team_gid, params={}, **options):
        """Get a team
        :param str team_gid: Globally unique identifier for the team. (required)
        [params] : {Object} Parameters for the request
        :return: TeamResponse
        """
        path = "/teams/{team_gid}".replace("{team_gid}", team_gid)
        return self.client.get(path, params, **options)


    def get_teams_for_organization(self, workspace_gid, params={}, **options):
        """Get teams in an organization
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        [params] : {Object} Parameters for the request
        :return: list[TeamCompact]
        """
        path = "/organizations/{workspace_gid}/teams".replace("{workspace_gid}", workspace_gid)
        return self.client.get(path, params, **options)


    def get_teams_for_user(self, user_gid, params={}, **options):
        """Get teams for a user
        :param str user_gid: Globally unique identifier for the user. (required)
        [params] : {Object} Parameters for the request
        :return: list[TeamCompact]
        """
        path = "/users/{user_gid}/teams".replace("{user_gid}", user_gid)
        return self.client.get(path, params, **options)


    def remove_user_for_team(self, team_gid, params={}, **options):
        """Remove a user from a team
        :param str team_gid: Globally unique identifier for the team. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/teams/{team_gid}/removeUser".replace("{team_gid}", team_gid)
        return self.client.get(path, params, **options)

