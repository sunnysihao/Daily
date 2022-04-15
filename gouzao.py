# -*- coding = utf-8 -*-
# 斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13
# 特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和。
class Fib():
    def __init__(self):
        pass
    def __call__(self,num):
        a,b = 0,1;
        self.l=[]

        for i in range (num):
            self.l.append(a)
            a,b= b,a+b
        return self.l
    def __str__(self):
        return str(self.l)
    __rept__=__str__

f = Fib()
print(f(10))
