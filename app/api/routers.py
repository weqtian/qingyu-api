# -*- coding:utf-8 _*_
"""
@Project    : qingyu-api 
@File       : routers.py
@Author     : 晴天 
@CreateTime : 2024-04-19 10:58
"""
from fastapi import APIRouter, FastAPI


router = APIRouter()


def register_routes(app: FastAPI) -> None:
    """ 注册路由 """
    from app.api.root_endpoint.root import root_router
    app.include_router(root_router, prefix='', tags=['root'])
