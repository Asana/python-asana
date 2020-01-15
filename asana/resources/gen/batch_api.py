
class _BatchAPI:

    def __init__(self, client=None):
        self.client = client

    def create_batch_request_action(self, params={}, **options):
        """Submit parallel requests
        [params] : {Object} Parameters for the request
        :return: list[BatchResponse]
        """
        path = "/batch"
        return self.client.get(path, params, **options)

