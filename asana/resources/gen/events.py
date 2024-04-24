# coding=utf-8
class _Events:

    def __init__(self, client=None):
        self.client = client

    def get_events(self, params=None, **options):
        """Get events on a resource
        :param Object params: Parameters for the request
            - resource {str}:  (required) A resource ID to subscribe to. The resource can be a task, project, or goal.
            - sync {str}:  A sync token received from the last request, or none on first sync. Events will be returned from the point in time that the sync token was generated. *Note: On your first request, omit the sync token. The response will be the same as for an expired sync token, and will include a new valid sync token.If the sync token is too old (which may happen from time to time) the API will return a `412 Precondition Failed` error, and include a fresh sync token in the response.*
        :param **options
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/events"
        return self.client.get_collection(path, params, **options)
