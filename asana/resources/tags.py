
from .gen.tags import _Tags

class Tags(_Tags):
    """Tags resource"""
    def create(self, params={}, **options):
        """Creates a new tag in a workspace or organization.

        Every tag is required to be created in a specific workspace or
        organization, and this cannot be changed once set. Note that you can use
        the `workspace` parameter regardless of whether or not it is an
        organization.

        Returns the full record of the newly created tag.

        Parameters
        ----------
        [data] : {Object} Data for the request
          - workspace : {Gid} The workspace or organization to create the tag in.
        """
        return self.client.post("/tags", params, **options)

    def create_in_workspace(self, workspace, params={}, **options):
        """Creates a new tag in a workspace or organization.

        Every tag is required to be created in a specific workspace or
        organization, and this cannot be changed once set. Note that you can use
        the `workspace` parameter regardless of whether or not it is an
        organization.

        Returns the full record of the newly created tag.

        Parameters
        ----------
        workspace : {Gid} The workspace or organization to create the tag in.
        [data] : {Object} Data for the request
        """
        path = "/workspaces/%s/tags" % (workspace)
        return self.client.post(path, params, **options)

    def find_by_id(self, tag, params={}, **options):
        """Returns the complete tag record for a single tag.

        Parameters
        ----------
        tag : {Gid} The tag to get.
        [params] : {Object} Parameters for the request
        """
        path = "/tags/%s" % (tag)
        return self.client.get(path, params, **options)

    def update(self, tag, params={}, **options):
        """Updates the properties of a tag. Only the fields provided in the `data`
        block will be updated; any unspecified fields will remain unchanged.

        When using this method, it is best to specify only those fields you wish
        to change, or else you may overwrite changes made by another user since
        you last retrieved the task.

        Returns the complete updated tag record.

        Parameters
        ----------
        tag : {Gid} The tag to update.
        [data] : {Object} Data for the request
        """
        path = "/tags/%s" % (tag)
        return self.client.put(path, params, **options)

    def delete(self, tag, params={}, **options):
        """A specific, existing tag can be deleted by making a DELETE request
        on the URL for that tag.

        Returns an empty data record.

        Parameters
        ----------
        tag : {Gid} The tag to delete.
        """
        path = "/tags/%s" % (tag)
        return self.client.delete(path, params, **options)

    def find_all(self, params={}, **options):
        """Returns the compact tag records for some filtered set of tags.
        Use one or more of the parameters provided to filter the tags returned.

        Parameters
        ----------
        [params] : {Object} Parameters for the request
          - [workspace] : {Gid} The workspace or organization to filter tags on.
          - [team] : {Gid} The team to filter tags on.
          - [archived] : {Boolean} Only return tags whose `archived` field takes on the value of
          this parameter.
        """
        return self.client.get_collection("/tags", params, **options)

    def find_by_workspace(self, workspace, params={}, **options):
        """Returns the compact tag records for all tags in the workspace.

        Parameters
        ----------
        workspace : {Gid} The workspace or organization to find tags in.
        [params] : {Object} Parameters for the request
        """
        path = "/workspaces/%s/tags" % (workspace)
        return self.client.get_collection(path, params, **options)

    def get_tasks_with_tag(self, tag, params={}, **options):
        """Returns the compact task records for all tasks with the given tag.
        Tasks can have more than one tag at a time.
        Parameters
        ----------
        tag : {Id} The tag to fetch tasks from.
        [params] : {Object} Parameters for the request
        """
        path = "/tags/%s/tasks" % (tag)
        return self.client.get_collection(path, params, **options)

