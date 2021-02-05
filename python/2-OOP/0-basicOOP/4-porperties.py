#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :4-porperties.py
@Description  :实例属性和类属性
@Time         :2020/10/23 22:05:43
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''


# 给类绑定一个实例，该类所有实例都可以访问到他

class Student(object):
    name = 'student'
    count = 0

    def __init__(self):
        self.count += 1


s = Student()
print(s.name)
print(Student.name)
s.name = 'Chris'
# 实例属性优先级更高 屏蔽掉类属性
print(s.name)
print(Student.name)
# 删除实例属性后仍保持类属性
del s.name
print(s.name)


# 通过构造函数 self 传递的属性为对象属性
class Person(object):
    # 该属性只归对象所有
    def __init__(self, name):
        self.name = name


p = Person('Chris')
p.age = 18
print(p.name)
# print(Person.name) 报错：类无此属性
