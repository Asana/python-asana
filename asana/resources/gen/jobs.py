
class _Jobs:

    def __init__(self, client=None):
        self.client = client

    def get_job(self, job_gid, params={}, **options):
        """Get a job by id
        :param str job_gid: Globally unique identifier for the job. (required)
        [params] : {Object} Parameters for the request
        :return: JobResponse
        """
        path = "/jobs/{job_gid}".replace("{job_gid}", job_gid)
        return self.client.get(path, params, **options)

