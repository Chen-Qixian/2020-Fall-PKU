#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :5-anonymous.py
@Description  :匿名函数lambda表达式
@Time         :2020/10/21 17:25:14
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''


l = [x for x in range(11)]
print(list(map(lambda x: x * x, l)))
