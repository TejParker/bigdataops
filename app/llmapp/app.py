#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-06 14:09 
@explain : 文件说明
"""

import dotenv
from injector import Injector

from config import Config
from internal.router import Router
from internal.server.llmops_server import LLMOpsApp
from pkg.sqlalchemy import SQLAlchemy
from .module import ExtensionModule

# 将.env加载到环境变量中
dotenv.load_dotenv()

conf = Config()

injector = Injector([ExtensionModule])
app = LLMOpsApp(__name__, conf=conf, db=injector.get(SQLAlchemy), router=injector.get(Router))

if __name__ == '__main__':
    app.run(debug=True)
