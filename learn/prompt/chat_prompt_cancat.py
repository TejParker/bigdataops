#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-09 22:26 
@explain : 文件说明
"""
from langchain_core.prompts import ChatPromptTemplate

system_chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请根据用户的提问进行回复，我叫:{username}"),
])

human_chat_prompt = ChatPromptTemplate.from_messages([
    ("human", "{query}"),
])

chat_prompt = system_chat_prompt + human_chat_prompt

print(chat_prompt.invoke({
    "username": "云法",
    "query": "你好，你是？"
}))
