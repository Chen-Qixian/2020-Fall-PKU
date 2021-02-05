#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :1-property.py
@Description  :@property
@Time         :2020/10/24 22:56:38
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
# 使用@property的getter setter的好处是，可以直接用为对象属性赋值，且可以对设置的属性进行检查


# 直接写属性会导致不合法数据的问题 而使用方法检查会显得臃肿 例如
class Student(object):
    def get_score(self):
        return self.score

    def set_score(self, sc):
        if not isinstance(sc, int):
            raise TypeError('Score must be an integer!')
        if not 0 <= sc <= 100:
            raise ValueError('Score range error!')
        self.score = sc


s = Student()
s.set_score(100)
print(s.get_score)
# s.set_score('a') 抛出异常
# s.set_score(9999) 抛出异常


# 引入@property内置装饰器可以将属性检查方法在设置对象属性时被调用
class Person(object):
    # 这个@property相当于一个getter
    @property
    def score(self):
        return self.__score

    # 调用@property的同时相当于自动生成了一个setter
    # 若无此setter相当于一个只读属性
    @score.setter
    def score(self, sc):
        if not isinstance(sc, int):
            raise TypeError('Score must be an integer!')
        if not 0 <= sc <= 100:
            raise ValueError('Score range error!')
        self.__score = sc


p = Person()
p.score = 100
# p.score = 'abc' 抛出异常
# p.score = 9999 抛出异常


# 【注意】getter setter只能写成私有属性！！！
class Screen(object):

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        self.__width = w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        self.__height = h

    @property
    def resolution(self):
        return self.__width * self.__height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
