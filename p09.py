# -*- coding = utf-8 -*-
n = int(input())
dict = {}
while True:
    try:
        line = input()
        t = line.split()
        index = int(t[0])
        value = int(t[1])
        if index in dict:
            dict[index] += value
        else:
            dict[index] = value
    except:
        break
for k, v in sorted(dict.items()):
    print(f"{k} {v}")