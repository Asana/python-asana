
from .gen.custom_fields import _CustomFields

class CustomFields(_CustomFields):
    """Custom Fields resource"""
    def add_enum_option(self, custom_field, params={}, **options):
        self.create_enum_option(custom_field, params, **options)

    def reorder_enum_option(self, custom_field, params={}, **options):
        self.insert_enum_option(custom_field, params, **options)

    def create(self, params={}, **options):
        """Creates a new custom field in a workspace. Every custom field is required to be created in a specific workspace, and this workspace cannot be changed once set.

        A custom field's `name` must be unique within a workspace and not conflict with names of existing task properties such as 'Due Date' or 'Assignee'. A custom field's `type` must be one of  'text', 'enum', or 'number'.

        Returns the full record of the newly created custom field.

        Parameters
        ----------
        [data] : {Object} Data for the request
          - workspace : {Gid} The workspace to create a custom field in.
          - resource_subtype : {String} The type of the custom field. Must be one of the given values.
          - [type] : {String} **Deprecated: New integrations should prefer the `resource_subtype` parameter.**
          - name : {String} The name of the custom field.
          - [description] : {String} The description of the custom field.
          - [precision] : {Integer} The number of decimal places for the numerical values. Required if the custom field is of type 'number'.
          - [enum_options] : {String} The discrete values the custom field can assume. Required if the custom field is of type 'enum'.
        """
        return self.client.post("/custom_fields", params, **options)

    def find_by_id(self, custom_field, params={}, **options):
        """Returns the complete definition of a custom field's metadata.

        Parameters
        ----------
        custom_field : {Gid} Globally unique identifier for the custom field.
        [params] : {Object} Parameters for the request
        """
        path = "/custom_fields/%s" % (custom_field)
        return self.client.get(path, params, **options)

    def find_by_workspace(self, workspace, params={}, **options):
        """Returns a list of the compact representation of all of the custom fields in a workspace.

        Parameters
        ----------
        workspace : {Gid} The workspace or organization to find custom field definitions in.
        [params] : {Object} Parameters for the request
        """
        path = "/workspaces/%s/custom_fields" % (workspace)
        return self.client.get_collection(path, params, **options)

    def update(self, custom_field, params={}, **options):
        """A specific, existing custom field can be updated by making a PUT request on the URL for that custom field. Only the fields provided in the `data` block will be updated; any unspecified fields will remain unchanged

        When using this method, it is best to specify only those fields you wish to change, or else you may overwrite changes made by another user since you last retrieved the custom field.

        An enum custom field's `enum_options` cannot be updated with this endpoint. Instead see "Work With Enum Options" for information on how to update `enum_options`.

        Locked custom fields can only be updated by the user who locked the field.

        Returns the complete updated custom field record.

        Parameters
        ----------
        custom_field : {Gid} Globally unique identifier for the custom field.
        [data] : {Object} Data for the request
        """
        path = "/custom_fields/%s" % (custom_field)
        return self.client.put(path, params, **options)

    def delete(self, custom_field, params={}, **options):
        """A specific, existing custom field can be deleted by making a DELETE request on the URL for that custom field.

        Locked custom fields can only be deleted by the user who locked the field.

        Returns an empty data record.

        Parameters
        ----------
        custom_field : {Gid} Globally unique identifier for the custom field.
        """
        path = "/custom_fields/%s" % (custom_field)
        return self.client.delete(path, params, **options)

    def create_enum_option(self, custom_field, params={}, **options):
        """Creates an enum option and adds it to this custom field's list of enum options. A custom field can have at most 50 enum options (including disabled options). By default new enum options are inserted at the end of a custom field's list.

        Locked custom fields can only have enum options added by the user who locked the field.

        Returns the full record of the newly created enum option.

        Parameters
        ----------
        custom_field : {Gid} Globally unique identifier for the custom field.
        [data] : {Object} Data for the request
          - name : {String} The name of the enum option.
          - [color] : {String} The color of the enum option. Defaults to 'none'.
          - [insert_before] : {Gid} An existing enum option within this custom field before which the new enum option should be inserted. Cannot be provided together with after_enum_option.
          - [insert_after] : {Gid} An existing enum option within this custom field after which the new enum option should be inserted. Cannot be provided together with before_enum_option.
        """
        path = "/custom_fields/%s/enum_options" % (custom_field)
        return self.client.post(path, params, **options)

    def update_enum_option(self, enum_option, params={}, **options):
        """Updates an existing enum option. Enum custom fields require at least one enabled enum option.

        Locked custom fields can only be updated by the user who locked the field.

        Returns the full record of the updated enum option.

        Parameters
        ----------
        enum_option : {Gid} Globally unique identifier for the enum option.
        [data] : {Object} Data for the request
          - name : {String} The name of the enum option.
          - [color] : {String} The color of the enum option. Defaults to 'none'.
          - [enabled] : {Boolean} Whether or not the enum option is a selectable value for the custom field.
        """
        path = "/enum_options/%s" % (enum_option)
        return self.client.put(path, params, **options)

    def insert_enum_option(self, custom_field, params={}, **options):
        """Moves a particular enum option to be either before or after another specified enum option in the custom field.

        Locked custom fields can only be reordered by the user who locked the field.

        Parameters
        ----------
        custom_field : {Gid} Globally unique identifier for the custom field.
        [data] : {Object} Data for the request
          - enum_option : {Gid} The ID of the enum option to relocate.
          - name : {String} The name of the enum option.
          - [color] : {String} The color of the enum option. Defaults to 'none'.
          - [before_enum_option] : {Gid} An existing enum option within this custom field before which the new enum option should be inserted. Cannot be provided together with after_enum_option.
          - [after_enum_option] : {Gid} An existing enum option within this custom field after which the new enum option should be inserted. Cannot be provided together with before_enum_option.
        """
        path = "/custom_fields/%s/enum_options/insert" % (custom_field)
        return self.client.post(path, params, **options)
