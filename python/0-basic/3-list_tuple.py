#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :3-list_tuple.py
@Description  :practice python list and tuple
@Time         :2020/10/17 11:21:50
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''

# list增删改查
classmates = ['Alice', 'Bob', 'Chris', 'Dimash']
print(classmates)
print(classmates[0])
# classmates[x] : x >= 0 ? classmates[x]: classmates[len - x]
print(classmates[-2])
print(len(classmates))
classmates.append('Ella')
print(classmates)
classmates.insert(2, 'Cherry')
print(classmates)
# pop()默认最后一个元素，有返回值
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)
classmates[1] = 'Yomen'
print(classmates)

# list可以混合元素类型存储
strs = 'Chen'
pi = 3.14
lists = ['a', 1, False, ['Chris', strs], pi]
print(len(lists), lists)
# 定义空list
nullList = []
print(len(nullList))

# 定义tuple， 与list不同， tuple一旦定义无法修改
# 维护数据安全性，阻止非法修改
friends = ('Lihang', 'WangYankai', 'ZhaoHaosen')
print(friends[1])
print(friends[-3])
print(friends)
tuples = (1, 'abc', True, [1, 'X', False])
print(tuples)
print(tuples[-1][-2])
# tuples[-1] = 'Y' 报错：tuple不能修改元素
# 下面这种形式可以，因为实质上修改的是list
tuples[-1][-2] = 'Y'
print(tuples)
# 定义只有1个元素的tuple 注意避免歧义
single = (1,)
print(single)
# 定义空tuple
nullTuple = ()
print(len(nullTuple))
