#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :9-iteration.py
@Description  :迭代
@Time         :2020/10/17 16:40:05
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''

for i in range(10):
    print(i, end=' ')
print()
for i in range(5, 20, 3):
    print(i, end=' ')
print()
l = [3, 2, 5, 1, 3]
for i in l:
    print(i, end=' ')
print()
d = {'a': 1, 'b': 2, True: 3}
for key in d:
    print(key, end=' ')
print()
for value in d.values():
    print(value, end=' ')
print()
for item in d.items():
    print(item, end=' ')
print()
for item in d.items():
    print(item[0], item[1], end=' ')
print()
s = 'abcd'
for ch in s:
    print(ch, end=' ')
print()
l1 = [[0, 0], [0, 1], [0, 2], [1, 1]]
for x, y in l1:
    print(x, y, end=' ')
print()
# 使用下标迭代
for i, value in enumerate(l):
    print(i, value)
