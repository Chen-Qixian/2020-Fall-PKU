#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :testobj.py
@Description  :单元测试的目标文件
@Time         :2020/10/26 20:11:30
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if not isinstance(self.score, int):
            raise TypeError('Invalid Type of score')
        if self.score < 0 or self.score > 100:
            raise ValueError('Invalid Value %d' % self.score)
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        return 'C'
