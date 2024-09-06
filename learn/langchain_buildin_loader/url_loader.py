#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-08-17 14:39 
@explain : 文件说明
"""
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("http://imooc.com")
documents = loader.load()

print(documents)
print(len(documents))
print(
    documents[0].metadata
)
