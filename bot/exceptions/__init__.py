from aiohttp.client_exceptions import ClientResponseError


class InvalidSessionException(BaseException): ...


class InvalidProtocol(BaseException): ...


class CustomClientResponseError(ClientResponseError):
    def __str__(self) -> str:
        return "{}, message={!r}".format(
            self.status,
            self.message,
        )


class InvalidApiKeyException(BaseException):
    pass


class ExpiredApiKeyException(BaseException):
    pass


class ExpiredTokenException(BaseException):
    pass


class GameSessionNotFoundException(BaseException):
    pass


class ErrorStartGameException(BaseException):
    pass


class MissingApiKeyException(BaseException):
    pass
