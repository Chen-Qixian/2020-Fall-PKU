#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File         :3-type.py
@Description  :获取对象信息
@Time         :2020/10/22 23:20:17
@Author       :Chen.Qixian
@Email        :chenqixian@stu.pku.edu.cn
'''
import types


def fn():
    pass


class Animal(object):
    pass


# type类型判断
a = Animal()
print(type(123))
print(type('123'))
print(type(123) == int)
print(type(123) == type('123'))
print(type('123') == str)
print(type(abs))
print(type(a))
print(type(None))

# types类型判断
print(type(abs) == types.BuiltinMethodType)
print(type(fn) == types.FunctionType)
print(type(lambda x: x+1) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 对于class等具有复杂继承关系使用isinstance
# 优先使用isinstance将子类型也判断完毕
print('')
print(isinstance(b'a', bytes))
# 判断是否是list或tuple中的某一种
print(isinstance([1, 2, 3], (list, tuple)))

# 获取一个对象中所有的属性和方法 dir ：返回一个list
# 如：获取一个str对象的属性和方法
print(dir('ABC'))
print(len('ABC'))
# 等价写法
print('ABC'.__len__())


# 定义自己的类中的len
class MyObj(object):
    def __init__(self):
        self.x = 1
        self.y = 2

    def __len__(self):
        return 100


# 等价于 MyObj().__len__()
print(len(MyObj()))


# 列出属性和方法后，使用hasattr / getattr/ setattr操作这些属性
obj = MyObj()
print(hasattr(obj, 'x'))
print(getattr(obj, 'x'))
print(getattr(obj, 'y'))
print(hasattr(obj, 'z'))
setattr(obj, 'z', 100)
print(hasattr(obj, 'z'))
print(getattr(obj, 'z'))
# 常用的组合
for i in range(3):
    if hasattr(obj, 'w') == False:
        print('set success!')
        setattr(obj, 'w', 5)
    else:
        print(getattr(obj, 'w'))

# 若获取失败返回默认值
print(getattr(obj, 'a', 404))


# 【注意】只有在不知道对象内部信息的时候才会getattr，否则直接获取属性即可
# 例如从fp对象中读图像
# def getImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None
# 由于“鸭子类型”只要read是一个合法的方法就可以读取流中的数据
