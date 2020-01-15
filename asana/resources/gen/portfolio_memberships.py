
class _PortfolioMemberships:

    def __init__(self, client=None):
        self.client = client

    def get_portfolio_membership(self, portfolio_membership_path_gid, params={}, **options):
        """Get a portfolio membership
        :param str portfolio_membership_path_gid: (required)
        [params] : {Object} Parameters for the request
        :return: PortfolioMembershipResponse
        """
        path = "/portfolio_memberships/{portfolio_membership_gid}".replace("portfolio_membership_path_gid", portfolio_membership_path_gid)
        return self.client.get(path, params, **options)


    def get_portfolio_memberships(self, params={}, **options):
        """Get multiple portfolio memberships
        [params] : {Object} Parameters for the request
        :return: list[PortfolioMembershipCompact]
        """
        path = "/portfolio_memberships"
        return self.client.get(path, params, **options)


    def get_portfolio_memberships_for_portfolio(self, portfolio_gid, params={}, **options):
        """Get memberships from a portfolio
        :param str portfolio_gid: Globally unique identifier for the portfolio. (required)
        [params] : {Object} Parameters for the request
        :return: list[PortfolioMembershipCompact]
        """
        path = "/portfolios/{portfolio_gid}/portfolio_memberships".replace("portfolio_gid", portfolio_gid)
        return self.client.get(path, params, **options)

