# -*- coding = utf-8 -*-

def deco(*args):
    def canshu(func):
        def ipv():
            print(*args)
            func()
        return ipv
    return canshu



@deco(2, 3, 'opo')
def test_deco():
    print("abc")
test_deco()