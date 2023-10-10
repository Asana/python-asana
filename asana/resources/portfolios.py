
from .gen.portfolios import _Portfolios

class Portfolios(_Portfolios):
    """Portfolios resource"""

    def create(self, params={}, **options):
        """Creates a new portfolio in the given workspace with the supplied name.

        Note that portfolios created in the Asana UI may have some state
        (like the "Priority" custom field) which is automatically added to the
        portfolio when it is created. Portfolios created via our API will **not**
        be created with the same initial state to allow integrations to create
        their own starting state on a portfolio.

        Parameters
        ----------
        [data] : {Object} Data for the request
          - workspace : {Gid} The workspace or organization in which to create the portfolio.
          - name : {String} The name of the newly-created portfolio
          - [color] : {String} An optional color for the portfolio
        """
        return self.client.post("/portfolios", params, **options)

    def find_by_id(self, portfolio, params={}, **options):
        """Returns the complete record for a single portfolio.

        Parameters
        ----------
        portfolio : {Gid} The portfolio to get.
        [params] : {Object} Parameters for the request
        """
        path = "/portfolios/%s" % (portfolio)
        return self.client.get(path, params, **options)

    def update(self, portfolio, params={}, **options):
        """An existing portfolio can be updated by making a PUT request on the
        URL for that portfolio. Only the fields provided in the `data` block will be
        updated; any unspecified fields will remain unchanged.

        Returns the complete updated portfolio record.

        Parameters
        ----------
        portfolio : {Gid} The portfolio to update.
        [data] : {Object} Data for the request
        """
        path = "/portfolios/%s" % (portfolio)
        return self.client.put(path, params, **options)

    def delete(self, portfolio, params={}, **options):
        """An existing portfolio can be deleted by making a DELETE request
        on the URL for that portfolio.

        Returns an empty data record.

        Parameters
        ----------
        portfolio : {Gid} The portfolio to delete.
        """
        path = "/portfolios/%s" % (portfolio)
        return self.client.delete(path, params, **options)

    def find_all(self, params={}, **options):
        """Returns a list of the portfolios in compact representation that are owned
        by the current API user.

        Parameters
        ----------
        [params] : {Object} Parameters for the request
          - workspace : {Gid} The workspace or organization to filter portfolios on.
          - owner : {String} The user who owns the portfolio. Currently, API users can only get a
          list of portfolios that they themselves own.
        """
        return self.client.get_collection("/portfolios", params, **options)

    def get_items(self, portfolio, params={}, **options):
        """Get a list of the items in compact form in a portfolio.

        Parameters
        ----------
        portfolio : {Gid} The portfolio from which to get the list of items.
        [params] : {Object} Parameters for the request
        """
        path = "/portfolios/%s/items" % (portfolio)
        return self.client.get_collection(path, params, **options)

    def add_item(self, portfolio, params={}, **options):
        """Add an item to a portfolio.

        Returns an empty data block.

        Parameters
        ----------
        portfolio : {Gid} The portfolio to which to add an item.
        [data] : {Object} Data for the request
          - item : {Gid} The item to add to the portfolio.
          - [insert_before] : {Gid} An id of an item in this portfolio. The new item will be added before the one specified here.
          `insert_before` and `insert_after` parameters cannot both be specified.
          - [insert_after] : {Gid} An id of an item in this portfolio. The new item will be added after the one specified here.
          `insert_before` and `insert_after` parameters cannot both be specified.
        """
        path = "/portfolios/%s/addItem" % (portfolio)
        return self.client.post(path, params, **options)

    def remove_item(self, portfolio, params={}, **options):
        """Remove an item to a portfolio.

        Returns an empty data block.

        Parameters
        ----------
        portfolio : {Gid} The portfolio from which to remove the item.
        [data] : {Object} Data for the request
          - item : {Gid} The item to remove from the portfolio.
        """
        path = "/portfolios/%s/removeItem" % (portfolio)
        return self.client.post(path, params, **options)

    def add_members(self, portfolio, params={}, **options):
        """Adds the specified list of users as members of the portfolio. Returns the updated portfolio record.

        Parameters
        ----------
        portfolio : {Gid} The portfolio to add members to.
        [data] : {Object} Data for the request
          - members : {Array} An array of user ids.
        """
        path = "/portfolios/%s/addMembers" % (portfolio)
        return self.client.post(path, params, **options)

    def remove_members(self, portfolio, params={}, **options):
        """Removes the specified list of members from the portfolio. Returns the updated portfolio record.

        Parameters
        ----------
        portfolio : {Gid} The portfolio to remove members from.
        [data] : {Object} Data for the request
          - members : {Array} An array of user ids.
        """
        path = "/portfolios/%s/removeMembers" % (portfolio)
        return self.client.post(path, params, **options)

    def custom_field_settings(self, portfolio, params={}, **options):
        """Get the custom field settings on a portfolio.

        Parameters
        ----------
        portfolio : {Gid} The portfolio from which to get the custom field settings.
        [params] : {Object} Parameters for the request
        """
        path = "/portfolios/%s/custom_field_settings" % (portfolio)
        return self.client.get_collection(path, params, **options)

    def add_custom_field_setting(self, portfolio, params={}, **options):
        """Create a new custom field setting on the portfolio. Returns the full
        record for the new custom field setting.

        Parameters
        ----------
        portfolio : {Gid} The portfolio onto which to add the custom field.
        [data] : {Object} Data for the request
          - custom_field : {Gid} The id of the custom field to add to the portfolio.
          - [is_important] : {Boolean} Whether this field should be considered important to this portfolio (for instance, to display in the list view of items in the portfolio).
          - [insert_before] : {Gid} An id of a custom field setting on this portfolio. The new custom field setting will be added before this one.
          `insert_before` and `insert_after` parameters cannot both be specified.
          - [insert_after] : {Gid} An id of a custom field setting on this portfolio. The new custom field setting will be added after this one.
          `insert_before` and `insert_after` parameters cannot both be specified.
        """
        path = "/portfolios/%s/addCustomFieldSetting" % (portfolio)
        return self.client.post(path, params, **options)

    def remove_custom_field_setting(self, portfolio, params={}, **options):
        """Remove a custom field setting on the portfolio. Returns an empty data
        block.

        Parameters
        ----------
        portfolio : {Gid} The portfolio from which to remove the custom field.
        [data] : {Object} Data for the request
          - custom_field : {Gid} The id of the custom field to remove from this portfolio.
        """
        path = "/portfolios/%s/removeCustomFieldSetting" % (portfolio)
        return self.client.post(path, params, **options)
