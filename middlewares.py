from types import coroutine
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from models.exceptions import GoustoBaseException


class ErrorHandlerMiddleWare(BaseHTTPMiddleware):
    """
    Basic error handler.

    It catches all GoustoBaseException and formats them into a
    proper HTTP response.

    """
    async def dispatch(
            self, request: Request, call_next: coroutine
    ) -> Response:
        try:
            return await call_next(request)

        except GoustoBaseException as error:
            return JSONResponse(
                content={
                    'error': {
                        'error_id': error.id,
                        'status_code': error.code,
                        'description': error.description,
                    }
                },
                status_code=error.code
            )
