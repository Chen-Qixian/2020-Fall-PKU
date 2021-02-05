#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :1-private.py
@Description  :访问限制
@Time         :2020/10/22 16:55:03
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''


# 如果以双下划线开头则声明为private变量
# 优点：数据保护 提高鲁棒性
class Student(object):
    __name = 'default'
    __age = 18
    __score = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 使用getter setter 对类内部数据进行访问
    def getAge(self):
        return self.__age

    # setter好处：可以对数据合法性进行检查
    def setScore(self, sc):
        if 0 <= sc <= 100:
            self.__score = sc
        else:
            raise ValueError('Score out of range!')

    def getGrade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 80:
            return 'B'
        elif self.__score >= 70:
            return 'C'
        elif self.__score >= 60:
            return 'D'
        else:
            return 'F'


s = Student('Chris.Chen', 22)
print(s.getAge())
# print(s.__age) 报错：私有变量无法在类外部直接访问
s.setScore(100)
print(s.getGrade())
# 【不推荐】也可以访问双下划线开头
print(s._Student__score)  # 不报错，但是不推荐！！
# 【错误】为双下划线变量赋值可以进行，但与类成员不是同一个变量
s.__score = 80
print(s.getGrade())  # 还是A，上述修改没有成功
# 【注意】总之：无论如何都不要尝试给一个private赋值 或 访问
# 以双下划线开头且结尾的变量不是私有变量可以被外部访问
