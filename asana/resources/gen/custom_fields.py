
class _CustomFields:

    def __init__(self, client=None):
        self.client = client

    def create_custom_field(self, params={}, **options):
        """Create a custom field
        [params] : {Object} Parameters for the request
        :return: CustomFieldResponse
        """
        path = "/custom_fields"
        return self.client.get(path, params, **options)


    def create_enum_option_for_custom_field(self, custom_field_gid, params={}, **options):
        """Create an enum option
        :param str custom_field_gid: Globally unique identifier for the custom field. (required)
        [params] : {Object} Parameters for the request
        :return: EnumOptionCompact
        """
        path = "/custom_fields/{custom_field_gid}/enum_options".replace("{custom_field_gid}", custom_field_gid)
        return self.client.get(path, params, **options)


    def delete_custom_field(self, custom_field_gid, params={}, **options):
        """Delete a custom field
        :param str custom_field_gid: Globally unique identifier for the custom field. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/custom_fields/{custom_field_gid}".replace("{custom_field_gid}", custom_field_gid)
        return self.client.get(path, params, **options)


    def get_custom_field(self, custom_field_gid, params={}, **options):
        """Get a custom field
        :param str custom_field_gid: Globally unique identifier for the custom field. (required)
        [params] : {Object} Parameters for the request
        :return: CustomFieldResponse
        """
        path = "/custom_fields/{custom_field_gid}".replace("{custom_field_gid}", custom_field_gid)
        return self.client.get(path, params, **options)


    def get_custom_fields_for_workspace(self, workspace_gid, params={}, **options):
        """Get a workspace's custom fields
        :param str workspace_gid: Globally unique identifier for the workspace or organization. (required)
        [params] : {Object} Parameters for the request
        :return: list[EnumOptionCompact]
        """
        path = "/workspaces/{workspace_gid}/custom_fields".replace("{workspace_gid}", workspace_gid)
        return self.client.get(path, params, **options)


    def insert_enum_option_for_custom_field(self, custom_field_gid, params={}, **options):
        """Reorder a custom field's enum
        :param str custom_field_gid: Globally unique identifier for the custom field. (required)
        [params] : {Object} Parameters for the request
        :return: EnumOptionCompact
        """
        path = "/custom_fields/{custom_field_gid}/enum_options/insert".replace("{custom_field_gid}", custom_field_gid)
        return self.client.get(path, params, **options)


    def update_custom_field(self, custom_field_gid, params={}, **options):
        """Update a custom field
        :param str custom_field_gid: Globally unique identifier for the custom field. (required)
        [params] : {Object} Parameters for the request
        :return: CustomFieldResponse
        """
        path = "/custom_fields/{custom_field_gid}".replace("{custom_field_gid}", custom_field_gid)
        return self.client.get(path, params, **options)


    def update_enum_option(self, enum_option_gid, params={}, **options):
        """Update an enum option
        :param str enum_option_gid: Globally unique identifier for the enum option. (required)
        [params] : {Object} Parameters for the request
        :return: EnumOptionCompact
        """
        path = "/enum_options/{enum_option_gid}".replace("{enum_option_gid}", enum_option_gid)
        return self.client.get(path, params, **options)

