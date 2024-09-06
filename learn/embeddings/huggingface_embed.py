#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-23 22:07 
@explain : 文件说明
"""
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L12-v2",
    cache_folder="./embeddings/"
)

embed_vector = embedding.embed_query("hello,I am simon, I like reading, programing and football")

print(embed_vector)
print(len(embed_vector))
