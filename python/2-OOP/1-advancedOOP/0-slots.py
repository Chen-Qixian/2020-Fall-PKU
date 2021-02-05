#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :0-slots.py
@Description  :限制属性绑定
@Time         :2020/10/24 21:15:49
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''


# python属于动态语言 对于任意class可以动态绑定一个属性/方法
from types import MethodType


class Person(object):
    pass


p = Person()
p.name = 'ChrisChen'


def set_age(self, age):
    self.age = age


# 可以运行：忽略插件报错
p.set_age = MethodType(set_age, p)
# p.set_age(18)   # 可以执行
# print(p.name, p.age)  # 可以执行

# 但是其他对象不共享此方法
# p2 = Person()
# p2.set_age(18)  # 报错：无此方法


def set_score(self, sc):
    self.score = sc


Person.set_score = set_score
p.set_score(100)
# print(p.score)  # 可以执行：可以为该类每个对象添加score属性


# 如果要限制可以为类添加的属性，可以使用 __slots__
class Student(object):
    # 注意：使用字符串表示变量名
    __slots__ = ('name', 'score')


s = Student()
s.name = 'ChenQixian'
s.score = 'A+'
# s.age = 18  # 报错：不允许绑定未规定的属性
print(s.name, s.score)


# 但是继承他的子类则取消了slots的限制
class SubStudent(Student):
    pass


ss = SubStudent()
ss.subname = 'subobj'
print(ss.subname)
