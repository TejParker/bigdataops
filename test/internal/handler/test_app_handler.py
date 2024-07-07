#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-07 21:16 
@explain : 文件说明
"""
import pytest

from pkg.response import HttpCode


class TestAppHandler:
    """app handler 测试类"""

    @pytest.mark.parametrize("query", [None])
    def test_chat_completion(self, query, client):
        # resp = client.post("/app/completion", json={"query": "hello, who are you?"})
        resp = client.post("/app/completion", json={"query": query})
        print("测试 chat_completion")
        assert resp.status_code == 200
        # assert resp.json.get("code") == HttpCode.SUCCESS
        if query is None:
            assert resp.json.get("code") == HttpCode.VALIDATE_ERROR
        else:
            assert resp.json.get("code") == HttpCode.SUCCESS
