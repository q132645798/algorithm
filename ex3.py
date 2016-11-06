#!/usr/bin/env python
# encoding: utf8

import time
import random
                
def DnC(ary):
    if(len(ary) <= 3): return sorted(ary)
    d = (len(ary)+1) / 3
    sal, sam, sar, tmp = DnC(ary[:d]), DnC(ary[d:d*2]), DnC(ary[d*2:]), []
    while(not(len(sal) == 0 and len(sam) == 0 and len(sar) == 0)):
        ta = []
        if(len(sal) != 0 and len(sam) != 0 and len(sar) != 0):
            ta = sal if(sal[0] <= sam[0] and sal[0] <= sar[0]) \
                    else sam if(sam[0] <= sal[0] and sam[0] <= sar[0]) else sar
        elif(len(sal) == 0 and len(sam) != 0 and len(sar) != 0):
            ta = sam if(sam[0] <= sar[0]) else sar
        elif(len(sam) == 0 and len(sal) != 0 and len(sar) != 0):
            ta = sal if(sal[0] <= sar[0]) else sar
        elif(len(sar) == 0 and len(sal) != 0 and len(sam) != 0):
            ta = sal if(sal[0] <= sam[0]) else sam
        if(len(ta) != 0):
            tmp.append(ta[0])
            ta.pop(0)
        ta = sal if(len(sal) != 0 and len(sam) == 0 and len(sar) == 0) else \
                sam if(len(sam) != 0 and len(sal) == 0 and len(sar) == 0) else \
                sar if(len(sar) != 0 and len(sal) == 0 and len(sam) == 0) else []
        for i in sorted(ta):
            tmp.append(i)
            ta.pop(0)
    return tmp

a = []
for i in range(1, 101):
    a.append(random.randint(1, 10000))
print('[*] Array is:')
print(a)
print('[*] Array length is {}'.format(len(a)))
print('[*] Sorted')
print DnC(a)
