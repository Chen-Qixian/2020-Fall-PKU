#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :0-3-childProcessIO.py
@Description  :子进程输入输出
@Time         :2020/11/04 15:41:02
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
from multiprocessing import Process
import os
import subprocess

# 子进程调用模块，传入list型参数
print('$ nslookup python.org')
r = subprocess.call(['nslookup', 'python.org'])
print('exit code:', r)

# 子进程需要输入，使用communicate
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('exit code:', p.returncode)
