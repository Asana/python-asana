# coding=utf-8
class _Portfolios:

    def __init__(self, client=None):
        self.client = client

    def add_custom_field_setting_for_portfolio(self, portfolio_gid, params=None, **options):
        """Add a custom field to a portfolio
        :param str portfolio_gid: (required) Globally unique identifier for the portfolio.
        :param Object params: Parameters for the request
        :param **options
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/portfolios/{portfolio_gid}/addCustomFieldSetting".replace("{portfolio_gid}", portfolio_gid)
        return self.client.post(path, params, **options)

    def add_item_for_portfolio(self, portfolio_gid, params=None, **options):
        """Add a portfolio item
        :param str portfolio_gid: (required) Globally unique identifier for the portfolio.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/portfolios/{portfolio_gid}/addItem".replace("{portfolio_gid}", portfolio_gid)
        return self.client.post(path, params, **options)

    def add_members_for_portfolio(self, portfolio_gid, params=None, **options):
        """Add users to a portfolio
        :param str portfolio_gid: (required) Globally unique identifier for the portfolio.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/portfolios/{portfolio_gid}/addMembers".replace("{portfolio_gid}", portfolio_gid)
        return self.client.post(path, params, **options)

    def create_portfolio(self, params=None, **options):
        """Create a portfolio
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/portfolios"
        return self.client.post(path, params, **options)

    def delete_portfolio(self, portfolio_gid, params=None, **options):
        """Delete a portfolio
        :param str portfolio_gid: (required) Globally unique identifier for the portfolio.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/portfolios/{portfolio_gid}".replace("{portfolio_gid}", portfolio_gid)
        return self.client.delete(path, params, **options)

    def get_items_for_portfolio(self, portfolio_gid, params=None, **options):
        """Get portfolio items
        :param str portfolio_gid: (required) Globally unique identifier for the portfolio.
        :param Object params: Parameters for the request
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/portfolios/{portfolio_gid}/items".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get_collection(path, params, **options)

    def get_portfolio(self, portfolio_gid, params=None, **options):
        """Get a portfolio
        :param str portfolio_gid: (required) Globally unique identifier for the portfolio.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/portfolios/{portfolio_gid}".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)

    def get_portfolios(self, params=None, **options):
        """Get multiple portfolios
        :param Object params: Parameters for the request
            - workspace {str}:  (required) The workspace or organization to filter portfolios on.
            - owner {str}:  (required) The user who owns the portfolio. Currently, API users can only get a list of portfolios that they themselves own.
        :param **options
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/portfolios"
        return self.client.get_collection(path, params, **options)

    def remove_custom_field_setting_for_portfolio(self, portfolio_gid, params=None, **options):
        """Remove a custom field from a portfolio
        :param str portfolio_gid: (required) Globally unique identifier for the portfolio.
        :param Object params: Parameters for the request
        :param **options
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/portfolios/{portfolio_gid}/removeCustomFieldSetting".replace("{portfolio_gid}", portfolio_gid)
        return self.client.post(path, params, **options)

    def remove_item_for_portfolio(self, portfolio_gid, params=None, **options):
        """Remove a portfolio item
        :param str portfolio_gid: (required) Globally unique identifier for the portfolio.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/portfolios/{portfolio_gid}/removeItem".replace("{portfolio_gid}", portfolio_gid)
        return self.client.post(path, params, **options)

    def remove_members_for_portfolio(self, portfolio_gid, params=None, **options):
        """Remove users from a portfolio
        :param str portfolio_gid: (required) Globally unique identifier for the portfolio.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/portfolios/{portfolio_gid}/removeMembers".replace("{portfolio_gid}", portfolio_gid)
        return self.client.post(path, params, **options)

    def update_portfolio(self, portfolio_gid, params=None, **options):
        """Update a portfolio
        :param str portfolio_gid: (required) Globally unique identifier for the portfolio.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/portfolios/{portfolio_gid}".replace("{portfolio_gid}", portfolio_gid)
        return self.client.put(path, params, **options)
