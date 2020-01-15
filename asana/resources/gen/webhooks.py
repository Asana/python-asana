
class _Webhooks:

    def __init__(self, client=None):
        self.client = client

    def create_webhook(self, params={}, **options):
        """Establish a webhook
        [params] : {Object} Parameters for the request
        :return: WebhookResponse
        """
        path = "/webhooks"
        return self.client.get(path, params, **options)


    def delete_webhook(self, webhook_gid, params={}, **options):
        """Delete a webhook
        :param str webhook_gid: Globally unique identifier for the webhook. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/webhooks/{webhook_gid}".replace("{webhook_gid}", webhook_gid)
        return self.client.get(path, params, **options)


    def get_webhook(self, webhook_gid, params={}, **options):
        """Get a webhook
        :param str webhook_gid: Globally unique identifier for the webhook. (required)
        [params] : {Object} Parameters for the request
        :return: WebhookResponse
        """
        path = "/webhooks/{webhook_gid}".replace("{webhook_gid}", webhook_gid)
        return self.client.get(path, params, **options)


    def get_webhooks(self, params={}, **options):
        """Get multiple webhooks
        [params] : {Object} Parameters for the request
        :return: list[WebhookResponse]
        """
        path = "/webhooks"
        return self.client.get(path, params, **options)

