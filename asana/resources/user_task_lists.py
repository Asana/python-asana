
from .gen.user_task_lists import _UserTaskLists

class UserTaskLists(_UserTaskLists):
    """User Task Lists resource"""
    def find_by_user(self, user, params={}, **options):
        """Returns the full record for the user task list for the given user

        Parameters
        ----------
        user : {String} An identifier for the user. Can be one of an email address,
        the globally unique identifier for the user, or the keyword `me`
        to indicate the current user making the request.
        [params] : {Object} Parameters for the request
          - workspace : {Gid} Globally unique identifier for the workspace or organization.
        """
        path = "/users/%s/user_task_list" % (user)
        return self.client.get(path, params, **options)

    def find_by_id(self, user_task_list, params={}, **options):
        """Returns the full record for a user task list.

        Parameters
        ----------
        user_task_list : {Gid} Globally unique identifier for the user task list.
        [params] : {Object} Parameters for the request
        """
        path = "/user_task_lists/%s" % (user_task_list)
        return self.client.get(path, params, **options)

    def tasks(self, user_task_list, params={}, **options):
        """Returns the compact list of tasks in a user's My Tasks list. The returned
        tasks will be in order within each assignee status group of `Inbox`,
        `Today`, and `Upcoming`.

        **Note:** tasks in `Later` have a different ordering in the Asana web app
        than the other assignee status groups; this endpoint will still return
        them in list order in `Later` (differently than they show up in Asana,
        but the same order as in Asana's mobile apps).

        **Note:** Access control is enforced for this endpoint as with all Asana
        API endpoints, meaning a user's private tasks will be filtered out if the
        API-authenticated user does not have access to them.

        **Note:** Both complete and incomplete tasks are returned by default
        unless they are filtered out (for example, setting `completed_since=now`
        will return only incomplete tasks, which is the default view for "My
        Tasks" in Asana.)

        Parameters
        ----------
        user_task_list : {Gid} The user task list in which to search for tasks.
        [params] : {Object} Parameters for the request
          - [completed_since] : {String} Only return tasks that are either incomplete or that have been
          completed since this time.
        """
        path = "/user_task_lists/%s/tasks" % (user_task_list)
        return self.client.get_collection(path, params, **options)


