# coding=utf-8
class _TaskTemplates:

    def __init__(self, client=None):
        self.client = client

    def delete_task_template(self, task_template_gid, params=None, **options):
        """Delete a task template
        :param str task_template_gid: (required) Globally unique identifier for the task template.
        :param Object params: Parameters for the request
        :param **options
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/task_templates/{task_template_gid}".replace("{task_template_gid}", task_template_gid)
        return self.client.delete(path, params, **options)

    def get_task_template(self, task_template_gid, params=None, **options):
        """Get a task template
        :param str task_template_gid: (required) Globally unique identifier for the task template.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/task_templates/{task_template_gid}".replace("{task_template_gid}", task_template_gid)
        return self.client.get(path, params, **options)

    def get_task_templates(self, params=None, **options):
        """Get multiple task templates
        :param Object params: Parameters for the request
            - project {str}:  The project to filter task templates on.
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/task_templates"
        return self.client.get_collection(path, params, **options)

    def instantiate_task(self, task_template_gid, params=None, **options):
        """Instantiate a task from a task template
        :param str task_template_gid: (required) Globally unique identifier for the task template.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/task_templates/{task_template_gid}/instantiateTask".replace("{task_template_gid}", task_template_gid)
        return self.client.post(path, params, **options)
