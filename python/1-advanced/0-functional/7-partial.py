#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :7-partial.py
@Description  :偏函数
@Time         :2020/10/22 15:21:15
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
import functools
# 偏函数的优点：可以固定函数默认传入的参数
# 创建偏函数：接受一个函数对象、可变参数*args、关键字参数**kw
# 定义一个默认2进制转换的偏函数
# 相当于固定传入关键字参数 **kw = {'base': 2}
int2 = functools.partial(int, base=2)
print(int2('100100101'))
# 但偏函数仍可以修改base
print(int2('10010', base=3))
# 偏函数可以固定可变参数
# 定义一个默认和10比较的求最大值函数
# 相当于固定了可变参数中有一个*args = (10)
max10 = functools.partial(max, 10)
print(max10(1, 2, 3, 4))
