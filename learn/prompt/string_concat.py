#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-09 22:17 
@explain : 文件说明
"""
from langchain_core.prompts import PromptTemplate

prompt = (PromptTemplate.from_template("请讲一个关于{subject}的冷笑话") + "，让我开心一下" + "\n使用{language}语言")

print(prompt.invoke({"subject": "程序员", "language": "中文"}).to_string())
