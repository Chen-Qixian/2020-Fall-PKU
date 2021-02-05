#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :0-handler.py
@Description  :错误处理
@Time         :2020/10/26 18:59:39
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
# except 捕获对应异常，finally是一定会执行的语句
import logging
print('#1')
try:
    print('try...')
    r = 10 / 0
    print(r)
except ZeroDivisionError as e:
    print('exception', e)
finally:
    print('finally...')
print('end')

print('#2')
try:
    print('try...')
    r = 10 / 2
    print(r)
except ZeroDivisionError as e:
    print('exception', e)
finally:
    print('finally...')
print('end')

# 多个异常接收情况
print('#3')
try:
    print('try...')
    r = 10 / int('a')
    print(r)
except ValueError as e:
    print('exception', e)
except ZeroDivisionError as e:
    print('exception', e)
finally:
    print('finally...')
print('end')

# 无异常会执行else
print('#4')
try:
    print('try...')
    r = 10 / 3
    print(r)
except ValueError as e:
    print('exception', e)
except ZeroDivisionError as e:
    print('exception', e)
else:
    print('no exception')
finally:
    print('finally...')
print('end')

# 类似ValueError, ZeroDivisionError均属于错误类
# 均有继承关系，所有错误类均继承自BaseException
# 会捕获该错误类型的所有子类错误
# 已被前面的except捕获的错误 不会再被后续except捕获
print('#5')
try:
    print('try...')
    r = 10 / 0
    print(r)
except BaseException as e:
    print('exception1', e)
# 此错误不会重复捕获，因为BaseException是所有异常的父类
except ZeroDivisionError as e:
    print('exception2', e)
else:
    print('no exception')
finally:
    print('finally...')
print('end')
# 跨调用层次捕获异常：仅在最顶层设置错误捕获即可，无需重复捕获
# 使用logging，将错误栈保存至日志
print('#6')


def foo(s):
    return 10 / int(s)


def bar(s):
    return 2 * foo(s)


def main():
    try:
        a = bar('0')
        print(a)
    except ZeroDivisionError as e:
        # logging打印完整的错误栈日志
        logging.exception(e)


main()
# 抛出异常
print('#7')


class MyException(ValueError):
    pass


def foo(x):
    if x == 0:
        raise MyException('Invalid value %s' % x)
    return 10 / x


try:
    foo(0)
except MyException as e:
    print('exception:', e)


# 另一种异常处理，直接在except中将异常 raise原样抛出，交给用户处理
