# -*- coding = utf-8 -*-
def hanoi(n, a, b, c):
    if n>0:
        hanoi(n-1, a, c, b)
        print("moving from %s to %s" % (a, c))
        hanoi(n-1, b, a, c)
hanoi(10, "A", "B", "C")
