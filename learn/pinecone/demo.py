#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-24 0:10 
@explain : 文件说明
"""
import dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

dotenv.load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small")

db = PineconeVectorStore(index_name="production-bot", embedding=embedding, namespace="dataset")

texts = [
    "please introduce attention mechanism form me",
    "what is cross attention?",
    "what is self-attention?"
]

db.add_texts(texts, namespace="dataset")
