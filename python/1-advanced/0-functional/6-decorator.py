#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :6-decorator.py
@Description  :装饰器
@Time         :2020/10/21 17:38:48
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
import functools
import time


def now():
    print('2020-10-21')


f = now
f()
print(now.__name__)
print(f.__name__)


# 添加装饰器在调用函数前打印日志
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('Call function %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# @log语法相当于 time = log(time)
# 此时time被替换成了wrapper：先执行日志打印语句，再执行time函数
@log
def time1():
    print('17:38:48')


time1()


# 需要传入参数的装饰函数
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# 相当于：time2 = log2('exectue')(time2)
@log2('execute')
def time2():
    print('13:28:02')


time2()
print(time2.__name__)


# 定义一个可以打印函数执行时间，并能提示开始和结束调用的位置
def log3(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('Call %s() start' % fn.__name__)
        start = time.time()
        res = fn(*args, **kw)
        print('function %s() executed %s ms' %
              (fn.__name__, time.time() - start))
        print('Call %s() end' % fn.__name__)
        return res
    return wrapper


@log3
def add(x, y):
    time.sleep(0.012)
    return x + y


@log3
def multi(x, y):
    time.sleep(0.123)
    return x * y


print(add(1, 2))
print(multi(5, 6))
