from asana.rest import ApiException

class PageIterator(object):
    def __init__(self, api_client, api_request_data,  **kwargs):
        self.__api_client = api_client
        self.api_request_data = api_request_data
        self.next_page = False
        self.item_limit = float('inf') if kwargs.get('item_limit', None) == None else kwargs.get('item_limit')
        self.count = 0

    def __iter__(self):
        """Iterator interface, self is an iterator"""
        return self

    def __next__(self):
        limit = self.api_request_data["query_params"].get("limit", None)
        if limit:
            self.api_request_data["query_params"]["limit"] = min(limit, self.item_limit - self.count)

        if self.next_page is None or self.api_request_data["query_params"].get("limit", None) == 0:
            raise StopIteration

        try:
            result = self.call_api()
        except ApiException as e:
            raise e

        # If the response has a next_page add the offset to the api_request_data for the next request
        self.next_page = result.get('next_page', None)
        if (self.next_page):
            self.api_request_data["query_params"]["offset"] = self.next_page["offset"]
        data = result['data']
        if data != None:
            self.count += len(data)
        return data

    def next(self):
        """Alias for __next__"""
        return self.__next__()

    def items(self):
        """Returns an iterator for each item in each page"""
        for page in self:
            for item in page:
                yield item

    def call_api(self):
        return self.__api_client.call_api(
            self.api_request_data["resource_path"],
            self.api_request_data["method"],
            self.api_request_data["path_params"],
            self.api_request_data["query_params"],
            self.api_request_data["header_params"],
            self.api_request_data["body"],
            self.api_request_data["post_params"],
            self.api_request_data["files"],
            self.api_request_data["response_type"],
            self.api_request_data["auth_settings"],
            self.api_request_data["async_req"],
            self.api_request_data["_return_http_data_only"],
            self.api_request_data["collection_formats"],
            self.api_request_data["_preload_content"],
            self.api_request_data["_request_timeout"]
        )
