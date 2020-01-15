
class _Typeahead:

    def __init__(self, client=None):
        self.client = client

    def typeahead_for_workspace(self, workspace_gid, params={}, **options):
        """Get objects via typeahead
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        [params] : {Object} Parameters for the request
        :return: list[AsanaNamedResource]
        """
        path = "/workspaces/{workspace_gid}/typeahead".replace("{workspace_gid}", workspace_gid)
        return self.client.get(path, params, **options)

