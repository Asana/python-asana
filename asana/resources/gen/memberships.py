# coding=utf-8
class _Memberships:

    def __init__(self, client=None):
        self.client = client

    def create_membership(self, params=None, **options):
        """Create a membership
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/memberships"
        return self.client.post(path, params, **options)

    def delete_membership(self, membership_gid, params=None, **options):
        """Delete a membership
        :param str membership_gid: (required) Globally unique identifier for the membership.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/memberships/{membership_gid}".replace("{membership_gid}", membership_gid)
        return self.client.delete(path, params, **options)

    def get_memberships(self, params=None, **options):
        """Get multiple memberships
        :param Object params: Parameters for the request
            - parent {str}:  Globally unique identifier for `project`, `portfolio`,   `team`, `goal`, and `workspace`.
            - member {str}:  Globally unique identifier for `team` or `user`.
            - resource_subtype {str}:  The resource_subtype to filter on. Must be provided with `member` and `workspace` if `parent` is not provided. Valid values include `team_membership`, `workspace_membership`, `portfolio_membership`
            - workspace {str}:  The workspace to filter on. Must be provided with `member` and `resource_subtype` if `parent` is not provided.
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Pagination limit for the request.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/memberships"
        return self.client.get_collection(path, params, **options)

    def update_membership(self, membership_gid, params=None, **options):
        """Update a membership
        :param str membership_gid: (required) Globally unique identifier for the membership.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/memberships/{membership_gid}".replace("{membership_gid}", membership_gid)
        return self.client.put(path, params, **options)
