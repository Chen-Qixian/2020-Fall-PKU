#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :0-basic.py
@Description  :正则表达式基础
@Time         :2020/11/05 20:39:12
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
# 技巧： 使用python字符串的r前缀，可以避免转义符的问题
import re

# 判断是否匹配成功
target = '010 - 62750443'
# 注意：整行匹配需要使用^$进行控制
reg = '\d{3}\s*-\s*\d{8}'
# 原理：match成功返回一个Match对象，否则返回None
if re.match(reg, target):
    print('Yes')
else:
    print('No')

# split切分字符串
# 正常切分，会有空白字符
print(re.split(r' ', 'a b  c'))
# 切分多个空格
print(re.split(r'\s+', 'a b  c'))
# 切分带逗号
print(re.split(r'[\,\s]+', 'a,b, c   d'))
# 切分带分号
print(re.split(r'[\;\,\s]+', 'a;;b;c, d,; e   f'))

# 注意 r 前缀的使用，在正则表达式里，
# 只有类似于[] {} , + \这些有特殊含义的符号时，前面需要加一个\转义
# 无r前缀情况下，上述符号会被解释成相应的特殊含义
if re.match(r'\[\\\,\\s\]\+', '[\,\s]+'):
    print('Yes')
else:
    print('No')

# 分组（）
reg = r'(\d{3})\s*-\s*(\d{3,8})'
m = re.match(reg, '010 -  12345')
# 第0组为全体
print(m.group(0), m.group(1), m.group(2))

# 切分时间
time = '16:06:24'
treg = r'^([0-2][0-9]|[0-9])\:([0-5][0-9]|[0-9])\:([0-5][0-9]|[0-9])$'
ma = re.match(treg, time)
if ma:
    h = ma.group(1)
    m = ma.group(2)
    s = ma.group(3)
    print(h, m, s)
else:
    print('Error')

# 贪婪匹配：默认为贪婪匹配，即尽可能多匹配字符
# 若要取消贪婪，添加一个？即可
greg = r'^(\d+)(0*)$'
print(re.match(greg, '102300').groups())
ngreg = r'^(\d+?)(0*)$'  # 非贪婪
print(re.match(ngreg, '102300').groups())

# 编译：提高效率
# 由于每次匹配都需要先编译正则表达式，非法的正则表达式会报错，而后再去匹配
reg_comp = re.compile(r'[\w\d\._]+@\w+?(\.\w+)+')
print(reg_comp.match('chenqixian@stu.pku.edu.cn') != None)
print(reg_comp.match('chenqixian@stu.pku.edu.') != None)
print(reg_comp.match('chenqixian@stu') != None)
print(reg_comp.match('chenqixianstu.pku.edu.cn') != None)
print(reg_comp.match('Chen_qi.xian98@stu.pku.edu.cn') != None)

reg_name_comp = re.compile(r'(<([\w\s]+)>)?\s*([\w\d\._]+)@\w+?(\.\w+)+')
print(reg_name_comp.match('<Chris>chenqixian@stu.pku.edu.cn').group(1)[1:-1])
