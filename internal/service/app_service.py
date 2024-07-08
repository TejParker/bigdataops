#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-07 23:44 
@explain : 文件说明
"""
import uuid
from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy
from injector import inject

from internal.model import App


@inject
@dataclass
class AppService:
    """App模型服务"""
    db: SQLAlchemy

    def creat_app(self) -> App:
        # 1. 创建app模型的实体类
        app = App(
            name="测试机器人",
            account_id=uuid.uuid4(),
            icon="",
            description="这是一个简单的聊天机器人"
        )
        # 2. 将实体类添加到session会话中
        self.db.session.add(app)
        # 3. 提交session会话
        self.db.session.commit()
        return app

    def get_app(self, id: uuid.UUID) -> App:
        return self.db.session.query(App).get(id)

    def update_app(self, id: uuid.UUID) -> App:
        app = self.get_app(id)
        app.name = "简单对话聊天机器人"
        self.db.session.commit()
        return app

    def delete_app(self, id: uuid.UUID) -> App:
        app = self.get_app(id)
        self.db.session.delete(app)
        self.db.session.commit()
        return app
