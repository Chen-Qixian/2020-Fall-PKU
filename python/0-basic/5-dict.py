#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :5-dict.py
@Description  :字典的练习
@Time         :2020/10/17 14:13:10
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''

# dict字典本质是一个hash map，因此必须使用不可变对象 如 数字 字符串作为key，不能用list等作为key
d = {'Chris': 100, 'Violet': 99, 'Alice': 70, 'Bob': 60}
print(d['Chris'])
d['Chris'] = d['Violet']
d['Violet'] = 100
print(d)
if 'Bob' in d:
    print(d['Bob'])
print('bob' in d)
print(d.get('Alice'))
# 未找到默认返回None
print(d.get('alice'))
# 可以指定未找到该key的返回值
print(d.get('alice'), -1)
# 删除某key的值
print(d.pop('Alice'))
print(d)
# 可以直接插入新的key-value对
d['Emma'] = 59
print(d)

# list不能作为dict的key unhashable
# d = {[1, 2]: 1} 报错
# 但是可以作为value
d = {1: [1, 2], 2: [3, 4]}
print(d)
# tuple可以作为dict的key，但tuple中不能带有list可变对象
# d = {(1, 2, 3): 1, (1,): 2, (1, [2, 3]): 3} 报错
d = {(1, 2, 3): 1, (1,): 2}
print(d)
print(d[(1,)])
