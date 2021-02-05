#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :2- multiInherit.py
@Description  :多继承
@Time         :2020/10/26 15:30:48
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
# 不同于只能单继承的JAVA， pyhton允许多继承
# 在设计继承层次时，最好设计一个继承主线，其他的多继承设计成mixin，即混入的新增功能


class Animal(object):
    def what(self):
        print('I am animal')


class RunnableMixin(object):
    def run(self):
        print('Running...')


class FlyableMixin(object):
    def fly(self):
        print('Flying...')


class Dog(Animal, RunnableMixin):
    def __init__(self):
        print('I am a dog')


class Bird(Animal, FlyableMixin):
    def __init__(self):
        print('I am a bird')


# 通过多继承，子类可以获得多个父类的全部功能
d = Dog()
b = Bird()
d.what()
d.run()
b.what()
b.fly()
