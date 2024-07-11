#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-11 23:32 
@explain : 文件说明
"""

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_template("{query}")

llm = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()

chain = prompt | llm | parser

print(chain.invoke({"query": "请讲一个程序员的冷笑话"}))
