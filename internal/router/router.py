#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-06 13:46 
@explain : 文件说明
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    """
    路由
    """
    app_handler: AppHandler

    def register_router(self, app: Flask):
        """注册路由"""
        # 1. 创建蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 2. 将url与对应的控制器方法做绑定
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)

        # 3. 在应用上注册蓝图
        app.register_blueprint(bp)
