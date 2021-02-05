#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :8-slice.py
@Description  :list切片功能
@Time         :2020/10/17 16:11:38
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''

l = list(range(100))
print(l[:10])
print(l[-10:])
print(l[10:20:2])
print(l[::5])
# 拷贝一份l
print(l[:])
# 对字符串进行相似的切分
s = 'hello world!'
print(s[:5])
print(s[6:])
print(s[1:8:2])
print(s[::3])
s2 = s[:]
s2 = 'c'
print(s)
print(s2)


def trim(s):
    i = 0
    j = len(s) - 1
    while i <= j and s[i] == ' ':
        i += 1
    while j >= i and s[j] == ' ':
        j -= 1
    if i == len(s):
        return ''
    return s[i:j+1]


print(trim('   sdf ') == 'sdf')

# 切片的赋值操作： 注意！ 右侧应为一个list！
l = [0, 1, 2, 3, 4, 5]
# 切取[2,2)获得一个l的浅拷贝：因此赋值会修改原list！相当于像下标2插入一个元素
l[2:2] = [100]
print(l)
# 获得[2,2)即[100]替换为[88]
l[2:3] = [88]
print(l)
# 将[2,5)即[88,2,3]替换为[77,66]
l[2:5] = [77, 66]
print(l)
# 由于l[2:0]返回也为[]，下标从2开始，因此也是像下标2插入一个list
print(l[2:0])
l[2:0] = [55, 44, 33]
print(l)
