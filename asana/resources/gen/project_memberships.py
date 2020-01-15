
class _ProjectMemberships:

    def __init__(self, client=None):
        self.client = client

    def get_project_membership(self, project_membership_path_gid, params={}, **options):
        """Get a project membership
        :param str project_membership_path_gid: (required)
        [params] : {Object} Parameters for the request
        :return: ProjectMembershipResponse
        """
        path = "/project_memberships/{project_membership_gid}".replace("project_membership_path_gid", project_membership_path_gid)
        return self.client.get(path, params, **options)


    def get_project_memberships_for_project(self, project_gid, params={}, **options):
        """Get memberships from a project
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: list[ProjectMembershipCompact]
        """
        path = "/projects/{project_gid}/project_memberships".replace("project_gid", project_gid)
        return self.client.get(path, params, **options)

