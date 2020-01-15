
from .gen.jobs import _Jobs

class Jobs(_Jobs):
    """Jobs resource"""
    def find_by_id(self, job, params={}, **options):
        """Returns the complete job record for a single job.

        Parameters
        ----------
        job : {Gid} The job to get.
        [params] : {Object} Parameters for the request
        """
        path = "/jobs/%s" % (job)
        return self.client.get(path, params, **options)
