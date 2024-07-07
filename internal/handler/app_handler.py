#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-06 13:43 
@explain : 文件说明
"""

from flask import request
from openai import OpenAI
from openai.types.chat import ChatCompletion

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from pkg.response import validate_error_json, success_json, fail_message


class AppHandler:
    """
    应用控制器
    """

    # @staticmethod
    def ping(self):
        raise FailException("数据未找到")
        # return {"msg": "you are here"}

    def chat_completion(self):
        """聊天接口"""
        # 1. 提取从接口中获取的输入,POST
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)
        query = request.json.get("query")
        # 2. 构建OpenAI客户端， 并发起请求
        client = OpenAI()
        # 3. 得到请求响应，然后将OpenAI的响应传递给前端
        completion: ChatCompletion = None
        try:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo-16k",
                messages=[
                    {"role": "system",
                     "content": "You are a chat bot developed by OpenAI, you can assist use as you can, especially in "
                                "programing"},
                    {"role": "user", "content": query}
                ]
            )
        except Exception as e:
            return fail_message("Api key error or reach limit")
        finally:
            client.close()

        content = ""
        if completion:
            content = completion.choices[0].message.content

        # resp = Response(code=HttpCode.SUCCESS, message="", data={"content": content})
        #
        # return jsonify(resp), 200
        # 对上面的返回进行封装
        return success_json({"content": content})
