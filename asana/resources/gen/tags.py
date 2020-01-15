
class _Tags:

    def __init__(self, client=None):
        self.client = client

    def create_tag(self, params={}, **options):
        """Create a tag
        [params] : {Object} Parameters for the request
        :return: TagResponse
        """
        path = "/tags"
        return self.client.get(path, params, **options)


    def create_tag_for_workspace(self, workspace_gid, params={}, **options):
        """Create a tag in a workspace
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        [params] : {Object} Parameters for the request
        :return: TagResponse
        """
        path = "/workspaces/{workspace_gid}/tags".replace("workspace_gid", workspace_gid)
        return self.client.get(path, params, **options)


    def get_tag(self, tag_gid, params={}, **options):
        """Get a tag
        :param str tag_gid: Globally unique identifier for the tag. (required)
        [params] : {Object} Parameters for the request
        :return: TagResponse
        """
        path = "/tags/{tag_gid}".replace("tag_gid", tag_gid)
        return self.client.get(path, params, **options)


    def get_tags(self, params={}, **options):
        """Get multiple tags
        [params] : {Object} Parameters for the request
        :return: list[TagCompact]
        """
        path = "/tags"
        return self.client.get(path, params, **options)


    def get_tags_for_task(self, task_gid, params={}, **options):
        """Get a task's tags
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: list[TagCompact]
        """
        path = "/tasks/{task_gid}/tags".replace("task_gid", task_gid)
        return self.client.get(path, params, **options)


    def get_tags_for_workspace(self, workspace_gid, params={}, **options):
        """Get tags in a workspace
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        [params] : {Object} Parameters for the request
        :return: list[TagCompact]
        """
        path = "/workspaces/{workspace_gid}/tags".replace("workspace_gid", workspace_gid)
        return self.client.get(path, params, **options)


    def update_tag(self, tag_gid, params={}, **options):
        """Update a tag
        :param str tag_gid: Globally unique identifier for the tag. (required)
        [params] : {Object} Parameters for the request
        :return: TagResponse
        """
        path = "/tags/{tag_gid}".replace("tag_gid", tag_gid)
        return self.client.get(path, params, **options)

