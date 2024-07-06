#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-06 13:43 
@explain : 文件说明
"""


class AppHandler:
    """
    应用控制器
    """

    @staticmethod
    def ping():
        return {"msg": "you are here"}
