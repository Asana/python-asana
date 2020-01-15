# coding=utf-8
class _BatchAPI:

    def __init__(self, client=None):
        self.client = client

    def create_batch_request_action(self, params={}, **options):
        """Submit parallel requests
        :param Object params: Parameters for the request
        :return: Object
        """
        path = "/batch"
        return self.client.get(path, params, **options)

