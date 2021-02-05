#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :12-iterator.py
@Description  :迭代器
@Time         :2020/10/19 16:15:25
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''

# Iterable 和 Iterator 的区别：
# 前者静态的，可以迭代； 后者动态运算，具有惰性，只有当调用了next()时，才会计算下一个值
from collections.abc import Iterable, Iterator
print('Iterable:')
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('str', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(123, Iterable))
print('Iterator:')
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('str', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(123, Iterator))
print('iter()')
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('str'), Iterator))
