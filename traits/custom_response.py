from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


def assert_response(status_code: int, content: any):
    return JSONResponse(status_code=status_code, content=jsonable_encoder(content))


def error_response(status_code: int, content: any):
    return JSONResponse(status_code=status_code, content=jsonable_encoder(content))
