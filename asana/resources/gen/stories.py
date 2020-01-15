
class _Stories:

    def __init__(self, client=None):
        self.client = client

    def create_story(self, task_gid, params={}, **options):
        """Create a story on a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: StoryResponse
        """
        path = "/tasks/{task_gid}/stories".replace("task_gid", task_gid)
        return self.client.get(path, params, **options)


    def delete_story(self, story_gid, params={}, **options):
        """Delete a story
        :param str story_gid: Globally unique identifier for the story. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/stories/{story_gid}".replace("story_gid", story_gid)
        return self.client.get(path, params, **options)


    def get_stories_for_task(self, task_gid, params={}, **options):
        """Get stories from a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: list[StoryCompact]
        """
        path = "/tasks/{task_gid}/stories".replace("task_gid", task_gid)
        return self.client.get(path, params, **options)


    def get_story(self, story_gid, params={}, **options):
        """Get a story
        :param str story_gid: Globally unique identifier for the story. (required)
        [params] : {Object} Parameters for the request
        :return: StoryResponse
        """
        path = "/stories/{story_gid}".replace("story_gid", story_gid)
        return self.client.get(path, params, **options)


    def update_story(self, story_gid, params={}, **options):
        """Update a story
        :param str story_gid: Globally unique identifier for the story. (required)
        [params] : {Object} Parameters for the request
        :return: StoryResponse
        """
        path = "/stories/{story_gid}".replace("story_gid", story_gid)
        return self.client.get(path, params, **options)

