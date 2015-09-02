class _Events:
    """An _event_ is an object representing a change to a resource that was observed
    by an event subscription.
    
    In general, requesting events on a resource is faster and subject to higher
    rate limits than requesting the resource itself. Additionally, change events
    bubble up - listening to events on a project would include when stories are
    added to tasks in the project, even on subtasks.
    
    Establish an initial sync token by making a request with no sync token.
    The response will be a `412` error - the same as if the sync token had
    expired.
    
    Subsequent requests should always provide the sync token from the immediately
    preceding call.
    
    Sync tokens may not be valid if you attempt to go 'backward' in the history
    by requesting previous tokens, though re-requesting the current sync token
    is generally safe, and will always return the same results.
    
    When you receive a `412 Precondition Failed` error, it means that the
    sync token is either invalid or expired. If you are attempting to keep a set
    of data in sync, this signals you may need to re-crawl the data.
    
    Sync tokens always expire after 24 hours, but may expire sooner, depending on
    load on the service.
    """

    def __init__(self, client=None):
        self.client = client