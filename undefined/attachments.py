
class _Attachments:
    """An _attachment_ object represents any file attached to a task in Asana,
    whether it's an uploaded file or one associated via a third-party service
    such as Dropbox or Google Drive."""

    def __init__(self, client=None):
        self.client = client
  
    def find_by_id(self, attachment, params={}, **options): 
        """Returns the full record for a single attachment."""
        
        path = "/attachments/%d" % (attachment)
        return self.client.get(path, params, **options)
        
  
    def find_by_task(self, task, params={}, **options): 
        """Returns the compact records for all attachments on the task."""
        
        path = "/tasks/%d/attachments" % (task)
        return self.client.get_collection(path, params, **options)
        
  
