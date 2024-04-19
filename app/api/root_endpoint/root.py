# -*- coding:utf-8 _*_
"""
@Project    : qingyu-api 
@File       : root.py 
@Author     : 晴天 
@CreateTime : 2024-04-19 11:05
"""
from fastapi import APIRouter


root_router = APIRouter()


@root_router.get("/")
def root():
    return {"code": 200, "message": "OK"}
