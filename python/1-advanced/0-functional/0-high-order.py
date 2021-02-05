#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :0-high-order.py
@Description  :函数式编程-高阶函数
@Time         :2020/10/19 19:02:36
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''

# 变量可以指向函数名，表示这个函数
f = abs
print(f(-10))

# 函数名也是变量 可以修改
abs = 10
# print(abs(-10))   报错：因为abs此时已编程一个数字，说明函数名作为变量可以修改


# 可以将函数名作为变量、参数传入函数中
# 高阶函数：让函数的参数能够接收别的参数
def add(x, y, f):
    return f(x) + f(y)


print(add(-1, 2, f))
