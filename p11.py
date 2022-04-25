# -*- coding = utf-8 -*-
from functools import reduce
def solution(n):
    res = reduce(lambda x, y:x+y, map(lambda x:x**2, range(1, n)))
    print(res)
solution(10)