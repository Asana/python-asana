
class _Users:
    """A _user_ object represents an account in Asana that can be given access to
    various workspaces, projects, and tasks.
    
    Like other objects in the system, users are referred to by numerical IDs.
    However, the special string identifier `me` can be used anywhere
    a user ID is accepted, to refer to the current authenticated user."""

    def __init__(self, client=None):
        self.client = client
  
    def me(self, params={}, **options): 
        """Returns the full user record for the currently authenticated user.

        Parameters
        ----------
        params : Object
          Parameters for the request
        """
        
        return self.client.get("/users/me", params, **options)
        
  
    def find_by_id(self, user, params={}, **options): 
        """Returns the full user record for a single user.

        Parameters
        ----------
        user : Id
          Globally unique identifier for the user.
        params : Object
          Parameters for the request
        """
        
        path = "/users/%d" % (user)
        return self.client.get(path, params, **options)
        
  
    def find_by_workspace(self, workspace, params={}, **options): 
        """Returns the user records for all users in all workspaces and organizations
        accessible to the authenticated user.

        Parameters
        ----------
        workspace : Id
          The workspace in which to get users.
        params : Object
          Parameters for the request
        """
        
        path = "/workspaces/%d/users" % (workspace)
        return self.client.get_collection(path, params, **options)
        
  
    def find_all(self, params={}, **options): 
        """Returns the user records for all users in the specified workspace or
        organization.

        Parameters
        ----------
        params : Object
          Parameters for the request
        workspace : Id
          The workspace or organization to filter users on.
        """
        
        return self.client.get_collection("/users", params, **options)
        
  
