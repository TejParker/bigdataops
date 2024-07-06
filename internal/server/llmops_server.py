#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-06 14:03 
@explain : 文件说明
"""
from flask import Flask

from internal.router import Router


class LLMOpsApp(Flask):
    """LLMOps的Http服务引擎， 后续还会添加 BigdataOps 的Http服务引擎"""

    def __init__(self, *args, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_router(self)
