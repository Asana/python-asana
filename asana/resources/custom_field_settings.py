
from .gen.custom_field_settings import _CustomFieldSettings

class CustomFieldSettings(_CustomFieldSettings):
    """Custom Field Settings resource"""
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
