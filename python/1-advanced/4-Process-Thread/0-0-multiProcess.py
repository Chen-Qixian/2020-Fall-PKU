#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :0-0-multiProcess.py
@Description  :多进程
@Time         :2020/11/03 22:55:35
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
# 总结：
# 1. os.fork()方法可以创建子进程，使用多进程
# 2. multiprocessing 中有 Process(target=, args=)创建子进程，p.start(),p.join(),p.terminate()
# 3. multiprocessing 中有 Pool(num)创建容量size的进程池，使用p.apply_async(target, args)同时启动多进程
# 4. Queue()用于实现进程间通信，q.put(), q.get()
from multiprocessing import Process
import os

# fork系统调用
print('Process (%s) start...' % os.getpid())
# 普通的系统调用，调用一次返回一次；fork调用一次返回两次
# 在父子进程分别返回 pid 父进程返回子进程pid，子进程返回0
pid = os.fork()
if pid == 0:
    print('I am a child process (%s) and my parent is %s' %
          (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process %s' % (os.getpid(), pid))

# 应用：Apache服务器由父进程监听端口，每当出现新的http请求，fork子进程处理响应请求
