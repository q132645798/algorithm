#!/usr/bin/env python
# encoding: utf8

import time

def DnC(ary):
    if(len(ary) <= 3): return sorted(ary)
    d = (len(ary)+1) / 3
    sal = DnC(ary[:d])
    sam = DnC(ary[d:d*2])
    sar = DnC(ary[d*2:])
    tmp = []
    while(not(len(sal) == 0 and len(sam) == 0 and len(sar) == 0)):
        ta = [0]
        if(len(sal) != 0 and len(sam) != 0 and len(sar) != 0):
            ta = sal if(sal[0] <= sam[0] and sal[0] <= sar[0]) \
                    else sam if(sam[0] <= sal[0] and sam[0] <= sar[0]) else sar
        elif(len(sal) == 0 and len(sam) != 0 and len(sar) != 0):
            ta = sam if(sam[0] <= sar[0]) else sar
        elif(len(sam) == 0 and len(sal) != 0 and len(sar) != 0):
            ta = sal if(sal[0] <= sar[0]) else sar
        elif(len(sar) == 0 and len(sal) != 0 and len(sam) != 0):
            ta = sal if(sal[0] <= sam[0]) else sam
        tmp.append(ta[0])
        ta.pop(0)
        ta = sal if(len(sal) != 0 and len(sam) == 0 and len(sar) == 0) else \
                sam if(len(sam) != 0 and len(sal) == 0 and len(sar) == 0) else \
                sar if(len(sar) != 0 and len(sal) == 0 and len(sam) == 0) else []
        for i in ta:
            tmp.append(i)
            ta.pop(0)
    return tmp

a = [120, 3, 1, 1321, 40, 2, 5 , 10, 1, 212, 23126, 312321, 5241, -123, -131]
print('Array length is {}'.format(len(a)))
print DnC(a)
