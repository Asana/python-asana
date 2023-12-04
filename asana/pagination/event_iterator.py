import json
from asana.pagination.page_iterator import PageIterator
from asana.rest import ApiException

class EventIterator(PageIterator):
    def __init__(self, api_client, api_request_data, **kwargs):
        super().__init__(api_client, api_request_data, **kwargs)
        self.sync = False
        self.has_more = True

    def __next__(self):
        if not self.has_more:
            raise StopIteration

        result = {}

        try:
            result = self.call_api()
        except ApiException as e:
            if (e.status == 412):
                errors = json.loads(e.body.decode("utf-8"))
                self.sync = errors["sync"]
            else:
                raise e
        
        if (self.sync):
            self.api_request_data["query_params"]["sync"] = self.sync
        else:
            self.sync = result.get('sync', None)
        
        if not result:
            try:
                result = self.call_api()
            except ApiException as e:
                raise e
        
        self.has_more = result.get('has_more', False)
        return result["data"]
