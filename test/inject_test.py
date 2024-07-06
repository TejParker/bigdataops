#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：xin wei
@Date    ：2024-07-06 0:21 
@explain : 文件说明
"""
from injector import inject, Injector


class A:
    name: str = "bigdata-ops"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"Class A: name: {self.a.name}")


injector = Injector()
b_instance = injector.get(B)
b_instance.print()
