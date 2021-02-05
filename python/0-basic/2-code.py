#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :2-code.py
@Description  :字符串编码
@Time         :2020/10/17 11:22:11
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''

# 返回字符的编码，和数值对应的字符
en = 'a'
ch = '中'
print(ord(en))
print(ord(ch))
en = 98
ch = 25991
print(chr(en))
print(chr(ch))
# b开头的字符串由byte表示
x = b'abc'
print(x)
# 编码与解码
a = 'ABC'.encode('ascii')
print(a)
b = 'ads中文'.encode('utf-8')
print(b)
c = a.decode('ascii')
print(c)
d = b.decode('utf-8')
print(d)
# 使用errors='ignore'忽略掉无效字符
e = b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
print(e)
# len返回字符串长度，若作用域b'str'对象则返回字符串的字节数
f = len(e)
print(f)
# utf-8可变长的unicode编码，长度1-6字节，英文1字节，中文3字节
g = len(b)
print(g)

# 格式化字符串输出两种推荐方法
name = 'Chris Chen'
age = 18
rate = 0.001
print('Hello, %s! Your age is %d\n Your grade is in top %.3lf %%' %
      (name, age, rate))
r = 3
s = 3.14 * r ** 2
print(f'The area of circle with radius {r} is {s}')

s2 = 85
s1 = 72
r = (s2 - s1) / s1
print('小明成绩提升了%.1lf%%' % r)
