
class _Tasks:
    """The _task_ is the basic object around which many operations in Asana are
    centered. In the Asana application, multiple tasks populate the middle pane
    according to some view parameters, and the set of selected tasks determines
    the more detailed information presented in the details pane.
    """

    def __init__(self, client=None):
        self.client = client
  
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
          - [workspace] : {Id} The workspace to create a task in.
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
        workspace : {Id} The workspace to create a task in.
        [data] : {Object} Data for the request
        """
        path = "/workspaces/%s/tasks" % (workspace)
        return self.client.post(path, params, **options)
        
    def find_by_id(self, task, params={}, **options): 
        """Returns the complete task record for a single task.

        Parameters
        ----------
        task : {Id} The task to get.
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
        task : {Id} The task to update.
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
        task : {Id} The task to delete.
        """
        path = "/tasks/%s" % (task)
        return self.client.delete(path, params, **options)
        
    def find_by_project(self, project_id, params={}, **options): 
        """Returns the compact task records for all tasks within the given project,
        ordered by their priority within the project.

        Parameters
        ----------
        projectId : {Id} The project in which to search for tasks.
        [params] : {Object} Parameters for the request
        """
        path = "/projects/%s/tasks" % (project_id)
        return self.client.get_collection(path, params, **options)
        
    def find_by_tag(self, tag, params={}, **options): 
        """Returns the compact task records for all tasks with the given tag.

        Parameters
        ----------
        tag : {Id} The tag in which to search for tasks.
        [params] : {Object} Parameters for the request
        """
        path = "/tags/%s/tasks" % (tag)
        return self.client.get_collection(path, params, **options)
        
    def find_by_section(self, section, params={}, **options): 
        """<b>Board view only:</b> Returns the compact section records for all tasks within the given section.

        Parameters
        ----------
        section : {Id} The section in which to search for tasks.
        [params] : {Object} Parameters for the request
        """
        path = "/sections/%s/tasks" % (section)
        return self.client.get_collection(path, params, **options)
        
    def find_all(self, params={}, **options): 
        """Returns the compact task records for some filtered set of tasks. Use one
        or more of the parameters provided to filter the tasks returned. You must
        specify a `project` or `tag` if you do not specify `assignee` and `workspace`.

        Parameters
        ----------
        [params] : {Object} Parameters for the request
          - [assignee] : {String} The assignee to filter tasks on.
          - [project] : {Id} The project to filter tasks on.
          - [section] : {Id} The section to filter tasks on.
          - [workspace] : {Id} The workspace or organization to filter tasks on.
          - [completed_since] : {String} Only return tasks that are either incomplete or that have been
          completed since this time.
          - [modified_since] : {String} Only return tasks that have been modified since the given time.
        """
        return self.client.get_collection("/tasks", params, **options)
        
    def search_in_workspace(self, workspace, params={}, **options): 
        """The search endpoint allows you to build complex queries to find and fetch exactly the data you need from Asana. For a more comprehensive description of all the query parameters and limitations of this endpoint, see our [long-form documentation](/developers/documentation/getting-started/search-api) for this feature.

        Parameters
        ----------
        workspace : {Id} The workspace or organization in which to search for tasks.
        [params] : {Object} Parameters for the request
        """
        path = "/workspaces/%s/tasks/search" % (workspace)
        return self.client.get_collection(path, params, **options)
        
    def dependencies(self, task, params={}, **options): 
        """Returns the compact representations of all of the dependencies of a task.

        Parameters
        ----------
        task : {Id} The task to get dependencies on.
        [params] : {Object} Parameters for the request
        """
        path = "/tasks/%s/dependencies" % (task)
        return self.client.get(path, params, **options)
        
    def dependents(self, task, params={}, **options): 
        """Returns the compact representations of all of the dependents of a task.

        Parameters
        ----------
        task : {Id} The task to get dependents on.
        [params] : {Object} Parameters for the request
        """
        path = "/tasks/%s/dependents" % (task)
        return self.client.get(path, params, **options)
        
    def add_dependencies(self, task, params={}, **options): 
        """Marks a set of tasks as dependencies of this task, if they are not
        already dependencies. *A task can have at most 15 dependencies.*

        Parameters
        ----------
        task : {Id} The task to add dependencies to.
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
        task : {Id} The task to add dependents to.
        [data] : {Object} Data for the request
          - dependents : {Array} An array of task IDs that should depend on this task.
        """
        path = "/tasks/%s/addDependents" % (task)
        return self.client.post(path, params, **options)
        
    def remove_dependencies(self, task, params={}, **options): 
        """Unlinks a set of dependencies from this task.

        Parameters
        ----------
        task : {Id} The task to remove dependencies from.
        [data] : {Object} Data for the request
          - dependencies : {Array} An array of task IDs to remove as dependencies.
        """
        path = "/tasks/%s/removeDependencies" % (task)
        return self.client.post(path, params, **options)
        
    def remove_dependents(self, task, params={}, **options): 
        """Unlinks a set of dependents from this task.

        Parameters
        ----------
        task : {Id} The task to remove dependents from.
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
        task : {Id} The task to add followers to.
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
        task : {Id} The task to remove followers from.
        [data] : {Object} Data for the request
          - followers : {Array} An array of followers to remove from the task.
        """
        path = "/tasks/%s/removeFollowers" % (task)
        return self.client.post(path, params, **options)
        
    def projects(self, task, params={}, **options): 
        """Returns a compact representation of all of the projects the task is in.

        Parameters
        ----------
        task : {Id} The task to get projects on.
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
        task : {Id} The task to add to a project.
        [data] : {Object} Data for the request
          - project : {Id} The project to add the task to.
          - [insert_after] : {Id} A task in the project to insert the task after, or `null` to
          insert at the beginning of the list.
          - [insert_before] : {Id} A task in the project to insert the task before, or `null` to
          insert at the end of the list.
          - [section] : {Id} A section in the project to insert the task into. The task will be
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
        task : {Id} The task to remove from a project.
        [data] : {Object} Data for the request
          - project : {Id} The project to remove the task from.
        """
        path = "/tasks/%s/removeProject" % (task)
        return self.client.post(path, params, **options)
        
    def tags(self, task, params={}, **options): 
        """Returns a compact representation of all of the tags the task has.

        Parameters
        ----------
        task : {Id} The task to get tags on.
        [params] : {Object} Parameters for the request
        """
        path = "/tasks/%s/tags" % (task)
        return self.client.get_collection(path, params, **options)
        
    def add_tag(self, task, params={}, **options): 
        """Adds a tag to a task. Returns an empty data block.

        Parameters
        ----------
        task : {Id} The task to add a tag to.
        [data] : {Object} Data for the request
          - tag : {Id} The tag to add to the task.
        """
        path = "/tasks/%s/addTag" % (task)
        return self.client.post(path, params, **options)
        
    def remove_tag(self, task, params={}, **options): 
        """Removes a tag from the task. Returns an empty data block.

        Parameters
        ----------
        task : {Id} The task to remove a tag from.
        [data] : {Object} Data for the request
          - tag : {Id} The tag to remove from the task.
        """
        path = "/tasks/%s/removeTag" % (task)
        return self.client.post(path, params, **options)
        
    def subtasks(self, task, params={}, **options): 
        """Returns a compact representation of all of the subtasks of a task.

        Parameters
        ----------
        task : {Id} The task to get the subtasks of.
        [params] : {Object} Parameters for the request
        """
        path = "/tasks/%s/subtasks" % (task)
        return self.client.get_collection(path, params, **options)
        
    def add_subtask(self, task, params={}, **options): 
        """Creates a new subtask and adds it to the parent task. Returns the full record
        for the newly created subtask.

        Parameters
        ----------
        task : {Id} The task to add a subtask to.
        [data] : {Object} Data for the request
        """
        path = "/tasks/%s/subtasks" % (task)
        return self.client.post(path, params, **options)
        
    def stories(self, task, params={}, **options): 
        """Returns a compact representation of all of the stories on the task.

        Parameters
        ----------
        task : {Id} The task containing the stories to get.
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
        
