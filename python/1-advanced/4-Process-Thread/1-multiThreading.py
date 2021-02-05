#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :1-multiThreading.py
@Description  :多线程
@Time         :2020/11/04 16:19:38
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
# 与多进程类似，启动一个线程就是向Threading对象中传入函数，start启动
import time
import threading


def loop():
    curThreadName = threading.current_thread().name
    print('thread %s is running...' % curThreadName)
    n = 0
    while n < 3:
        n = n + 1
        print('Thread %s >>> %d' % (curThreadName, n))
        time.sleep(0.5)
    print('thread %s has ended...' % curThreadName)


# 与进程操作非常类似
print('thread %s is running...' % threading.current_thread().name)
# 主线程默认名为MainThread，其他线程不命名则默认自动编号
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s has ended...' % threading.current_thread().name)

# 多线程一定要加锁，否则多个线程修改共享数据时会引发一致性错误
# 例子：多次存取后，balance应保持不变，但执行次数足够多，就不能保持不变
balance = 0


def change(n):
    global balance
    balance += n
    balance -= n


def run(n):
    for i in range(2000000):
        change(n)


t1 = threading.Thread(target=run, args=(5,))
t2 = threading.Thread(target=run, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
# 期望是0，但是由于线程执行顺序原因，对共享数据的访问不能保证是一致的
# 在执行时，线程交替执行，可能打断线程，导致共享对象被非法修改
print(balance)


# 使用锁Lock()对象保证一段原子操作不会被打断，加锁后一定要释放锁
# 好处：保证了数据一致性  坏处：降低了并发度，可能导致死锁
balance = 0
lock = threading.Lock()  # 创建一个锁对象


def locked_run(n):
    for i in range(2000000):
        lock.acquire()
        try:
            # 加锁执行不被打断，但是降低了并发程度
            change(n)
        finally:
            # 使用try finally语句保证锁可以释放
            lock.release()


print(balance)
