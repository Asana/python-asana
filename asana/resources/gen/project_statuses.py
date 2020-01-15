
class _ProjectStatuses:

    def __init__(self, client=None):
        self.client = client

    def create_project_status(self, project_gid, params={}, **options):
        """Create a project status
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: ProjectStatusResponse
        """
        path = "/projects/{project_gid}/project_statuses".replace("project_gid", project_gid)
        return self.client.get(path, params, **options)


    def delete_project_status(self, project_status_path_gid, params={}, **options):
        """Delete a project status
        :param str project_status_path_gid: The project status update to get. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/project_statuses/{project_status_gid}".replace("project_status_path_gid", project_status_path_gid)
        return self.client.get(path, params, **options)


    def get_project_status(self, project_status_path_gid, params={}, **options):
        """Get a project status
        :param str project_status_path_gid: The project status update to get. (required)
        [params] : {Object} Parameters for the request
        :return: ProjectStatusResponse
        """
        path = "/project_statuses/{project_status_gid}".replace("project_status_path_gid", project_status_path_gid)
        return self.client.get(path, params, **options)


    def get_project_statuses(self, project_gid, params={}, **options):
        """Get statuses from a project
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: list[ProjectStatusCompact]
        """
        path = "/projects/{project_gid}/project_statuses".replace("project_gid", project_gid)
        return self.client.get(path, params, **options)

