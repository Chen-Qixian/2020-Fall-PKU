#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :7-function.py
@Description  :定义并调用函数
@Time         :2020/10/17 14:45:10
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''

import math


# 定义一个空函数
def nop():
    pass


# 定义一个函数，并添加一个参数类型判断，使用isinstance函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Invalid operand type')
    return x if x >= 0 else -x


# 函数可以有多个返回值，组成一个tuple
# 可以使用默认参数，在传入参数时，可缺省该位
def move(x, y, step=1, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


# 传递特定的参数
def enroll(name, sex, age=18, city='Beijing'):
    print('name:', name)
    print('sex:', sex)
    print('age:', age)
    print('city:', city)


# 注意默认参数必须是不变对象
def add_end(L=[]):
    L.append('end')
    return L


# 修改上述函数实现每次创建新的list
def add_end2(L=None):
    if L == None:
        L = []
    L.append('end')
    return L


# 实现可变参数
def multiple(x=0, *y):
    ret = x
    for i in y:
        ret *= i
    return ret


# 实现关键字参数
def person(name, sex, **kw):
    print('name: ', name, 'sex: ', sex, 'other: ', kw)


# 实现命名参数：命名参数可以设定默认值
def person2(name, *, job, city):
    print(name, job, city)


# 若有可变参数，则在可变参数后的均为命名参数
def person3(name, *args, job, city):
    print(name, job, city)
    for i in args:
        print(i)


# 函数调用测试
print(my_abs(1))
print(my_abs(0))
print(my_abs(-1))
# print(my_abs('A'))

r = move(100, 100, 60, math.pi / 6)
print(r)
# 调用传递特定位置参数 和有默认参数 的函数
enroll('ChrisChen', 'Male')
enroll('QilingZi', 'Female', city='Shanghai')

# 注意 当默认参数为可变对象时，参数将指向这个对象本身，即 该参数在函数定义时就已经被计算出来
print(add_end())
print(add_end())
print(add_end())
# 修改如下: 【重点】必须采用不变对象当默认参数
print(add_end2())
print(add_end2())
print(add_end2())

# 不可变对象的好处： 创建后内部数据不会改变，数据安全。 且多线程环境下读取该对象无需加锁，方便

# 可变参数：用*args接受多个参数，args为一个tuple
# 调用方式1
print(multiple(5))
print(multiple(5, 4))
print(multiple(5, 4, 3))
# 调用方式2:将 list / tuple 转化成可变参数传入
multi_list = [5, 4, 3, 2]
print(multiple(*multi_list))

# 关键字参数：用**kw表示的参数，kw为一个dict
person('A', 'F')
person('B', 'M', age=18, job='CTO', married=False)
# 另一种调用方式，将一个dict转化成关键字参数
# 注意这种方式是拷贝一个keywords副本传入函数，函数中对kw的改变不会影响到keywords
keywords = {'age': 20, 'job': 'CEO'}
person('C', 'F', **keywords)

# 命名参数： 必须传递对应指定参数名
person2('D', job='doctor', city='Shanghai')
# person2('D', 'doctor', 'Shanghai') 报错：不指定名称的参数会默认为位置参数
person3('E', 20, city='Beijing', job='engineer')

# 多种参数混合 注意顺序：必选 - 默认 - 可变 - 命名 - 关键字
