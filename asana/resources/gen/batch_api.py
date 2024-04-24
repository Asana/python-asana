# coding=utf-8
class _BatchAPI:

    def __init__(self, client=None):
        self.client = client

    def create_batch_request(self, params=None, **options):
        """Submit parallel requests
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/batch"
        return self.client.post(path, params, **options)
