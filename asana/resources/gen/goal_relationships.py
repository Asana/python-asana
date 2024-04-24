# coding=utf-8
class _GoalRelationships:

    def __init__(self, client=None):
        self.client = client

    def add_supporting_relationship(self, goal_gid, params=None, **options):
        """Add a supporting goal relationship
        :param str goal_gid: (required) Globally unique identifier for the goal.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/goals/{goal_gid}/addSupportingRelationship".replace("{goal_gid}", goal_gid)
        return self.client.post(path, params, **options)

    def get_goal_relationship(self, goal_relationship_gid, params=None, **options):
        """Get a goal relationship
        :param str goal_relationship_gid: (required) Globally unique identifier for the goal relationship.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/goal_relationships/{goal_relationship_gid}".replace("{goal_relationship_gid}", goal_relationship_gid)
        return self.client.get(path, params, **options)

    def get_goal_relationships(self, params=None, **options):
        """Get goal relationships
        :param Object params: Parameters for the request
            - supported_goal {str}:  (required) Globally unique identifier for the supported goal in the goal relationship.
            - resource_subtype {str}:  If provided, filter to goal relationships with a given resource_subtype.
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/goal_relationships"
        return self.client.get_collection(path, params, **options)

    def remove_supporting_relationship(self, goal_gid, params=None, **options):
        """Removes a supporting goal relationship
        :param str goal_gid: (required) Globally unique identifier for the goal.
        :param Object params: Parameters for the request
        :param **options
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/goals/{goal_gid}/removeSupportingRelationship".replace("{goal_gid}", goal_gid)
        return self.client.post(path, params, **options)

    def update_goal_relationship(self, goal_relationship_gid, params=None, **options):
        """Update a goal relationship
        :param str goal_relationship_gid: (required) Globally unique identifier for the goal relationship.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/goal_relationships/{goal_relationship_gid}".replace("{goal_relationship_gid}", goal_relationship_gid)
        return self.client.put(path, params, **options)
