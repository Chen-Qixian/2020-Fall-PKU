#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :0-class-object.py
@Description  :类和实例
@Time         :2020/10/22 16:45:35
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''


class Student(object):
    # 类似于构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    def getGrade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        elif self.score >= 60:
            return 'D'
        else:
            return 'F'


s = Student('ChrisChen', 18)
s.score = 100
print(s.getAge())
print(s.getGrade())
