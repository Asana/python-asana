
class AsanaError(Exception):
    def __init__(self, message=None, status=None, value=None):
        super(AsanaError, self).__init__(message)
        self.status = status
        self.value = value

class ForbiddenError(AsanaError):
    def __init__(self, value=None):
        super(ForbiddenError, self).__init__(
            message='Forbidden',
            status=403,
            value=value
        )

class NoAuthorizationError(AsanaError):
    def __init__(self, value=None):
        super(NoAuthorizationError, self).__init__(
            message='No Authorization',
            status=401,
            value=value
        )

class NotFoundError(AsanaError):
    def __init__(self, value=None):
        super(NotFoundError, self).__init__(
            message='Not Found',
            status=404,
            value=value
        )

class RateLimitEnforcedError(AsanaError):
    def __init__(self, value=None):
        super(RateLimitEnforcedError, self).__init__(
            message='Rate Limit Enforced',
            status=429,
            value=value
        )

class ServerError(AsanaError):
    def __init__(self, value=None):
        super(ServerError, self).__init__(
            message='Server Error',
            status=500,
            value=value
        )
