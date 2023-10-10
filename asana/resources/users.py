
from .gen.users import _Users

class Users(_Users):
    """Users resource"""
    def me(self, params={}, **options):
        """Returns the full user record for the currently authenticated user.

        Parameters
        ----------
        [params] : {Object} Parameters for the request
        """
        return self.client.get("/users/me", params, **options)

    def find_by_id(self, user, params={}, **options):
        """Returns the full user record for the single user with the provided ID.

        Parameters
        ----------
        user : {String} An identifier for the user. Can be one of an email address,
        the globally unique identifier for the user, or the keyword `me`
        to indicate the current user making the request.
        [params] : {Object} Parameters for the request
        """
        path = "/users/%s" % (user)
        return self.client.get(path, params, **options)

    def get_user_favorites(self, user, params={}, **options):
        """Returns all of a user's favorites in the given workspace, of the given type.
        Results are given in order (The same order as Asana's sidebar).

        Parameters
        ----------
        user : {String} An identifier for the user. Can be one of an email address,
        the globally unique identifier for the user, or the keyword `me`
        to indicate the current user making the request.
        [params] : {Object} Parameters for the request
          - workspace : {Id} The workspace in which to get favorites.
          - resource_type : {Enum} The resource type of favorites to be returned.
        """
        path = "/users/%s/favorites" % (user)
        return self.client.get_collection(path, params, **options)

    def find_by_workspace(self, workspace, params={}, **options):
        """Returns the user records for all users in the specified workspace or
        organization.

        Parameters
        ----------
        workspace : {Id} The workspace in which to get users.
        [params] : {Object} Parameters for the request
        """
        path = "/workspaces/%s/users" % (workspace)
        return self.client.get_collection(path, params, **options)

    def find_all(self, params={}, **options):
        """Returns the user records for all users in all workspaces and organizations
        accessible to the authenticated user. Accepts an optional workspace ID
        parameter.

        Parameters
        ----------
        [params] : {Object} Parameters for the request
          - [workspace] : {Id} The workspace or organization to filter users on.
        """
        return self.client.get_collection("/users", params, **options)


