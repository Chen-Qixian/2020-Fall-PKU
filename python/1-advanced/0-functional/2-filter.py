#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :2-filter.py
@Description  :过滤器
@Time         :2020/10/19 20:38:56
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''


# 过滤偶数
def getOdd(lim):
    return list(filter(lambda x: x % 2 == 0, [x for x in range(lim)]))


print(getOdd(20))


# 过滤非空
def notNull(l):
    return list(filter(lambda s: s, l))


print(notNull([1, True, 'abc', '  ', '', 0, False, 123]))


# 筛素数
def getPrime(lim):
    yield 2

    def _gen_odd():
        x = 1
        while True:
            x += 2
            yield x

    def _is_division(d):
        return lambda x: x % d != 0

    it = _gen_odd()
    while True:
        n = next(it)
        if n > lim:
            break
        yield n
        it = filter(_is_division(n), it)


for x in getPrime(100):
    print(x)
