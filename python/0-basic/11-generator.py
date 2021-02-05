#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :11-generator.py
@Description  :生成器
@Time         :2020/10/18 16:48:37
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''

g = (x * x for x in range(9) if x % 2 == 0)
print(g)
# 基本上不使用next方法，因为generator是iteratable对象，使用next有可能造成StopIteration错误
print(next(g))
# generator是可遍历的
for n in g:
    print(n, end=' ')
print()


# generator另一定义：函数中使用yield
# 每次执行到yield后 返回，不同于return，下次调用generator从上一个yield后继续执行
def fib(lim):
    n, a, b = 0, 0, 1
    while n < lim:
        yield a
        a, b = b, a + b
        n += 1
    return 'done'


f = fib(20)
for n in f:
    print(n, end=' ')
print()

f = fib(6)
while True:
    try:
        x = next(f)
        print(x, end=' ')
    except StopIteration as e:
        print('\nGenerator return value', e.value)
        break


# 定义杨辉三角形生成器
def triangle1():
    arr = [1]
    while True:
        yield arr
        l = len(arr)
        if l == 1:
            tmp = [1, 1]
            arr = tmp
        else:
            tmp = [1]
            for i in range(l-1):
                tmp.append(arr[i] + arr[i+1])
            tmp.append(1)
            arr = tmp


def triangle2():
    l = [1]
    while True:
        yield l
        # 注意数组拼接+列表生成式的运用
        l = [1] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [1]


# 测试上述函数
n = 0
results = []
for t in triangle2():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for r in results:
    print(r)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
