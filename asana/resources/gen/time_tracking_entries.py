# coding=utf-8
class _TimeTrackingEntries:

    def __init__(self, client=None):
        self.client = client

    def create_time_tracking_entry(self, task_gid, params=None, **options):
        """Create a time tracking entry
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/time_tracking_entries".replace("{task_gid}", task_gid)
        return self.client.post(path, params, **options)

    def delete_time_tracking_entry(self, time_tracking_entry_gid, params=None, **options):
        """Delete a time tracking entry
        :param str time_tracking_entry_gid: (required) Globally unique identifier for the time tracking entry.
        :param Object params: Parameters for the request
        :param **options
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/time_tracking_entries/{time_tracking_entry_gid}".replace("{time_tracking_entry_gid}", time_tracking_entry_gid)
        return self.client.delete(path, params, **options)

    def get_time_tracking_entries_for_task(self, task_gid, params=None, **options):
        """Get time tracking entries for a task
        :param str task_gid: (required) The task to operate on.
        :param Object params: Parameters for the request
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/tasks/{task_gid}/time_tracking_entries".replace("{task_gid}", task_gid)
        return self.client.get_collection(path, params, **options)

    def get_time_tracking_entry(self, time_tracking_entry_gid, params=None, **options):
        """Get a time tracking entry
        :param str time_tracking_entry_gid: (required) Globally unique identifier for the time tracking entry.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/time_tracking_entries/{time_tracking_entry_gid}".replace("{time_tracking_entry_gid}", time_tracking_entry_gid)
        return self.client.get(path, params, **options)

    def update_time_tracking_entry(self, time_tracking_entry_gid, params=None, **options):
        """Update a time tracking entry
        :param str time_tracking_entry_gid: (required) Globally unique identifier for the time tracking entry.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/time_tracking_entries/{time_tracking_entry_gid}".replace("{time_tracking_entry_gid}", time_tracking_entry_gid)
        return self.client.put(path, params, **options)
