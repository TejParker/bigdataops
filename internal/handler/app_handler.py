#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-06 13:43 
@explain : 文件说明
"""
import uuid
from dataclasses import dataclass
from operator import itemgetter

from injector import inject
from langchain.memory import ConversationBufferWindowMemory
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from internal.service import AppService
from pkg.response import validate_error_json, success_json, success_message


@inject
@dataclass
class AppHandler:
    """
    应用控制器
    """
    app_service: AppService

    def create_app(self):
        """调用服务创建新的App记录"""
        app = self.app_service.creat_app()
        return success_message(f"app创建成功, id为{app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用成功获取，名字是[{app.name}]")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用信息已经修改，修改的名字是:{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，删除的id为{app.id}")

    # @staticmethod
    def ping(self):
        raise FailException("数据未找到")
        # return {"msg": "you are here"}

    def debug(self, app_id: uuid.UUID):
        """聊天调试接口"""
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        # 创建prompt与记忆
        prompt = ChatPromptTemplate.from_messages([
            ("system", "you are a chatbot developed by OpenAI, you can answer any questions user asked"),
            MessagesPlaceholder("history"),
            ("human", "{query}"),
        ])
        memory = ConversationBufferWindowMemory(
            k=3,
            input_key="query",
            output_key="output",
            return_messages=True,
            chat_memory=FileChatMessageHistory("./storage/memory/chat_history.txt")
        )
        # 创建llm
        llm = ChatOpenAI(model='gpt-3.5-turbo')

        chain = RunnablePassthrough.assign(
            history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")
        ) | prompt | llm | StrOutputParser()

        chain_input = {"query": req.query.data}
        content = chain.invoke(chain_input)
        memory.save_context(chain_input, {"output": content})
        # prompt = ChatPromptTemplate.from_template("{query}")
        # llm = ChatOpenAI(model='gpt-3.5-turbo')
        # parser = StrOutputParser()
        #
        # chain = prompt | llm | parser
        #
        # content = chain.invoke({"query": req.query.data})

        return success_json({"content": content})

    def chat_completion(self):
        """聊天接口"""
        # 1. 提取从接口中获取的输入,POST
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        prompt = ChatPromptTemplate.from_template("{query}")
        # 2. 构建OpenAI客户端， 并发起请求
        llm = ChatOpenAI(model="gpt-3.5-turbo")
        parser = StrOutputParser()

        # ai_message = llm.invoke(prompt.invoke({"query": req.query.data}))

        # 解析响应内容
        # content = parser.invoke(ai_message)

        chain = prompt | llm | parser

        content = chain.invoke({"query": req.query.data})
        # 3. 得到请求响应，然后将OpenAI的响应传递给前端

        # resp = Response(code=HttpCode.SUCCESS, message="", data={"content": content})
        #
        # return jsonify(resp), 200
        # 对上面的返回进行封装
        return success_json({"content": content})
