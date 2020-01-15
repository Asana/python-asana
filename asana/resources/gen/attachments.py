
class _Attachments:

    def __init__(self, client=None):
        self.client = client

    def create_attachment_for_task(self, task_gid, params={}, **options):
        """Upload an attachment
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: AttachmentResponse
        """
        path = "/tasks/{task_gid}/attachments".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)


    def delete_attachment(self, attachment_gid, params={}, **options):
        """Delete an attachment
        :param str attachment_gid: Globally unique identifier for the attachment. (required)
        [params] : {Object} Parameters for the request
        :return: EmptyObject
        """
        path = "/attachments/{attachment_gid}".replace("{attachment_gid}", attachment_gid)
        return self.client.get(path, params, **options)


    def get_attachment(self, attachment_gid, params={}, **options):
        """Get an attachment
        :param str attachment_gid: Globally unique identifier for the attachment. (required)
        [params] : {Object} Parameters for the request
        :return: AttachmentResponse
        """
        path = "/attachments/{attachment_gid}".replace("{attachment_gid}", attachment_gid)
        return self.client.get(path, params, **options)


    def get_attachments_for_task(self, task_gid, params={}, **options):
        """Get attachments for a task
        :param str task_gid: The task to operate on. (required)
        [params] : {Object} Parameters for the request
        :return: list[AttachmentCompact]
        """
        path = "/tasks/{task_gid}/attachments".replace("{task_gid}", task_gid)
        return self.client.get(path, params, **options)

