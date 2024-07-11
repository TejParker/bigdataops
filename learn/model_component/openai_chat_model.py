#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-09 23:04 
@explain : 文件说明
"""
import logging
from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
# 获取logger实例


logging.basicConfig(level=logging.DEBUG)

# 1、编排prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}")
]).partial(now=datetime.now())
print(prompt)

llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

ai_message = llm.invoke(prompt.invoke({"query": "现在是几点？请讲一个程序员的冷笑话"}))

print(ai_message)

# llm = ChatOpenAI(
#     model="gpt-4o",
#     temperature=0,
#     max_tokens=None,
#     timeout=None,
#     max_retries=2,
#     # api_key="...",  # if you prefer to pass api key in directly instaed of using env vars
#     # base_url="http://localhost:7890",
#     # organization="...",
#     # other params...
# )
# messages = [
#     (
#         "system",
#         "You are a helpful assistant that translates English to French. Translate the user sentence.",
#     ),
#     ("human", "I love programming."),
# ]
# ai_msg = llm.invoke(messages)
# ai_msg
#
# print(ai_msg.content)
