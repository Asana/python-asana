class _Workspaces:
    """A _workspace_ is the highest-level organizational unit in Asana. All projects
    and tasks have an associated workspace.
    
    An _organization_ is a special kind of workspace that represents a company.
    In an organization, you can group your projects into teams. You can read
    more about how organizations work on the Asana Guide.
    To tell if your workspace is an organization or not, check its
    `is_organization` property.
    
    Over time, we intend to migrate most workspaces into organizations and to
    release more organization-specific functionality. We may eventually deprecate
    using workspace-based APIs for organizations. Currently, and until after
    some reasonable grace period following any further announcements, you can
    still reference organizations in any `workspace` parameter.
    """

    def __init__(self, client=None):
        self.client = client
  
    def find_by_id(self, workspace, params={}, **options): 
        """Returns the full workspace record for a single workspace.

        Parameters
        ----------
        workspace : {Id} Globally unique identifier for the workspace or organization.
        [params] : {Object} Parameters for the request
        """
        path = "/workspaces/%s" % (workspace)
        return self.client.get(path, params, **options)
        
    def find_all(self, params={}, **options): 
        """Returns the compact records for all workspaces visible to the authorized user.

        Parameters
        ----------
        [params] : {Object} Parameters for the request
        """
        return self.client.get_collection("/workspaces", params, **options)
        
    def update(self, workspace, params={}, **options): 
        """A specific, existing workspace can be updated by making a PUT request on
        the URL for that workspace. Only the fields provided in the data block
        will be updated; any unspecified fields will remain unchanged.
        
        Currently the only field that can be modified for a workspace is its `name`.
        
        Returns the complete, updated workspace record.

        Parameters
        ----------
        workspace : {Id} The workspace to update.
        [data] : {Object} Data for the request
        """
        path = "/workspaces/%s" % (workspace)
        return self.client.put(path, params, **options)
        
    def typeahead(self, workspace, params={}, **options): 
        """Retrieves objects in the workspace based on an auto-completion/typeahead
        search algorithm. This feature is meant to provide results quickly, so do
        not rely on this API to provide extremely accurate search results. The
        result set is limited to a single page of results with a maximum size,
        so you won't be able to fetch large numbers of results.

        Parameters
        ----------
        workspace : {Id} The workspace to fetch objects from.
        [params] : {Object} Parameters for the request
          - type : {Enum} The type of values the typeahead should return.
          Note that unlike in the names of endpoints, the types listed here are
          in singular form (e.g. `task`). Using multiple types is not yet supported.
          - [query] : {String} The string that will be used to search for relevant objects. If an
          empty string is passed in, the API will currently return an empty
          result set.
          - [count] : {Number} The number of results to return. The default is `20` if this
          parameter is omitted, with a minimum of `1` and a maximum of `100`.
          If there are fewer results found than requested, all will be returned.
        """
        path = "/workspaces/%s/typeahead" % (workspace)
        return self.client.get_collection(path, params, **options)
        
    def add_user(self, workspace, params={}, **options): 
        """The user can be referenced by their globally unique user ID or their email address.
        Returns the full user record for the invited user.

        Parameters
        ----------
        workspace : {Id} The workspace or organization to invite the user to.
        [data] : {Object} Data for the request
          - user : {String} An identifier for the user. Can be one of an email address,
          the globally unique identifier for the user, or the keyword `me`
          to indicate the current user making the request.
        """
        path = "/workspaces/%s/addUser" % (workspace)
        return self.client.post(path, params, **options)
        
    def remove_user(self, workspace, params={}, **options): 
        """The user making this call must be an admin in the workspace.
        Returns an empty data record.

        Parameters
        ----------
        workspace : {Id} The workspace or organization to invite the user to.
        [data] : {Object} Data for the request
          - user : {String} An identifier for the user. Can be one of an email address,
          the globally unique identifier for the user, or the keyword `me`
          to indicate the current user making the request.
        """
        path = "/workspaces/%s/removeUser" % (workspace)
        return self.client.post(path, params, **options)