#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :1-unittest.py
@Description  :单元测试
@Time         :2020/10/26 20:08:42
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
# 测试驱动开发 TDD -> 单元测试
# 意义：每次代码修改，需要重新运行一遍单元测试
# 引用unittest包，继承自unittest.TestCase类
import unittest
from testobj import Student


# 单元测试实际上有若干assert语句组成
class TestStudent(unittest.TestCase):
    # setUp tearDown两个方法会分别在每个测试方法前后被调用
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    # 所有单元测试用例都以test开头，否则不会执行测试
    def test_80_to_100(self):
        s1 = Student('Adam', 100)
        s2 = Student('Bar', 80)
        s3 = Student('Chris', 99)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')
        self.assertEqual(s3.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Adam', 79)
        s2 = Student('Bar', 60)
        s3 = Student('Chris', 71)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')
        self.assertEqual(s3.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Adam', 0)
        s2 = Student('Bar', 59)
        s3 = Student('Chris', 10)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')
        self.assertEqual(s3.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Adam', -1)
        s2 = Student('Bar', 101)
        s3 = Student('Chris', 'a')
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()
        with self.assertRaises(TypeError):
            s3.get_grade()


# 运行单元测试两种方法
# 1. 在 __main__中运行 unittest.main()
if __name__ == '__main__':
    unittest.main()
# 2. 在命令行运行 $python -m unittest FILENAME.py
