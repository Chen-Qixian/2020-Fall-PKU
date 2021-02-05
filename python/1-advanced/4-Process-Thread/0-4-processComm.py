#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :0-4-processComm.py
@Description  :进程间消息通讯
@Time         :2020/11/04 15:53:11
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
# 通过消息队列Queue和管道PIPE
from multiprocessing import Process, Queue
import os
import time
import random


# 写数据程序代码
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据程序代码
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue' % value)


if __name__ == '__main__':
    # 创建一个消息队列
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    # 阻塞直到pw结束
    pw.join()
    # 死循环，需要强行终止
    pr.terminate()
