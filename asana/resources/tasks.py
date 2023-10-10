
from .gen.tasks import _Tasks

class Tasks(_Tasks):
    """Tasks resource"""
    def set_parent(self, task_id, params={}, **options):
        """Changes the parent of a task. Each task may only be a subtask of a single
        parent, or no parent task at all. Returns an empty data block.

        Parameters
        ----------
        task : {Id} Globally unique identifier for the task.
        [data] : {Object} Data for the request
          - parent : {Id} The new parent of the task, or `null` for no parent.
        """
        path = '/tasks/%s/setParent' % (task_id)
        return self.client.post(path, params, **options)

    def create(self, params={}, **options):
        """Creating a new task is as easy as POSTing to the `/tasks` endpoint
        with a data block containing the fields you'd like to set on the task.
        Any unspecified fields will take on default values.

        Every task is required to be created in a specific workspace, and this
        workspace cannot be changed once set. The workspace need not be set
        explicitly if you specify `projects` or a `parent` task instead.

        `projects` can be a comma separated list of projects, or just a single
        project the task should belong to.

        Parameters
        ----------
        [data] : {Object} Data for the request
          - [workspace] : {Gid} The workspace to create a task in.
        """
        return self.client.post("/tasks", params, **options)

    def create_in_workspace(self, workspace, params={}, **options):
        """Creating a new task is as easy as POSTing to the `/tasks` endpoint
        with a data block containing the fields you'd like to set on the task.
        Any unspecified fields will take on default values.

        Every task is required to be created in a specific workspace, and this
        workspace cannot be changed once set. The workspace need not be set
        explicitly if you specify a `project` or a `parent` task instead.

        Parameters
        ----------
        workspace : {Gid} The workspace to create a task in.
        [data] : {Object} Data for the request
        """
        path = "/workspaces/%s/tasks" % (workspace)
        return self.client.post(path, params, **options)

    def find_by_id(self, task, params={}, **options):
        """Returns the complete task record for a single task.

        Parameters
        ----------
        task : {Gid} The task to get.
        [params] : {Object} Parameters for the request
        """
        path = "/tasks/%s" % (task)
        return self.client.get(path, params, **options)

    def update(self, task, params={}, **options):
        """A specific, existing task can be updated by making a PUT request on the
        URL for that task. Only the fields provided in the `data` block will be
        updated; any unspecified fields will remain unchanged.

        When using this method, it is best to specify only those fields you wish
        to change, or else you may overwrite changes made by another user since
        you last retrieved the task.

        Returns the complete updated task record.

        Parameters
        ----------
        task : {Gid} The task to update.
        [data] : {Object} Data for the request
        """
        path = "/tasks/%s" % (task)
        return self.client.put(path, params, **options)

    def delete(self, task, params={}, **options):
        """A specific, existing task can be deleted by making a DELETE request on the
        URL for that task. Deleted tasks go into the "trash" of the user making
        the delete request. Tasks can be recovered from the trash within a period
        of 30 days; afterward they are completely removed from the system.

        Returns an empty data record.

        Parameters
        ----------
        task : {Gid} The task to delete.
        """
        path = "/tasks/%s" % (task)
        return self.client.delete(path, params, **options)

    def duplicate_task(self, task, params={}, **options):
        """Creates and returns a job that will asynchronously handle the duplication.

        Parameters
        ----------
        task : {Gid} The task to duplicate.
        [data] : {Object} Data for the request
          - name : {String} The name of the new task.
          - [include] : {Array} The fields that will be duplicated to the new task.
        """
        path = "/tasks/%s/duplicate" % (task)
        return self.client.post(path, params, **options)

    def find_by_project(self, project, params={}, **options):
        """Returns the compact task records for all tasks within the given project,
        ordered by their priority within the project.

        Parameters
        ----------
        project : {Gid} The project in which to search for tasks.
        [params] : {Object} Parameters for the request
        """
        path = "/projects/%s/tasks" % (project)
        return self.client.get_collection(path, params, **options)

    def find_by_tag(self, tag, params={}, **options):
        """Returns the compact task records for all tasks with the given tag.

        Parameters
        ----------
        tag : {Gid} The tag in which to search for tasks.
        [params] : {Object} Parameters for the request
        """
        path = "/tags/%s/tasks" % (tag)
        return self.client.get_collection(path, params, **options)

    def find_by_section(self, section, params={}, **options):
        """<b>Board view only:</b> Returns the compact section records for all tasks within the given section.

        Parameters
        ----------
        section : {Gid} The section in which to search for tasks.
        [params] : {Object} Parameters for the request
        """
        path = "/sections/%s/tasks" % (section)
        return self.client.get_collection(path, params, **options)

    def find_by_user_task_list(self, user_task_list, params={}, **options):
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

    def find_all(self, params={}, **options):
        """Returns the compact task records for some filtered set of tasks. Use one
        or more of the parameters provided to filter the tasks returned. You must
        specify a `project`, `section`, `tag`, or `user_task_list` if you do not
        specify `assignee` and `workspace`.

        Parameters
        ----------
        [params] : {Object} Parameters for the request
          - [assignee] : {String} The assignee to filter tasks on.
          - [workspace] : {Gid} The workspace or organization to filter tasks on.
          - [project] : {Gid} The project to filter tasks on.
          - [section] : {Gid} The section to filter tasks on.
          - [tag] : {Gid} The tag to filter tasks on.
          - [user_task_list] : {Gid} The user task list to filter tasks on.
          - [completed_since] : {String} Only return tasks that are either incomplete or that have been
          completed since this time.
          - [modified_since] : {String} Only return tasks that have been modified since the given time.
        """
        return self.client.get_collection("/tasks", params, **options)

    def search_in_workspace(self, workspace, params={}, **options):
        """The search endpoint allows you to build complex queries to find and fetch exactly the data you need from Asana. For a more comprehensive description of all the query parameters and limitations of this endpoint, see our [long-form documentation](/developers/documentation/getting-started/search-api) for this feature.

        Parameters
        ----------
        workspace : {Gid} The workspace or organization in which to search for tasks.
        [params] : {Object} Parameters for the request
          - [resource_subtype] : {Enum} Filters results by the task's resource_subtype.
        """
        path = "/workspaces/%s/tasks/search" % (workspace)
        return self.client.get_collection(path, params, **options)

    def dependencies(self, task, params={}, **options):
        """Returns the compact representations of all of the dependencies of a task.

        Parameters
        ----------
        task : {Gid} The task to get dependencies on.
        [params] : {Object} Parameters for the request
        """
        path = "/tasks/%s/dependencies" % (task)
        return self.client.get(path, params, **options)

    def dependents(self, task, params={}, **options):
        """Returns the compact representations of all of the dependents of a task.

        Parameters
        ----------
        task : {Gid} The task to get dependents on.
        [params] : {Object} Parameters for the request
        """
        path = "/tasks/%s/dependents" % (task)
        return self.client.get(path, params, **options)

    def add_dependencies(self, task, params={}, **options):
        """Marks a set of tasks as dependencies of this task, if they are not
        already dependencies. *A task can have at most 15 dependencies.*

        Parameters
        ----------
        task : {Gid} The task to add dependencies to.
        [data] : {Object} Data for the request
          - dependencies : {Array} An array of task IDs that this task should depend on.
        """
        path = "/tasks/%s/addDependencies" % (task)
        return self.client.post(path, params, **options)

    def add_dependents(self, task, params={}, **options):
        """Marks a set of tasks as dependents of this task, if they are not already
        dependents. *A task can have at most 30 dependents.*

        Parameters
        ----------
        task : {Gid} The task to add dependents to.
        [data] : {Object} Data for the request
          - dependents : {Array} An array of task IDs that should depend on this task.
        """
        path = "/tasks/%s/addDependents" % (task)
        return self.client.post(path, params, **options)

    def remove_dependencies(self, task, params={}, **options):
        """Unlinks a set of dependencies from this task.

        Parameters
        ----------
        task : {Gid} The task to remove dependencies from.
        [data] : {Object} Data for the request
          - dependencies : {Array} An array of task IDs to remove as dependencies.
        """
        path = "/tasks/%s/removeDependencies" % (task)
        return self.client.post(path, params, **options)

    def remove_dependents(self, task, params={}, **options):
        """Unlinks a set of dependents from this task.

        Parameters
        ----------
        task : {Gid} The task to remove dependents from.
        [data] : {Object} Data for the request
          - dependents : {Array} An array of task IDs to remove as dependents.
        """
        path = "/tasks/%s/removeDependents" % (task)
        return self.client.post(path, params, **options)

    def add_followers(self, task, params={}, **options):
        """Adds each of the specified followers to the task, if they are not already
        following. Returns the complete, updated record for the affected task.

        Parameters
        ----------
        task : {Gid} The task to add followers to.
        [data] : {Object} Data for the request
          - followers : {Array} An array of followers to add to the task.
        """
        path = "/tasks/%s/addFollowers" % (task)
        return self.client.post(path, params, **options)

    def remove_followers(self, task, params={}, **options):
        """Removes each of the specified followers from the task if they are
        following. Returns the complete, updated record for the affected task.

        Parameters
        ----------
        task : {Gid} The task to remove followers from.
        [data] : {Object} Data for the request
          - followers : {Array} An array of followers to remove from the task.
        """
        path = "/tasks/%s/removeFollowers" % (task)
        return self.client.post(path, params, **options)

    def projects(self, task, params={}, **options):
        """Returns a compact representation of all of the projects the task is in.

        Parameters
        ----------
        task : {Gid} The task to get projects on.
        [params] : {Object} Parameters for the request
        """
        path = "/tasks/%s/projects" % (task)
        return self.client.get_collection(path, params, **options)

    def add_project(self, task, params={}, **options):
        """Adds the task to the specified project, in the optional location
        specified. If no location arguments are given, the task will be added to
        the end of the project.

        `addProject` can also be used to reorder a task within a project or section that
        already contains it.

        At most one of `insert_before`, `insert_after`, or `section` should be
        specified. Inserting into a section in an non-order-dependent way can be
        done by specifying `section`, otherwise, to insert within a section in a
        particular place, specify `insert_before` or `insert_after` and a task
        within the section to anchor the position of this task.

        Returns an empty data block.

        Parameters
        ----------
        task : {Gid} The task to add to a project.
        [data] : {Object} Data for the request
          - project : {Gid} The project to add the task to.
          - [insert_after] : {Gid} A task in the project to insert the task after, or `null` to
          insert at the beginning of the list.
          - [insert_before] : {Gid} A task in the project to insert the task before, or `null` to
          insert at the end of the list.
          - [section] : {Gid} A section in the project to insert the task into. The task will be
          inserted at the bottom of the section.
        """
        path = "/tasks/%s/addProject" % (task)
        return self.client.post(path, params, **options)

    def remove_project(self, task, params={}, **options):
        """Removes the task from the specified project. The task will still exist
        in the system, but it will not be in the project anymore.

        Returns an empty data block.

        Parameters
        ----------
        task : {Gid} The task to remove from a project.
        [data] : {Object} Data for the request
          - project : {Gid} The project to remove the task from.
        """
        path = "/tasks/%s/removeProject" % (task)
        return self.client.post(path, params, **options)

    def tags(self, task, params={}, **options):
        """Returns a compact representation of all of the tags the task has.

        Parameters
        ----------
        task : {Gid} The task to get tags on.
        [params] : {Object} Parameters for the request
        """
        path = "/tasks/%s/tags" % (task)
        return self.client.get_collection(path, params, **options)

    def add_tag(self, task, params={}, **options):
        """Adds a tag to a task. Returns an empty data block.

        Parameters
        ----------
        task : {Gid} The task to add a tag to.
        [data] : {Object} Data for the request
          - tag : {Gid} The tag to add to the task.
        """
        path = "/tasks/%s/addTag" % (task)
        return self.client.post(path, params, **options)

    def remove_tag(self, task, params={}, **options):
        """Removes a tag from the task. Returns an empty data block.

        Parameters
        ----------
        task : {Gid} The task to remove a tag from.
        [data] : {Object} Data for the request
          - tag : {Gid} The tag to remove from the task.
        """
        path = "/tasks/%s/removeTag" % (task)
        return self.client.post(path, params, **options)

    def subtasks(self, task, params={}, **options):
        """Returns a compact representation of all of the subtasks of a task.

        Parameters
        ----------
        task : {Gid} The task to get the subtasks of.
        [params] : {Object} Parameters for the request
        """
        path = "/tasks/%s/subtasks" % (task)
        return self.client.get_collection(path, params, **options)

    def add_subtask(self, task, params={}, **options):
        """Creates a new subtask and adds it to the parent task. Returns the full record
        for the newly created subtask.

        Parameters
        ----------
        task : {Gid} The task to add a subtask to.
        [data] : {Object} Data for the request
        """
        path = "/tasks/%s/subtasks" % (task)
        return self.client.post(path, params, **options)

    def stories(self, task, params={}, **options):
        """Returns a compact representation of all of the stories on the task.

        Parameters
        ----------
        task : {Gid} The task containing the stories to get.
        [params] : {Object} Parameters for the request
        """
        path = "/tasks/%s/stories" % (task)
        return self.client.get_collection(path, params, **options)

    def add_comment(self, task, params={}, **options):
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

    def insert_in_user_task_list(self, user_task_list, params={}, **options):
        """Insert or reorder tasks in a user's My Tasks list. If the task was not
        assigned to the owner of the user task list it will be reassigned when
        this endpoint is called. If neither `insert_before` nor `insert_after`
        are provided the task will be inserted at the top of the assignee's
        inbox.

        Returns an empty data block.

        Parameters
        ----------
        user_task_list : {Gid} Globally unique identifier for the user task list.
        [data] : {Object} Data for the request
          - task : {Gid} Globally unique identifier for the task.
          - [insert_before] : {Gid} Insert the task before the task specified by this field. The inserted
          task will inherit the `assignee_status` of this task. `insert_before`
          and `insert_after` parameters cannot both be specified.
          - [insert_after] : {Gid} Insert the task after the task specified by this field. The inserted
          task will inherit the `assignee_status` of this task. `insert_before`
          and `insert_after` parameters cannot both be specified.
        """
        path = "/user_task_lists/%s/tasks/insert" % (user_task_list)
        return self.client.post(path, params, **options)

