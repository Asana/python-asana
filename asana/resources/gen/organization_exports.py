class _OrganizationExports:
    """An _organization_export_ object represents a request to export the complete data of an Organization
    in JSON format.
    
    To export an Organization using this API:
    
    * Create an `organization_export` [request](#create) and store the id that is returned.\
    * Request the `organization_export` every few minutes, until the `state` field contains 'finished'.\
    * Download the file located at the URL in the `download_url` field.
    
    Exports can take a long time, from several minutes to a few hours for large Organizations.
    
    **Note:** These endpoints are only available to [Service Accounts](/guide/help/premium/service-accounts)
    of an [Enterprise](/enterprise) Organization.
    """

    def __init__(self, client=None):
        self.client = client
  
    def find_by_id(self, organization_export, params={}, **options): 
        """Returns details of a previously-requested Organization export.

        Parameters
        ----------
        organization_export : {Id} Globally unique identifier for the Organization export.
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
          - organization : {Id} Globally unique identifier for the workspace or organization.
        """
        return self.client.post("/organization_exports", params, **options)