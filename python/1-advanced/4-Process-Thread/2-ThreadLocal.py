#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :2-ThreadLocal.py
@Description  :处理线程私有数据
@Time         :2020/11/04 16:52:23
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
# 尽量不用全局变量，以免被多次修改，使用局部数据，使不同线程之间互不干扰
import threading

# 创建ThreadLocal对象
local_school = threading.local()


def process_student():
    # 访问该线程的局部数据
    std = local_school.student
    print('hello, %s (%s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 给当前thread的局部数据赋值
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',))
t2 = threading.Thread(target=process_thread, args=('Bob',))
t1.start()
t2.start()
t1.join()
t2.join()
