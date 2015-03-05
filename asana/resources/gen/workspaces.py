
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
    still reference organizations in any `workspace` parameter."""

    def __init__(self, client=None):
        self.client = client
  
    def find_by_id(self, workspace, params={}, **options): 
        """Returns the full workspace record for a single workspace."""
        
        path = "/workspaces/%d" % (workspace)
        return self.client.get(path, params, **options)
        
  
    def find_all(self, params={}, **options): 
        """Returns the compact records for all workspaces visible to the authorized user."""
        
        return self.client.get_collection("/workspaces", params, **options)
        
  
    def update(self, workspace, params={}, **options): 
        """Update properties on a workspace. Returns the complete, updated workspace record."""
        
        path = "/workspaces/%d" % (workspace)
        return self.client.put(path, params, **options)
        
  
    def typeahead(self, workspace, params={}, **options): 
        """Retrieves objects in the workspace based on an auto-completion/typeahead
        search algorithm. This feature is meant to provide results quickly, so do
        not rely on this API to provide extremely accurate search results. The
        result set is limited to a single page of results with a maximum size,
        so you won't be able to fetch large numbers of results."""
        
        path = "/workspaces/%d/typeahead" % (workspace)
        return self.client.get_collection(path, params, **options)
        
  
