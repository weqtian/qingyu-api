# -*- coding:utf-8 _*_
"""
@Project    : qingyu-api 
@File       : __init__.py.py 
@Author     : 晴天 
@CreateTime : 2024-04-19 10:29
"""
from fastapi import FastAPI
from app.api.routers import register_routes
from app.exceptions.exception_handlers import register_exception_handlers


def create_app() -> FastAPI:
    app = FastAPI(
        title="Qingyu API",
        description="API for Qingyu",
        version="0.0.1",
    )

    # 注册路由
    register_routes(app)

    # 注册全局异常处理
    register_exception_handlers(app)

    return app
