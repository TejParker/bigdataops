#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-11 22:33 
@explain : 文件说明
"""
import dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI


class Joke(BaseModel):
    joke: str = Field(description="回答用户的冷笑话")

    punchline: str = Field(description="这个冷笑话的笑点")


parser = JsonOutputParser(pydantic_object=Joke)

prompt = ChatPromptTemplate.from_template("请根据用户的提问进行回答。\n{format_instruction}\n{query}").partial(
    format_instruction=parser.get_format_instructions())
dotenv.load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo")

joke = parser.invoke(llm.invoke(prompt.invoke({"query": "请讲一个关于程序员的冷笑话"})))

print(joke)
