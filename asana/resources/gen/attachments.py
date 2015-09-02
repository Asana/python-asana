class _Attachments:
    """An _attachment_ object represents any file attached to a task in Asana,
    whether it's an uploaded file or one associated via a third-party service
    such as Dropbox or Google Drive.
    """

    def __init__(self, client=None):
        self.client = client
  
    def find_by_id(self, attachment, params={}, **options): 
        """Returns the full record for a single attachment.

        Parameters
        ----------
        attachment : {Id} Globally unique identifier for the attachment.
        [params] : {Object} Parameters for the request
        """
        path = "/attachments/%s" % (attachment)
        return self.client.get(path, params, **options)
        
    def find_by_task(self, task, params={}, **options): 
        """Returns the compact records for all attachments on the task.

        Parameters
        ----------
        task : {Id} Globally unique identifier for the task.
        [params] : {Object} Parameters for the request
        """
        path = "/tasks/%s/attachments" % (task)
        return self.client.get_collection(path, params, **options)