# -*- coding = utf-8 -*-
'''单例模式实现方法'''
# 使用装饰器

def singl(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
            return instances[cls]
    return wrapper
@singl
def func(*args):
    pass

f1 = func(1)
f2 = func(2)
print(f1 is f2)

#使用基类
class Single(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance