#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-23 23:08 
@explain : 文件说明
"""
import dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

dotenv.load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small")

db = FAISS.from_texts([
    "please introduce attention mechanism form me",
    "what is cross attention?",
    "what is self-attention?"
], embedding, relevance_score_fn=lambda distance: 1.0 / (1.0 + distance))

print(db.similarity_search_with_relevance_scores("what is attention mechanism?"))

# print(db.index.ntotal)
