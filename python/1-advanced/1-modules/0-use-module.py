#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :0-use-module.py
@Description  :一个标准模块文件
@Time         :2020/10/22 15:46:48
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''

# 模块的定义：
# 每个.py文件就是一个模块
# 为了区分同名模块引入包的概念
# 每个包中都含有一个 __init__.py的文件 该文件就是一个模块 模块名即为包名

import sys
'The 1st module hello'

__author__ = 'Chris Chen'


def greeting():
    # sys.argv 用于在执行时 从控制台接受参数列表
    args = sys.argv
    if len(args) == 1:
        print('Hello world!')
    elif len(args) == 2:
        # 注意： 接收到的第一个参数为该模块名
        print('Hello %s' % args[1])
    else:
        print('Too many arguments')


# 从习惯上 不应该引用private变量
# private变量的命名习惯以 _开头
# 优点： 外界调用public函数时不关心内部private的具体实现，实现了数据封装
def _private_1(name):
    print('Hello, %s' % name)


def _private_2(name):
    print('Hi, %s' % name)


def greet(name):
    if len(name) > 3:
        _private_1(name)
    else:
        _private_2(name)


# 每次从命令行执行该模块时，解释器自动将__name__变量置为__main__，而被其他模块引用时则不会
# 好处： 方便测试
if __name__ == '__main__':
    greeting()
    greet('CCC')
    greet('dddd')
