
from .gen.webhooks import _Webhooks

class Webhooks(_Webhooks):
    """Webhooks resource"""
    def create(self, params={}, **options):
        """Establishing a webhook is a two-part process. First, a simple HTTP POST
        similar to any other resource creation. Since you could have multiple
        webhooks we recommend specifying a unique local id for each target.

        Next comes the confirmation handshake. When a webhook is created, we will
        send a test POST to the `target` with an `X-Hook-Secret` header as
        described in the
        [Resthooks Security documentation](http://resthooks.org/docs/security/).
        The target must respond with a `200 OK` and a matching `X-Hook-Secret`
        header to confirm that this webhook subscription is indeed expected.

        If you do not acknowledge the webhook's confirmation handshake it will
        fail to setup, and you will receive an error in response to your attempt
        to create it. This means you need to be able to receive and complete the
        webhook *while* the POST request is in-flight.

        Parameters
        ----------
        resource : {Id} A resource ID to subscribe to. The resource can be a task or project.
        target : {String} The URL to receive the HTTP POST.
        [data] : {Object} Data for the request
        """
        return self.client.post("/webhooks", params, **options)

    def get_all(self, params={}, **options):
        """Returns the compact representation of all webhooks your app has
        registered for the authenticated user in the given workspace.

        Parameters
        ----------
        workspace : {Id} The workspace to query for webhooks in.
        [params] : {Object} Parameters for the request
          - [resource] : {Id} Only return webhooks for the given resource.
        """
        return self.client.get_collection("/webhooks", params, **options)

    def get_by_id(self, webhook, params={}, **options):
        """Returns the full record for the given webhook.

        Parameters
        ----------
        webhook : {Id} The webhook to get.
        [params] : {Object} Parameters for the request
        """
        path = "/webhooks/%s" % (webhook)
        return self.client.get(path, params, **options)

    def delete_by_id(self, webhook, params={}, **options):
        """This method permanently removes a webhook. Note that it may be possible
        to receive a request that was already in flight after deleting the
        webhook, but no further requests will be issued.

        Parameters
        ----------
        webhook : {Id} The webhook to delete.
        """
        path = "/webhooks/%s" % (webhook)
        return self.client.delete(path, params, **options)
