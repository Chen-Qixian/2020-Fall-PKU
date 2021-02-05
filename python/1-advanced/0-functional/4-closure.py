#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :4-closure.py
@Description  :返回函数（函数闭包）
@Time         :2020/10/21 16:42:03
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''


# 内部函数返回外部函数局部变量和参数，并将该内部函数返回，形成闭包
# 外部函数的局部变量和参数被保存在返回的函数中
def lazy_sum(*args):
    def sum():
        total = 0
        for n in args:
            total += n
        return total
    return sum


f1 = lazy_sum(1, 3, 5, 7, 9)
# 返回的函数没有立即执行，而是需要单独（）调用执行
print(f1)
print(f1())
f2 = lazy_sum(1, 3, 5, 7, 9)
# 即使参数相同，返回的两个函数也不相同
print(f1 == f2)


# 闭包的一个问题：返回函数尽量不要引用循环变量
def count():
    res = []
    for i in range(1, 4):
        def f():
            return i * i
        res.append(f)
    return res


f1, f2, f3 = count()
# 输出9 9 9:因为当调用这个 f 的时候引用的i已经变成了3
print(f1(), f2(), f3())


# 修改
def count2():
    def f(i):
        def g():
            return i * i
        return g
    res = []
    # 此时f(i)立即执行，当前i的值作为参数传给了g保存并返回，因此i可以取得当前值
    for i in range(1, 4):
        res.append(f(i))
    return res


f1, f2, f3 = count2()
print(f1(), f2(), f3())


# 闭包实现计数器
def counter():
    cnt = 0

    def ret():
        nonlocal cnt
        cnt += 1
        return cnt
    return ret


counterA = counter()
print(counterA(), counterA(), counterA())
