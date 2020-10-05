
from .gen.attachments import _Attachments

class Attachments(_Attachments):
    """Attachments resource"""

    def create_attachment_for_task(self, task_id, file_content, file_name, file_content_type=None, **options):
        """Upload an attachment for a task. Accepts a file object or string, file name, and optional file Content-Type"""
        path = '/tasks/%s/attachments' % (task_id)
        return self.client.request('post', path, files=[('file', (file_name, file_content, file_content_type))], **options)

    def create_on_task(self, task_id, file_content, file_name, file_content_type=None, **options):
        path = '/tasks/%s/attachments' % (task_id)
        return self.client.request('post', path, files=[('file', (file_name, file_content, file_content_type))], **options)

    def find_by_id(self, attachment, params={}, **options):
        """Returns the full record for a single attachment.

        Parameters
        ----------
        attachment : {Gid} Globally unique identifier for the attachment.
        [params] : {Object} Parameters for the request
        """
        path = "/attachments/%s" % (attachment)
        return self.client.get(path, params, **options)

    def find_by_task(self, task, params={}, **options):
        """Returns the compact records for all attachments on the task.

        Parameters
        ----------
        task : {Gid} Globally unique identifier for the task.
        [params] : {Object} Parameters for the request
        """
        path = "/tasks/%s/attachments" % (task)
        return self.client.get_collection(path, params, **options)
