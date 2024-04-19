# -*- coding:utf-8 _*_
"""
@Project    : qingyu-api 
@File       : main.py 
@Author     : 晴天 
@CreateTime : 2024-04-19 10:12
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True)
