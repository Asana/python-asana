class _CustomFieldSettings:
    """Custom fields are attached to a particular project with the Custom
    Field Settings resource. This resource both represents the many-to-many join
    of the Custom Field and Project as well as stores information that is relevant to that
    particular pairing; for instance, the `is_important` property determines
    some possible application-specific handling of that custom field (see below)
    """

    def __init__(self, client=None):
        self.client = client
  
    def find_by_project(self, project, params={}, **options): 
        """Returns a list of all of the custom fields settings on a project, in compact form. Note that, as in all queries to collections which return compact representation, `opt_fields` and `opt_expand` can be used to include more data than is returned in the compact representation. See the getting started guide on [input/output options](/developers/documentation/getting-started/input-output-options) for more information.

        Parameters
        ----------
        project : {Id} The ID of the project for which to list custom field settings
        [params] : {Object} Parameters for the request
        """
        path = "/projects/%s/custom_field_settings" % (project)
        return self.client.get_collection(path, params, **options)