# coding=utf-8
class _ProjectMemberships:

    def __init__(self, client=None):
        self.client = client

    def get_project_membership(self, project_membership_gid, params=None, **options):
        """Get a project membership
        :param str project_membership_gid: (required)
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/project_memberships/{project_membership_gid}".replace("{project_membership_gid}", project_membership_gid)
        return self.client.get(path, params, **options)

    def get_project_memberships_for_project(self, project_gid, params=None, **options):
        """Get memberships from a project
        :param str project_gid: (required) Globally unique identifier for the project.
        :param Object params: Parameters for the request
            - user {str}:  A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/projects/{project_gid}/project_memberships".replace("{project_gid}", project_gid)
        return self.client.get_collection(path, params, **options)
