
from .gen.stories import _Stories

class Stories(_Stories):
    """Stories resource"""
    def find_by_task(self, task, params={}, **options):
        """Returns the compact records for all stories on the task.

        Parameters
        ----------
        task : {Gid} Globally unique identifier for the task.
        [params] : {Object} Parameters for the request
        """
        path = "/tasks/%s/stories" % (task)
        return self.client.get_collection(path, params, **options)

    def find_by_id(self, story, params={}, **options):
        """Returns the full record for a single story.

        Parameters
        ----------
        story : {Gid} Globally unique identifier for the story.
        [params] : {Object} Parameters for the request
        """
        path = "/stories/%s" % (story)
        return self.client.get(path, params, **options)

    def create_on_task(self, task, params={}, **options):
        """Adds a comment to a task. The comment will be authored by the
        currently authenticated user, and timestamped when the server receives
        the request.

        Returns the full record for the new story added to the task.

        Parameters
        ----------
        task : {Id} Globally unique identifier for the task.
        [data] : {Object} Data for the request
          - text : {String} The plain text of the comment to add.
        """
        path = "/tasks/%s/stories" % (task)
        return self.client.post(path, params, **options)

    def update(self, story, params={}, **options):
        """Updates the story and returns the full record for the updated story.
        Only comment stories can have their text updated, and only comment stories and
        attachment stories can be pinned. Only one of `text` and `html_text` can be specified.

        Parameters
        ----------
        story : {Gid} Globally unique identifier for the story.
        [data] : {Object} Data for the request
          - [text] : {String} The plain text with which to update the comment.
          - [html_text] : {String} The rich text with which to update the comment.
          - [is_pinned] : {Boolean} Whether the story should be pinned on the resource.
        """
        path = "/stories/%s" % (story)
        return self.client.put(path, params, **options)

    def delete(self, story, params={}, **options):
        """Deletes a story. A user can only delete stories they have created. Returns an empty data record.

        Parameters
        ----------
        story : {Gid} Globally unique identifier for the story.
        """
        path = "/stories/%s" % (story)
        return self.client.delete(path, params, **options)


