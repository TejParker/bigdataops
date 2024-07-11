#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-11 22:08 
@explain : 文件说明
"""
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
content = parser.parse("hello langchain")

print(content)
