# -*- coding = utf-8 -*-
'''自定义装饰器'''
import time

def coust_time(func):
    def impro(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(f"花费的时间为{end - start}")
        return ret
    return impro

@coust_time
def bianli(y=5):
    for x in range(y):
        print(x)


if __name__ == "__main__":
    bianli(y=20)
