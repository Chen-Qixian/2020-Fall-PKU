#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :0-1-multiProcess.py
@Description  :多进程
@Time         :2020/11/03 23:32:41
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
import os
from multiprocessing import Process


def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('Process (%s)' % os.getpid())
    # 创建一个子进程，执行读目标函数为target，传入参数为args
    p = Process(target=run_proc, args=('test',))
    print('Child process will start...')
    p.start()  # 启动子进程
    p.join()  # 进程间同步，子进程结束后继续运行
    print('Child process end...')
