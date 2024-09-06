#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-08-17 13:57 
@explain : 文件说明
"""

from langchain_community.document_loaders import UnstructuredMarkdownLoader

loader = UnstructuredMarkdownLoader("./项目API资料.md")

documents = loader.load()

print(documents)
print(len(documents))
print(documents[0].metadata)
