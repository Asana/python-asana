
class _CustomFieldSettings:

    def __init__(self, client=None):
        self.client = client

    def add_custom_field_setting_for_portfolio(self, portfolio_gid, params={}, **options):
        """Add a custom field to a portfolio
        :param str portfolio_gid: Globally unique identifier for the portfolio. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/portfolios/{portfolio_gid}/addCustomFieldSetting".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)


    def get_custom_field_settings_for_portfolio(self, portfolio_gid, params={}, **options):
        """Get a portfolio's custom fields
        :param str portfolio_gid: Globally unique identifier for the portfolio. (required)
        [params] : {Object} Parameters for the request
        :return: list[CustomFieldSettingResponse]
        """
        path = "/portfolios/{portfolio_gid}/custom_field_settings".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)


    def get_custom_field_settings_for_project(self, project_gid, params={}, **options):
        """Get a project's custom fields
        :param str project_gid: Globally unique identifier for the project. (required)
        [params] : {Object} Parameters for the request
        :return: list[CustomFieldSettingResponse]
        """
        path = "/projects/{project_gid}/custom_field_settings".replace("{project_gid}", project_gid)
        return self.client.get(path, params, **options)


    def remove_custom_field_setting_for_portfolio(self, portfolio_gid, params={}, **options):
        """Remove a custom field from a portfolio
        :param str portfolio_gid: Globally unique identifier for the portfolio. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/portfolios/{portfolio_gid}/removeCustomFieldSetting".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)

