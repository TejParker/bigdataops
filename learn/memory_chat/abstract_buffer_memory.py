#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-15 23:27 
@explain : 文件说明
"""
from typing import Any

import dotenv
from openai import OpenAI

dotenv.load_dotenv()


class ConversationSummaryBufferMemory:
    """摘要缓冲记忆类"""

    def __init__(self, summary: str = '', chat_histories: list = None, max_tokens: int = 300):
        self.summary = summary
        self.chat_histories = [] if chat_histories is None else chat_histories
        self.max_tokens = max_tokens
        self._clent = OpenAI()  # 生成摘要的客户端

    @classmethod
    def get_num_tokens(cls, query: str) -> int:
        """计算传入的query的token数量"""
        return len(query)

    def save_context(self, human_query: str, ai_content: str) -> None:
        """保存传入的新一次对话消息"""
        self.chat_histories.append({"human": human_query, "ai": ai_content})

        buffer_string = self.get_buffer_string()

        tokens = self.get_num_tokens(buffer_string)

        if tokens > self.max_tokens:
            first_chat = self.chat_histories[0]
            print("新摘要生成中。。。。")
            self.summary = self.summary_text(self.summary,
                                             f"Human: {first_chat.get('human')}\n AI:{first_chat.get('ai')}")
            print("新摘要生成成功：", self.summary)
            del self.chat_histories[0]

    def get_buffer_string(self) -> str:
        """获取历史对话消息的字符串格式"""
        buffer: str = ''
        for chat in self.chat_histories:
            buffer += f"Human:{chat.get('human')}\n AI:{chat.get('ai')}\n\n"

        return buffer.strip()

    def load_memory_variables(self) -> dict[str, Any]:
        """加载记忆变量为一个字典，便于格式化到prompt中"""
        buffer_str = self.get_buffer_string()
        return {
            "chat_history": f"摘要:{self.summary}\n\n 历史信息:{buffer_str}"
        }

    def summary_text(self, origin_summary: str, new_line: str) -> str:
        """用于将旧的摘要和传入的对话生成新摘要"""
        prompt = f"""你是一个强大的聊天机器人，请根据用户提供的谈话内容，总结摘要，并将其添加到先前提供的摘要中，返回一个新的摘要，除了新摘要其他任何数据都不要生成，如果用户的对话信息里有一些关键的信息，比方说姓名、爱好、性别、重要事件等等，这些全部都要包括在生成的摘要中，摘要尽可能要还原用户的对话记录。

        请不要将<example>标签里的数据当成实际的数据，这里的数据只是一个示例数据，告诉你该如何生成新摘要。

        <example>
        当前摘要：人类会问人工智能对人工智能的看法，人工智能认为人工智能是一股向善的力量。

        新的对话：
        Human：为什么你认为人工智能是一股向善的力量？
        AI：因为人工智能会帮助人类充分发挥潜力。

        新摘要：人类会问人工智能对人工智能的看法，人工智能认为人工智能是一股向善的力量，因为它将帮助人类充分发挥潜力。
        </example>

        =====================以下的数据是实际需要处理的数据=====================

        当前摘要：{origin_summary}

        新的对话：
        {new_line}

        请帮用户将上面的信息生成新摘要。"""
        completion = self._clent.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        return completion.choices[0].message.content
    # 1. max_tokens用于判断是否要生成新的摘要
    # 2、 summary用于存储摘要的信息
    # 3、 chat_histories 用于存储历史对话
    # 4. get_num_tokens 用于计算传入文本的token数
    # 5. save_context 用于存储新的交流对话
    # 6. get_buffer_string 用于将历史对话转换成字符串
    # 7. load_memory_variables 用于加载记忆变量信息
    # 8. summary_text 用于将旧的摘要和传入的对话生成新摘要


clien = OpenAI()

memory = ConversationSummaryBufferMemory("", [], 300)

while True:
    # 获取人类输入
    query = input("Human: ")

    if query == 'q':
        break

    memory_variables = memory.load_memory_variables()
    answer_prompt = (
        "你是一个强大的聊天机器人， 请根据对应的上下文和用户提问回答问题。\n\n"
        f"{memory_variables.get('chat_history')}\n\n"
        f"用户提问是：{query}"
    )
    response = clien.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": answer_prompt}
        ],
        stream=True
    )

    print("AI: ", flush=True, end='')
    ai_content = ''
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content is None:
            break
        ai_content += content
        print(content, flush=True, end="")
    print("")
    memory.save_context(query, ai_content)
