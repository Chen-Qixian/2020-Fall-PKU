#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :3-special.py
@Description  :定制类
@Time         :2020/10/26 15:38:57
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''


# 修改对象打印信息 __str__ & __repr__
# 在对象本身没有某属性时，访问__getattr__，动态绑定该属性的值
# 将对象本身设置为可调用的方法，只需添加__call__()方法
# callable用于判断某一类实例是否有__call__()方法
class Student(object):
    def __init__(self, name):
        self.name = name

    # 修改print该对象的输出内容
    def __str__(self):
        return 'Object Student (name: %s)' % self.name

    # 直接输入变量会调用此显示方法
    __repr__ = __str__

    # 注意：仅在对象本身不含该属性时调用该方法，如name不会调用该方法
    def __getattr__(self, attr):
        if attr == 'score':
            return 100
        elif attr == 'age':
            return lambda: 18
        else:
            # 添加一个对于可添加属性的约束
            raise AttributeError(
                'class Student does not have attribute %s!' % attr)

    def __call__(self, n):
        print('My name is %s, input number is %d' % (self.name, n))


s = Student('ChrisChen')
print(s)
print(s.score)
# 注意：动态返回函数的属性需要调用
print(s.age())
# 不调用__getattr__
print(s.name)
# print(s.abc) 报错：被约束
# 先用callable方法判断该类的实例是否具有__call__()方法，即是否为可调用的
if callable(s):
    s(100)
print(callable([1, 2, 3]))
print(callable((1,)))
print(callable(abs))


# 利用动态getattr实现链式调用
class Chain(object):
    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        if path == 'user':
            return lambda name: Chain('%s/%s' % (self.path, name))
        return Chain('%s/%s' % (self.path, path))

    def __str__(self):
        return self.path


c = Chain()
# 可以实现API名称的动态改动，用具体的用户名代替user位置的变量
print(c.server.user('Chen').timeline.list)


# 使对象可迭代 __iter__ & __next__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    # 返回自己，对象本身就是一个可迭代的
    def __iter__(self):
        return self

    # 重定义next方法 【注意新版本python中定义为__next__】
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

    # 让对象可以像list一样取出元素
    def __getitem__(self, n):
        # 尝试对切片进行处理，先判断传入参数的类型
        if isinstance(n, int):
            x, y = 0, 1
            for i in range(n):
                x, y = y, x + y
            return x
        # 若为切片类型
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            x, y = 0, 1
            L = []
            for i in range(stop):
                x, y = y, x + y
                if i >= start:
                    L.append(x)
            return L


for n in Fib():
    print(n, end=' ')
print()

f = Fib()
print('f[100] =', f[100])
print('f[3:5] =', f[3:5])
print('f[:10] =', f[:10])
