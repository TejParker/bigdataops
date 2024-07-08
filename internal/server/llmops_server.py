#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-06 14:03 
@explain : 文件说明
"""
import os

from flask import Flask

from config import Config
from internal.exception import CustomException
from internal.model import App
from internal.router import Router
from pkg.response import json, Response, HttpCode
from pkg.sqlalchemy import SQLAlchemy


class LLMOpsApp(Flask):
    """LLMOps的Http服务引擎， 后续还会添加 BigdataOps 的Http服务引擎"""

    def __init__(self, *args, conf: Config, db: SQLAlchemy, router: Router, **kwargs):
        super().__init__(*args, **kwargs)

        # 注册绑定异常错误处理
        self.register_error_handler(Exception, self._register_error_handler)

        self.config.from_object(conf)
        # 初始化flask-SQLAlchemy
        db.init_app(self)
        with self.app_context():
            _ = App()
            db.create_all()
        # 注册应用路由
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {}
            ))

        if self.debug or os.getenv("FLASK_ENV") == "development":
            raise error
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data={}
            ))
