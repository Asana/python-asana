# coding=utf-8
class _TeamMemberships:

    def __init__(self, client=None):
        self.client = client

    def get_team_membership(self, team_membership_gid, params=None, **options):
        """Get a team membership
        :param str team_membership_gid: (required)
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/team_memberships/{team_membership_gid}".replace("{team_membership_gid}", team_membership_gid)
        return self.client.get(path, params, **options)

    def get_team_memberships(self, params=None, **options):
        """Get team memberships
        :param Object params: Parameters for the request
            - team {str}:  Globally unique identifier for the team.
            - user {str}:  A string identifying a user. This can either be the string \"me\", an email, or the gid of a user. This parameter must be used with the workspace parameter.
            - workspace {str}:  Globally unique identifier for the workspace. This parameter must be used with the user parameter.
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/team_memberships"
        return self.client.get_collection(path, params, **options)

    def get_team_memberships_for_team(self, team_gid, params=None, **options):
        """Get memberships from a team
        :param str team_gid: (required) Globally unique identifier for the team.
        :param Object params: Parameters for the request
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/teams/{team_gid}/team_memberships".replace("{team_gid}", team_gid)
        return self.client.get_collection(path, params, **options)

    def get_team_memberships_for_user(self, user_gid, params=None, **options):
        """Get memberships from a user
        :param str user_gid: (required) A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
        :param Object params: Parameters for the request
            - workspace {str}:  (required) Globally unique identifier for the workspace.
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/users/{user_gid}/team_memberships".replace("{user_gid}", user_gid)
        return self.client.get_collection(path, params, **options)
