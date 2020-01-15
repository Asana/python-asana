
class _Portfolios:

    def __init__(self, client=None):
        self.client = client

    def add_item_for_portfolio(self, portfolio_gid, params={}, **options):
        """Add a portfolio item
        :param str portfolio_gid: Globally unique identifier for the portfolio. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/portfolios/{portfolio_gid}/addItem".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)


    def add_members_for_portfolio(self, portfolio_gid, params={}, **options):
        """Add users to a portfolio
        :param str portfolio_gid: Globally unique identifier for the portfolio. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/portfolios/{portfolio_gid}/addMembers".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)


    def create_portfolio(self, params={}, **options):
        """Create a portfolio
        [params] : {Object} Parameters for the request
        :return: PortfolioResponse
        """
        path = "/portfolios"
        return self.client.get(path, params, **options)


    def delete_portfolio(self, portfolio_gid, params={}, **options):
        """Delete a portfolio
        :param str portfolio_gid: Globally unique identifier for the portfolio. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/portfolios/{portfolio_gid}".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)


    def get_items_for_portfolio(self, portfolio_gid, params={}, **options):
        """Get portfolio items
        :param str portfolio_gid: Globally unique identifier for the portfolio. (required)
        [params] : {Object} Parameters for the request
        :return: list[ProjectCompact]
        """
        path = "/portfolios/{portfolio_gid}/items".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)


    def get_portfolio(self, portfolio_gid, params={}, **options):
        """Get a portfolio
        :param str portfolio_gid: Globally unique identifier for the portfolio. (required)
        [params] : {Object} Parameters for the request
        :return: PortfolioResponse
        """
        path = "/portfolios/{portfolio_gid}".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)


    def get_portfolios(self, params={}, **options):
        """Get multiple portfolios
        [params] : {Object} Parameters for the request
        :return: list[PortfolioCompact]
        """
        path = "/portfolios"
        return self.client.get(path, params, **options)


    def remove_item_for_portfolio(self, portfolio_gid, params={}, **options):
        """Remove a portfolio item
        :param str portfolio_gid: Globally unique identifier for the portfolio. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/portfolios/{portfolio_gid}/removeItem".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)


    def remove_members_for_portfolio(self, portfolio_gid, params={}, **options):
        """Remove users from a portfolio
        :param str portfolio_gid: Globally unique identifier for the portfolio. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/portfolios/{portfolio_gid}/removeMembers".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)


    def update_portfolio(self, portfolio_gid, params={}, **options):
        """Update a portfolio
        :param str portfolio_gid: Globally unique identifier for the portfolio. (required)
        [params] : {Object} Parameters for the request
        :return: PortfolioResponse
        """
        path = "/portfolios/{portfolio_gid}".replace("{portfolio_gid}", portfolio_gid)
        return self.client.get(path, params, **options)

