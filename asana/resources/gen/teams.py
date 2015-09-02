class _Teams:
    """A _team_ is used to group related projects and people together within an
    organization. Each project in an organization is associated with a team.
    """

    def __init__(self, client=None):
        self.client = client
  
    def find_by_id(self, team, params={}, **options): 
        """Returns the full record for a single team.

        Parameters
        ----------
        team : {Id} Globally unique identifier for the team.
        [params] : {Object} Parameters for the request
        """
        path = "/teams/%s" % (team)
        return self.client.get(path, params, **options)
        
    def find_by_organization(self, organization, params={}, **options): 
        """Returns the compact records for all teams in the organization visible to
        the authorized user.

        Parameters
        ----------
        organization : {Id} Globally unique identifier for the workspace or organization.
        [params] : {Object} Parameters for the request
        """
        path = "/organizations/%s/teams" % (organization)
        return self.client.get_collection(path, params, **options)
        
    def users(self, team, params={}, **options): 
        """Returns the compact records for all users that are members of the team.

        Parameters
        ----------
        team : {Id} Globally unique identifier for the team.
        [params] : {Object} Parameters for the request
        """
        path = "/teams/%s/users" % (team)
        return self.client.get_collection(path, params, **options)