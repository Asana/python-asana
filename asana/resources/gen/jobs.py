
class _Jobs:
    """A _job_ represents a process that handles asynchronous work.
    
    Jobs are created when an endpoint requests an action that will be handled asynchronously.
    Such as project or task duplication.
    """

    def __init__(self, client=None):
        self.client = client
  
    def find_by_id(self, job, params={}, **options): 
        """Returns the complete job record for a single job.

        Parameters
        ----------
        job : {Gid} The job to get.
        [params] : {Object} Parameters for the request
        """
        path = "/jobs/%s" % (job)
        return self.client.get(path, params, **options)
        
