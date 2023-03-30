from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from starlette import status
from starlette.middleware.base import BaseHTTPMiddleware

from traits.custom_response import error_response


class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return error_response(status.HTTP_500_INTERNAL_SERVER_ERROR, {"message": f"Internal server error ${e}"})
