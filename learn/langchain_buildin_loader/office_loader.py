#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-08-17 14:15 
@explain : 文件说明
"""

from langchain_community.document_loaders import (
    UnstructuredPowerPointLoader
)

# loader = UnstructuredExcelLoader("./员工考勤表.xlsx")
#
# documents = loader.load()
# loader = UnstructuredWordDocumentLoader("./喵喵.docx")
# documents = loader.load()

loader = UnstructuredPowerPointLoader("./章节介绍.pptx")
documents = loader.load()

print(documents)
print(len(documents))
print(
    documents[0].metadata
)
