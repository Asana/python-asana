# coding=utf-8
class _OrganizationExports:

    def __init__(self, client=None):
        self.client = client

    def create_organization_export(self, params=None, **options):
        """Create an organization export request
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/organization_exports"
        return self.client.post(path, params, **options)

    def get_organization_export(self, organization_export_gid, params=None, **options):
        """Get details on an org export request
        :param str organization_export_gid: (required) Globally unique identifier for the organization export.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/organization_exports/{organization_export_gid}".replace("{organization_export_gid}", organization_export_gid)
        return self.client.get(path, params, **options)
