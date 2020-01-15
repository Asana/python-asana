
class _OrganizationExports:

    def __init__(self, client=None):
        self.client = client

    def create_organization_export(self, params={}, **options):
        """Create an organization export request
        [params] : {Object} Parameters for the request
        :return: OrganizationExportResponse
        """
        path = "/organization_exports"
        return self.client.get(path, params, **options)


    def get_organization_export(self, organization_export_gid, params={}, **options):
        """Get details on an org export request
        :param str organization_export_gid: Globally unique identifier for the organization export. (required)
        [params] : {Object} Parameters for the request
        :return: OrganizationExportResponse
        """
        path = "/organization_exports/{organization_export_gid}".replace("{organization_export_gid}", organization_export_gid)
        return self.client.get(path, params, **options)

