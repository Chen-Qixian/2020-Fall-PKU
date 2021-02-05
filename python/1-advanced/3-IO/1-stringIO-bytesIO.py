#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :0-stringIO-bytesIO.py
@Description  :stringIO与bytesIO
@Time         :2020/11/03 16:13:49
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
from io import StringIO, BytesIO

# 写字符串以及获取值
s = StringIO()
s.write('hello')
s.write(' ')
s.write('world!')
print(s.getvalue())
# 像文件一样读写:两者类似，但是需要为对象赋初值
s1 = StringIO('Hi!\nHello!\nBye!')
while True:
    st = s1.readline()
    if st == '':
        break
    print(st.strip())
# 对二进制读写
b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue())
