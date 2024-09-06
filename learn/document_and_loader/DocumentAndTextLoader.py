#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-08-17 13:21 
@explain : 文件说明
"""
from langchain_community.document_loaders import TextLoader

loader = TextLoader("./电商产品数据.txt", encoding='utf-8')
documents = loader.load()

print(documents)
print(len(documents))
print(documents[0].metadata)
