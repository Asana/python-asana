
class _CustomFieldSettings:
    """Custom fields are applied to a particular project or portfolio with the
    Custom Field Settings resource. This resource both represents the
    many-to-many join of the Custom Field and Project or Portfolio as well as
    stores information that is relevant to that particular pairing; for instance,
    the `is_important` property determines some possible application-specific
    handling of that custom field and parent.
    """

    def __init__(self, client=None):
        self.client = client
  
    def find_by_project(self, project, params={}, **options): 
        """Returns a list of all of the custom fields settings on a project.

        Parameters
        ----------
        project : {Gid} The ID of the project for which to list custom field settings
        [params] : {Object} Parameters for the request
        """
        path = "/projects/%s/custom_field_settings" % (project)
        return self.client.get_collection(path, params, **options)
        
    def find_by_portfolio(self, portfolio, params={}, **options): 
        """Returns a list of all of the custom fields settings on a portfolio.

        Parameters
        ----------
        portfolio : {Gid} The ID of the portfolio for which to list custom field settings
        [params] : {Object} Parameters for the request
        """
        path = "/portfolios/%s/custom_field_settings" % (portfolio)
        return self.client.get_collection(path, params, **options)
        
