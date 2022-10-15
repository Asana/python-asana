# coding=utf-8
class _Typeahead:

    def __init__(self, client=None):
        self.client = client

    def typeahead_for_workspace(self, workspace_gid, params=None, **options):
        """Get objects via typeahead
        :param str workspace_gid: (required) Globally unique identifier for the workspace or organization.
        :param Object params: Parameters for the request
            - resource_type {str}:  (required) The type of values the typeahead should return. You can choose from one of the following: `custom_field`, `project`, `project_template`, `portfolio`, `tag`, `task`, and `user`. Note that unlike in the names of endpoints, the types listed here are in singular form (e.g. `task`). Using multiple types is not yet supported.
            - type {str}:  *Deprecated: new integrations should prefer the resource_type field.*
            - query {str}:  The string that will be used to search for relevant objects. If an empty string is passed in, the API will return results.
            - count {int}:  The number of results to return. The default is 20 if this parameter is omitted, with a minimum of 1 and a maximum of 100. If there are fewer results found than requested, all will be returned.
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/workspaces/{workspace_gid}/typeahead".replace("{workspace_gid}", workspace_gid)
        return self.client.get_collection(path, params, **options)
