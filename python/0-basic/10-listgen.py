#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :10-listgen.py
@Description  :列表生成式
@Time         :2020/10/17 17:08:19
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
import os

l1 = list(range(11))
l2 = list(range(1, 11))
l3 = list(range(0, 11, 2))
print(l1)
print(l2)
print(l3)
l4 = [x * x for x in range(11)]
# 生成式for后面加判断作用是筛选，不能加else
l5 = [x * x for x in range(11) if x % 2 == 0]
# 生成式for前面加判断用于改变值，必须加else
l6 = [x if x % 2 == 0 else -x for x in range(11)]
# 生成式可以两层for
l7 = [x + y for x in 'ABC' for y in 'abc']
print(l4)
print(l5)
print(l6)
print(l7)
d = {'a': 1, 'b': 2, 'c': 3}
l8 = [k + '=' + str(v) for k, v in d.items()]
# 输出当前路径下所有文件
l9 = [di for di in os.listdir('.')]
print(l8)
print(l9)
# 应用：全部转为小写字母
lstr = ['Hello', 'WORLD', 'Chris', 8, False, 'Chen']
l10 = [s.lower() for s in lstr if isinstance(s, str)]
print(l10)
