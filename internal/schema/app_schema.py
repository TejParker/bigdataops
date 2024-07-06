#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-07 0:04 
@explain : 文件说明
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    """基础聊天接口请求验证"""
    query = StringField("query", validators=[
        DataRequired(message="用户的提问是必填的"),
        Length(max=2000, message="用户的提问最大长度是2000"), ])
