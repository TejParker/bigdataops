#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-09 1:25 
@explain : 文件说明
"""
from datetime import datetime

from langchain_core.messages import AIMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder

prompt = PromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
print(prompt.format(subject="戏剧演员"))

prompt_value = prompt.invoke({"subject": "程序员"})
print(prompt_value.to_string())
print(prompt_value.to_messages())

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请根据用户的提问进行回复，当前的时间为:{now}"),
    MessagesPlaceholder("chat_history"),
    HumanMessagePromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
]).partial(now=datetime.now())
print("----------------------------------")
chat_prompt_value = chat_prompt.invoke({
    # "now": datetime.now(),
    "chat_history": [
        ("human", "我叫云法"),
        AIMessage("你好，我是ChatGPT，有什么可以帮到您？")
    ],
    "subject": "程序员"
})

print(chat_prompt_value)
print(chat_prompt_value.to_string())
