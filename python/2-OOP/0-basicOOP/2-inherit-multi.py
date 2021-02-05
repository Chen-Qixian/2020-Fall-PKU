#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :2-inherit-multi.py
@Description  :继承 多态
@Time         :2020/10/22 23:02:32
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''


class Animal(object):
    def run(self):
        print('Animal is running ...')


# 继承
class Dog(Animal):
    def eat(self):
        print('Dog is eating ...')


class Cat(Animal):
    # 多态
    def run(self):
        print('Cat is running ...')


a = Animal()
d = Dog()
c = Cat()
a.run()
d.run()
c.run()
print(isinstance(a, Animal))
print(isinstance(d, Animal))
print(isinstance(c, Animal))
print(isinstance(a, Dog))
print(isinstance(d, Dog))
print(isinstance(c, Cat))


# 多态的用途：新增Animal一个子类，不需要重写该方法
# 开放封闭原则：
#    对扩展开放：可以新增子类
#    对修改封闭：无需修改依赖Animal的方法
def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Cat())


class Turtle(Animal):
    def run(self):
        print('Turtle is running slowly ...')


run_twice(Turtle())


# 鸭子类型：python是动态语言 与Java这种静态语言不同，不要求有严格的继承体系
class Time(object):
    def run(self):
        print('Start ...')


run_twice(Time())
