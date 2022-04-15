# -*- coding = utf-8 -*-
# import numpy as np
#
# for x in np.arange(0, 250,step = 25):
#     print(int(x))
count = 0
for i in range(0,101):
    for j in range(0,101):
        k = 100 - i - j
        if k >= 0 and 5*i + j + 0.5*k == 100:
            count+=1
            print(i, end="\t")
            print(j, end="\t")
            print(k)
print(count)