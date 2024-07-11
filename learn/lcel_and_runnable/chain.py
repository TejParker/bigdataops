#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-11 23:18 
@explain : 文件说明
"""
from typing import Any

import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_template("{query}")

llm = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()

list = [prompt, llm, parser]


class Chain:
    steps: list = []

    def __init__(self, steps: list):
        self.steps = steps

    def invoke(self, input: Any) -> Any:
        for step in self.steps:
            input = step.invoke(input)
            print("Step:", step)
            print("Output:", input)
            print("====================")

        return input


chain = Chain(list)

print(chain.invoke({"query": "你好，你用的是什么模型？"}))
