#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-23 22:26 
@explain : 文件说明
"""
import dotenv
from langchain_community.embeddings import QianfanEmbeddingsEndpoint

dotenv.load_dotenv()

embeddings = QianfanEmbeddingsEndpoint()

embed_vector = embeddings.embed_query("hello,I am simon, I like reading, programing and football")

print(embed_vector)
print(len(embed_vector))
