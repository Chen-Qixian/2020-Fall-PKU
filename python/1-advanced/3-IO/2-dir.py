#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :2-dir.py
@Description  :操作文件 目录
@Time         :2020/11/03 16:31:18
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
import os
# OS名
print(os.name)
print(os.uname())
# OS PATH环境变量
print(os.environ)
print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))
# 操作文件和目录
print(os.path.abspath('.'))
# 不要直接字符串拼接
print(os.path.join('/Users/chenqixian/Desktop/python/1-advanced/3-IO', 'test'))
# 创建目录
os.mkdir('/Users/chenqixian/Desktop/python/1-advanced/3-IO/dir')
# 删除目录
# os.rmdir('/Users/chenqixian/Desktop/python/1-advanced/3-IO/dir')
# 同理不要直接拆分字符串，而使用路径操作方法
print(os.path.split('/Users/chenqixian/Desktop/python/1-advanced/3-IO/file.txt'))
# 拆分扩展名
print(os.path.splitext('/Users/chenqixian/Desktop/python/1-advanced/3-IO/file.txt'))
# 重命名
# os.rename('/Users/chenqixian/Desktop/python/1-advanced/3-IO/file.py',
#   '/Users/chenqixian/Desktop/python/1-advanced/3-IO/file.txt')

# 过滤当前目录下所有的目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出所有的 py文件
print([x for x in os.listdir('.') if os.path.isfile(
    x) and os.path.splitext(x)[1] == '.py'])
