#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-07 23:02 
@explain : 文件说明
"""
from flask_migrate import Migrate
from injector import Module, Binder

from internal.extension.database_extension import db
from internal.extension.migrate_extension import migrate
from pkg.sqlalchemy import SQLAlchemy


class ExtensionModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        binder.bind(Migrate, to=migrate)
