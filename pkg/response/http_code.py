#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-07 0:28 
@explain : 文件说明
"""
from enum import Enum


class HttpCode(str, Enum):
    """HTTP基础业务状态码"""
    SUCCESS = "success"
    FAIL = "fail"
    NOT_FOUND = "not_found"
    UNAUTHORIZED = "unauthorized"
    FORBIDDEN = "forbidden"
    VALIDATE_ERROR = "validate_error"  # 数据验证错误
