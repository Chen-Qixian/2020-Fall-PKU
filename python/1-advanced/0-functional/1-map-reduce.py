#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :1-map-reduce.py
@Description  :map reduce
@Time         :2020/10/19 19:19:43
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
from functools import reduce


def f(x):
    return x * x


x = [1, 2, 3, 4, 5]
# map接受两个参数，function和 iterable，效果为对iterable中每个元素调用function
y = list(map(f, x))
print(y)
y = list(map(str, x))
print(y)


# 【例1】reduce接受两个参数，效果为调用两个元素的结果累加到下一个元素的函数调用中
# 一个累加和的方法：等价于sum()
def add(a, b):
    return a + b


print(reduce(add, x))


# 【例2】数字拼接的例子
def trans(a, b):
    return a * 10 + b


print(reduce(trans, x))


# 【例3】字符串转数字：等价于int()方法
# python中允许在函数中定义函数
def str2int(s):
    def fn(a, b):
        return a * 10 + b

    def char2num(ch):
        return ord(ch) - ord('0')
    return reduce(fn, map(char2num, s))


print(str2int('19981219'))


# 【例4】格式化字符串
def str2float(s):
    idx = len(s) - 1 - s.index('.')
    s = s.replace('.', '')
    return reduce(lambda x, y: x*10+y, map(lambda ch: ord(ch)-ord('0'), s)) / (10 ** idx)


print('str2float(\'1243.4567\') =', str2float('1243.4567'))
if abs(str2float('1243.4567') - 1243.4567) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
