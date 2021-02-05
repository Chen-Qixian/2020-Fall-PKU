#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :3-sorted.py
@Description  :排序函数
@Time         :2020/10/20 22:16:04
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''

# 排序函数也是高阶函数
l = [3, 0, -1, 2, 4, -9, 5, -7, 8, -2]
a = sorted(l)
b = sorted(l, key=abs)

# 排序
n = ['Alice', 'Zebby', 'alex', 'danvers']
c = sorted(n)
d = sorted(n, key=str.lower)
e = sorted(n, key=str.lower, reverse=True)
print(a)
print(b)
print(c)
print(d)
print(e)

# 成绩表的排序
mark = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
f = sorted(mark, key=by_name)
g = sorted(mark, key=by_mark)
print(f)
print(g)


def by_mark(t):
    return t[0]


def by_name(t):
    return -t[1]
