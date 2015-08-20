
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
