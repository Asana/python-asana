
from .gen.portfolio_memberships import _PortfolioMemberships

class PortfolioMemberships(_PortfolioMemberships):
    """Portfolio Memberships resource"""

    def find_all(self, params={}, **options):
        """Returns the compact portfolio membership records for the portfolio. You must
        specify `portfolio`, `portfolio` and `user`, or `workspace` and `user`.

        Parameters
        ----------
        [params] : {Object} Parameters for the request
          - [portfolio] : {Gid} The portfolio for which to fetch memberships.
          - [workspace] : {Gid} The workspace for which to fetch memberships.
          - [user] : {String} The user to filter the memberships to.
        """
        return self.client.get_collection("/portfolio_memberships", params, **options)

    def find_by_portfolio(self, portfolio, params={}, **options):
        """Returns the compact portfolio membership records for the portfolio.

        Parameters
        ----------
        portfolio : {Gid} The portfolio for which to fetch memberships.
        [params] : {Object} Parameters for the request
          - [user] : {String} If present, the user to filter the memberships to.
        """
        path = "/portfolios/%s/portfolio_memberships" % (portfolio)
        return self.client.get_collection(path, params, **options)

    def find_by_id(self, portfolio_membership, params={}, **options):
        """Returns the portfolio membership record.

        Parameters
        ----------
        portfolio_membership : {Gid} Globally unique identifier for the portfolio membership.
        [params] : {Object} Parameters for the request
        """
        path = "/portfolio_memberships/%s" % (portfolio_membership)
        return self.client.get(path, params, **options)

