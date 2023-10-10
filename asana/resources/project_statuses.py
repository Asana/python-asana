
from .gen.project_statuses import _ProjectStatuses

class ProjectStatuses(_ProjectStatuses):
    """Project Statuses resource"""
    def create(self, project, params={}, **options):
        self.create_in_project(project, params, **options)

    def create_in_project(self, project, params={}, **options):
        """Creates a new status update on the project.

        Returns the full record of the newly created project status update.

        Parameters
        ----------
        project : {Gid} The project on which to create a status update.
        [data] : {Object} Data for the request
          - text : {String} The text of the project status update.
          - color : {String} The color to associate with the status update. Must be one of `"red"`, `"yellow"`, or `"green"`.
        """
        path = "/projects/%s/project_statuses" % (project)
        return self.client.post(path, params, **options)

    def find_by_project(self, project, params={}, **options):
        """Returns the compact project status update records for all updates on the project.

        Parameters
        ----------
        project : {Gid} The project to find status updates for.
        [params] : {Object} Parameters for the request
        """
        path = "/projects/%s/project_statuses" % (project)
        return self.client.get_collection(path, params, **options)

    def find_by_id(self, project_status, params={}, **options):
        """Returns the complete record for a single status update.

        Parameters
        ----------
        project-status : {Gid} The project status update to get.
        [params] : {Object} Parameters for the request
        """
        path = "/project_statuses/%s" % (project_status)
        return self.client.get(path, params, **options)

    def delete(self, project_status, params={}, **options):
        """Deletes a specific, existing project status update.

        Returns an empty data record.

        Parameters
        ----------
        project-status : {Gid} The project status update to delete.
        """
        path = "/project_statuses/%s" % (project_status)
        return self.client.delete(path, params, **options)
