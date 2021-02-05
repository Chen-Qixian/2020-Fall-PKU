#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :3-pickle.py
@Description  :序列化
@Time         :2020/11/03 17:07:38
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
# 核心： load 和 dump 操作
import pickle
import json

# 序列化为二进制
d = dict(name='ChrisChen', age=18, score=100)
print(pickle.dumps(d))
with open('/Users/chenqixian/Desktop/python/1-advanced/3-IO/output.txt', 'wb') as wf:
    pickle.dump(d, wf)

# 二进制反序列化
with open('/Users/chenqixian/Desktop/python/1-advanced/3-IO/output.txt', 'rb') as rf:
    rd = pickle.load(rf)
    print(rd)

# 序列化为JSON
json_str = json.dumps(d)
print(json_str)
# JSON反序列化
print(json.loads(json_str))


# 类的反序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Chris Chen', 18, 'A+')
# 使用__dict__获取class对象中的成员变量dict
stu_json = json.dumps(s, default=lambda obj: obj.__dict__)
print(json.loads(stu_json))


# 也可以转换回Student对象
def json2stu(d):
    return Student(d['name'], d['age'], d['score'])


print(json.loads(stu_json, object_hook=json2stu))

# 确保转换成ascii码
obj = dict(name='小明abc', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
