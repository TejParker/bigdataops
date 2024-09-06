#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-08-17 15:01 
@explain : 文件说明
"""
from langchain_community.document_loaders import UnstructuredFileLoader

loader = UnstructuredFileLoader("./章节介绍.pptx")
documents = loader.load()

print(documents)
print(len(documents))
print(
    documents[0].metadata
)
