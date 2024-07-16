#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-16 22:20 
@explain : 文件说明
"""
from langchain_core.chat_history import InMemoryChatMessageHistory

chat_history = InMemoryChatMessageHistory()

chat_history.add_user_message("hi, I am simon. who are you")
chat_history.add_ai_message("hello, I am chatgpt")

print(chat_history)
