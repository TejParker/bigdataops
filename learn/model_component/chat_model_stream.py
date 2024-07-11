#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-10 0:04 
@explain : 文件说明
"""
from datetime import datetime

import dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# 1、编排prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}")
]).partial(now=datetime.now())
print(prompt)

llm = ChatOpenAI(model="gpt-3.5-turbo-16k")

response = llm.stream(prompt.invoke({"query": "请简单介绍一下LLM和LLMOps"}))

for chunk in response:
    print(chunk.content, flush=True, end="")
