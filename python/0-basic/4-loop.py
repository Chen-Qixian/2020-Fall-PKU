#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :4-loop.py
@Description  :练习循环
@Time         :2020/10/17 11:44:28
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''

names = ['a', 'b', 'c', 'd']
for name in names:
    print(name)
for i in range(5):
    print(i)
_sum = 0
for i in range(1, 101):
    _sum += i
print(_sum)
