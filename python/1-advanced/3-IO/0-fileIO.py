#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :0-fileIO.py
@Description  :文件读写
@Time         :2020/11/03 16:20:05
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
# 最优写法：包含try异常处理、close
# read不加限制将读取整个文件内容
# 可以使用read(size)限制读取的size
# 使用readline()可以方便读取配置文件 按行读取
with open('/Users/chenqixian/Desktop/python/1-advanced/3-IO/file.txt', 'r') as f:
    print(f.read())

# 读非规范编码文件
# with open('file/to/path/gbk.txt', 'r', encoding='gbk', errors='ignore') as f:

# 读二进制文件:如图片
# with open('file/to/path/pic.jpg', 'rb') as f:

# 写文件:二进制为'wb'
with open('/Users/chenqixian/Desktop/python/1-advanced/3-IO/write.txt', 'w') as f2:
    f2.write('Hello world!\n Write')
