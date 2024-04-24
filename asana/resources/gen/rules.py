# coding=utf-8
class _Rules:

    def __init__(self, client=None):
        self.client = client

    def trigger_rule(self, rule_trigger_gid, params=None, **options):
        """Trigger a rule
        :param str rule_trigger_gid: (required) The ID of the incoming web request trigger. This value is a path parameter that is automatically generated for the API endpoint.
        :param Object params: Parameters for the request
        :param **options
        :return: Object
        """
        if params is None:
            params = {}
        path = "/rule_triggers/{rule_trigger_gid}/run".replace("{rule_trigger_gid}", rule_trigger_gid)
        return self.client.post(path, params, **options)
