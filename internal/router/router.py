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
        bp.add_url_rule("/app/completion", methods=["POST"], view_func=self.app_handler.chat_completion)
        bp.add_url_rule("/app", methods=["GET"], view_func=self.app_handler.create_app)
        bp.add_url_rule("/app/<uuid:id>", methods=["GET"], view_func=self.app_handler.get_app)
        bp.add_url_rule("/app/<uuid:id>", methods=["POST"], view_func=self.app_handler.update_app)
        bp.add_url_rule("/app/<uuid:id>/delete", methods=["POST"], view_func=self.app_handler.delete_app)

        # 3. 在应用上注册蓝图
        app.register_blueprint(bp)
