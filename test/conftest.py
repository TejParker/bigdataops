#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-07 21:27 
@explain : 文件说明
"""
import pytest

from app.llmapp.app import app


@pytest.fixture
def client():
    """构建Flask应用的测试应用，并返回"""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
