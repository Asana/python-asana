class _CustomFields:
    """Custom Fields store the metadata that is used in order to add user-specified
    information to tasks in Asana. Be sure to reference the [Custom
    Fields](/developers/documentation/getting-started/custom-fields) developer
    documentation for more information about how custom fields relate to various
    resources in Asana.
    """

    def __init__(self, client=None):
        self.client = client
  
    def find_by_id(self, custom_field, params={}, **options): 
        """Returns the complete definition of a custom field's metadata.

        Parameters
        ----------
        custom-field : {Id} Globally unique identifier for the custom field.
        [params] : {Object} Parameters for the request
        """
        path = "/custom_fields/%s" % (custom_field)
        return self.client.get(path, params, **options)
        
    def find_by_workspace(self, workspace, params={}, **options): 
        """Returns a list of the compact representation of all of the custom fields in a workspace.

        Parameters
        ----------
        workspace : {Id} The workspace or organization to find custom field definitions in.
        [params] : {Object} Parameters for the request
        """
        path = "/workspaces/%s/custom_fields" % (workspace)
        return self.client.get_collection(path, params, **options)