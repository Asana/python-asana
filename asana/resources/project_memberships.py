
from .gen.project_memberships import _ProjectMemberships

class ProjectMemberships(_ProjectMemberships):
    """Project Memberships resource"""

    def find_by_project(self, project, params={}, **options):
        """Returns the compact project membership records for the project.

        Parameters
        ----------
        project : {Gid} The project for which to fetch memberships.
        [params] : {Object} Parameters for the request
          - [user] : {String} If present, the user to filter the memberships to.
        """
        path = "/projects/%s/project_memberships" % (project)
        return self.client.get_collection(path, params, **options)

    def find_by_id(self, project_membership, params={}, **options):
        """Returns the project membership record.

        Parameters
        ----------
        project_membership : {Gid} Globally unique identifier for the project membership.
        [params] : {Object} Parameters for the request
        """
        path = "/project_memberships/%s" % (project_membership)
        return self.client.get(path, params, **options)

