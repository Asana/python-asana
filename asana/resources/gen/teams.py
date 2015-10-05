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
        
    def add_user(self, team, params={}, **options): 
        """The user making this call must be a member of the team in order to add others.
        The user to add must exist in the same organization as the team in order to be added.
        The user to add can be referenced by their globally unique user ID or their email address.
        Returns the full user record for the added user.

        Parameters
        ----------
        team : {Id} Globally unique identifier for the team.
        [data] : {Object} Data for the request
          - user : {String} An identifier for the user. Can be one of an email address,
          the globally unique identifier for the user, or the keyword `me`
          to indicate the current user making the request.
        """
        path = "/teams/%s/addUser" % (team)
        return self.client.post(path, params, **options)
        
    def remove_user(self, team, params={}, **options): 
        """The user to remove can be referenced by their globally unique user ID or their email address.
        Removes the user from the specified team. Returns an empty data record.

        Parameters
        ----------
        team : {Id} Globally unique identifier for the team.
        [data] : {Object} Data for the request
          - user : {String} An identifier for the user. Can be one of an email address,
          the globally unique identifier for the user, or the keyword `me`
          to indicate the current user making the request.
        """
        path = "/teams/%s/removeUser" % (team)
        return self.client.post(path, params, **options)