# -*- coding:utf-8 _*_
"""
@Project    : qingyu-api 
@File       : exception_handlers.py 
@Author     : 晴天 
@CreateTime : 2024-04-19 11:12
"""
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import Response


async def http_exception_handler(request: Request, exc: HTTPException) -> Response:
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError) -> Response:
    return JSONResponse(
        status_code=400,
        content={"message": "Validation error", "details": exc.errors()}
    )


async def starlette_exception_handler(request: Request, exc: StarletteHTTPException) -> Response:
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


async def generic_exception_handler(request: Request, exc: Exception) -> Response:
    return JSONResponse(
        status_code=500,
        content={"message": "An internal server error occurred."}
    )


def register_exception_handlers(app) -> None:
    """ 注册全局异常处理 """
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(StarletteHTTPException, starlette_exception_handler)
    app.add_exception_handler(Exception, generic_exception_handler)
