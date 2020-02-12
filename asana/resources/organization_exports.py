from .gen.organization_exports import _OrganizationExports


class OrganizationExports(_OrganizationExports):
    """The :class:`OrganizationExports` object, which represents the resource
    of the same name in Asana's API.

    """

    def find_by_id(self, organization_export, params={}, **options):
        """Returns details of a previously-requested Organization export.

        Parameters
        ----------
        organization_export : {Gid} Globally unique identifier for the Organization export.
        [params] : {Object} Parameters for the request
        """
        path = "/organization_exports/%s" % (organization_export)
        return self.client.get(path, params, **options)

    def create(self, params={}, **options):
        """This method creates a request to export an Organization. Asana will complete the export at some
        point after you create the request.

        Parameters
        ----------
        [data] : {Object} Data for the request
          - organization : {Gid} Globally unique identifier for the workspace or organization.
        """
        return self.client.post("/organization_exports", params, **options)
