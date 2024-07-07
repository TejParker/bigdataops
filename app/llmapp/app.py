#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-06 14:09 
@explain : 文件说明
"""
import os

import dotenv
from injector import Injector

from config import Config
from internal.router import Router
from internal.server.llmops_server import LLMOpsApp

# 将.env加载到环境变量中
dotenv.load_dotenv()

conf = Config()
injector = Injector()
app = LLMOpsApp(__name__, conf=conf, router=injector.get(Router))

if __name__ == '__main__':
    print(os.getenv(
        "OPENAI_API_KEY"
    ))
    app.run(debug=True)
