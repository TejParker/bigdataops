#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-06 14:09 
@explain : 文件说明
"""
from injector import Injector

from internal.router import Router
from internal.server.llmops_server import LLMOpsApp

injector = Injector()
app = LLMOpsApp(__name__, router=injector.get(Router))

if __name__ == '__main__':
    app.run(debug=True)
