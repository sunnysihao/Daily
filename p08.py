# -*- coding = utf-8 -*-
while True:
    try:
        a, b = input(), input()
        if len(a) > len(b):
            a, b = b, a
        res = ''
        for i in range(0, len(a)):
            for j in range(i+1, len(a)):
                if a[i:j+1] in b and len(a[i:j+1]) > len(res):
                        res = a[i:j+1]
            print(res)
    except:
        break



