#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :6-set.py
@Description  :
@Time         :2020/10/17 14:23:15
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''

s = set([1, 2, 3])
print(s)
# set为无重复元素集合，自动过滤重复元素
s.add(3)
print(s)
s2 = set([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3])
print(s2)
# 报错，不存在该元素
# s.remove(4)
# 鲁棒性写法，应该先判断是否存在
if 3 in s2:
    s2.remove(3)
    print(s2)
else:
    print('No such element')
if 5 in s2:
    s2.remove(3)
    print(s2)
else:
    print('No such element')
# 集合求交集并集
s1 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
# 报错unhashable，可变对象不能加入到set
# s1.add([1, 2, 3])

# 可变对象与不可变对象
a = ['c', 'b', 'a']
a.sort()
print(a)
# replace是返回一个字符串副本，并不真正改变a的值
a = 'abc'
b = a.replace('a', 'A')
print(a)
print(b)
# set可以加入tuple，但该tuple中不能含有list
s.add((1, 2, 3, 4))
# s.add((1, [2, 3])) 报错
print(s)
