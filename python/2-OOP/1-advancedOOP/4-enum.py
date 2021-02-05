#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :4-enum.py
@Description  :枚举类型
@Time         :2020/10/26 16:46:55
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
from enum import Enum, unique

# 默认枚举值从1开始编号依次递增
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
                       'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 使用Month.Jan来引用一个常量
# 使用Month.__members__来枚举成员
# 使用items()方法遍历dict中的对象
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# 使用unique检查重复值
@unique
class Weekday(Enum):
    # Sun的value被设定为0
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Wed'])
print(Weekday.Thu.value)


# 使用枚举类型可以避免无意义的字符串使用
@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


bart = Student('Bart', Gender.Male)
print(bart.gender)
