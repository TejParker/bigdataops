#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-10 0:14 
@explain : 文件说明
"""
import logging

import dotenv
import openai

dotenv.load_dotenv()

# 获取logger实例
logger = logging.getLogger("openai")

# 设置日志级别，例如设置为DEBUG级别
logger.setLevel(logging.DEBUG)

# 创建控制台处理器并设置日志级别
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 创建格式化器并添加到控制台处理器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# 将控制台处理器添加到logger
logger.addHandler(ch)

# 使用OpenAI API
# openai.api_key = 'your_openai_api_key'

# 示例请求
response = openai.chat.completions.create(
    model="davinci",
    messages="Translate the following English text to French: 'Hello, how are you?'",
)

print(response)
