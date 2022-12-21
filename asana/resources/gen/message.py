# coding=utf-8
class _Message:

    def __init__(self, client=None):
        self.client = client

    def get_message(self, message_gid, params=None, **options):
        """Get a message
        :param str message_gid: (required) The message to get.
        :param Object params: Parameters for the request
        :param **options
            - opt_fields {list[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """
        if params is None:
            params = {}
        path = "/messages/{message_gid}".replace("{message_gid}", message_gid)
        return self.client.get(path, params, **options)
