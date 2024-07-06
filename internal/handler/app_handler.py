#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-06 13:43 
@explain : 文件说明
"""
import os

from flask import request
from openai import OpenAI

from internal.schema.app_schema import CompletionReq
from pkg.response import success_json, validate_error_json


class AppHandler:
    """
    应用控制器
    """

    @staticmethod
    def ping():
        return {"msg": "you are here"}

    def chat_completion(self):
        """聊天接口"""
        # 1. 提取从接口中获取的输入,POST
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)
        query = request.json.get("query")

        # 2. 构建OpenAI客户端， 并发起请求
        client = OpenAI(base_url=os.getenv("OPENAI_API_BASE"))
        # 3. 得到请求响应，然后将OpenAI的响应传递给前端
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system",
                 "content": "You are a chat bot developed by OpenAI, you can assist use as you can, especially in "
                            "programing"},
                {"role": "user", "content": query}
            ]
        )

        content = completion.choices[0].message.content

        return success_json({"content": content})
