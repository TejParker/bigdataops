#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-09 22:31 
@explain : 文件说明
"""
from langchain_core.prompts import PromptTemplate, PipelinePromptTemplate

full_template = PromptTemplate.from_template("""
{instruction}

{example}

{start}

""")

instruct_prompt = PromptTemplate.from_template("你正在模拟{person}")
example_prompt = PromptTemplate.from_template("""下面是一个交互例子：

Q: {example_q}
A: {example_a}""")

start_prompt = PromptTemplate.from_template("""现在，你是一个真实的人，请回答用户的问题:

Q: {input}
A:""")

pipeline_prompt = [
    ("instruction", instruct_prompt),
    ("example", example_prompt),
    ("start", start_prompt)
]
pipeline_prompt = PipelinePromptTemplate(
    final_prompt=full_template,
    pipeline_prompts=pipeline_prompt
)

print(pipeline_prompt.invoke({
    "person": "will",
    "example_q": "你最喜欢的产品是什么？",
    "example_a": "dMachine",
    "input": "你最喜欢的功能是？"
}).to_string())
