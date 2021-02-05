#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :0-2-multiProcessPool.py
@Description  :进程池
@Time         :2020/11/04 15:08:10
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %.2f seconds...' % (name, end-start))


if __name__ == '__main__':
    print('Parent process %s' % os.getppid())
    # 进程池设定大小，默认为当前环境CPU核数
    p = Pool(4)
    # 启动批量的子进程执行，根据进程池的大小最多每次有限数量的子进程被启动
    for i in range(6):
        # args传入参数，是一个tuple，注意只有1个元素的tuple写法
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    # 等待所有子进程执行完毕
    p.join()
    print('All subprocesses done.')
