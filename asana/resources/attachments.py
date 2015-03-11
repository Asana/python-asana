
from .gen.attachments import _Attachments

class Attachments(_Attachments):
    """Attachments resource"""

    def create_on_task(self, task_id, file_content, file_name, file_content_type=None, **options):
        """Upload an attachment for a task. Accepts a file object or string, file name, and optional file Content-Type"""
        path = '/tasks/%d/attachments' % (task_id)
        return self.client.request('post', path, files=[('file', (file_name, file_content, file_content_type))], **options)
