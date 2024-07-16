#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-16 23:52 
@explain : 文件说明
"""

import dotenv
from langchain_community.chat_message_histories import FileChatMessageHistory
from openai import OpenAI

dotenv.load_dotenv()
client = OpenAI()
chat_history = FileChatMessageHistory("./memory.txt")

while True:
    # 获取人类输入
    query = input("Human: ")

    if query == 'q':
        break
    system_prompt = (
        "you are a Chatbot developed by OpenAI, you can reply message to user based on the context as follow, the context contains the chat history you made with the user.\n\n"
        f"<context>{chat_history}</context>\n\n"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ],
        stream=True
    )

    ai_content = ''
    print("AI: ", flush=True, end="")
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content is None:
            break
        ai_content += content
        print(content, flush=True, end="")

    chat_history.add_user_message(query)
    chat_history.add_ai_message(ai_content)
    print("")
