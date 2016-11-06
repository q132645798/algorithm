#!/usr/bin/env python
# encoding: utf8

import time

def DnC(ary):
    if(len(ary) <= 3):
        return sorted(ary)
    d = (len(ary)+1) / 3
    al = ary[:d]
    am = ary[d:d*2]
    ar = ary[d*2:]
    sal = DnC(al)
    sam = DnC(am)
    sar = DnC(ar)
    print 'merge', sal, sam, sar
    tmp = []
    while True:
        if(len(sal) != 0 and len(sam) != 0 and len(sar) != 0):
            if(sal[0] <= sam[0] and sal[0] <= sar[0]):
                tmp.append(sal[0])
                sal.pop(0)
            elif(sam[0] <= sal[0] and sam[0] <= sar[0]):
                tmp.append(sam[0])
                sam.pop(0)
            else:
                tmp.append(sar[0])
                sar.pop(0)
        if(len(sal) == 0 and len(sam) != 0 and len(sar) != 0):
            if(sam[0] <= sar[0]):
                tmp.append(sam[0])
                sam.pop(0)
            else:
                tmp.append(sar[0])
                sar.pop(0)
        if(len(sam) == 0 and len(sal) != 0 and len(sar) != 0):
            if(sal[0] <= sar[0]):
                tmp.append(sal[0])
                sal.pop(0)
            else:
                tmp.append(sar[0])
                sar.pop(0)
        if(len(sar) == 0 and len(sal) != 0 and len(sam) != 0):
            if(sal[0] <= sam[0]):
                tmp.append(sal[0])
                sal.pop(0)
            else:
                tmp.append(sam[0])
                sam.pop(0)
        if(len(sal) != 0 and len(sam) == 0 and len(sar) == 0):
            for i in sal:
                tmp.append(i)
            break
        if(len(sam) != 0 and len(sal) == 0 and len(sar) == 0):
            for i in sam:
                tmp.append(i)
            break
        if(len(sar) != 0 and len(sal) == 0 and len(sam) == 0):
            for i in sar:
                tmp.append(i)
            break
    return tmp

a = [120, 3, 1, 1321, 40, 2, 5 , 10, 1, 212, 23126, 312321, 5241, -123, -131]
print('Array length is {}'.format(len(a)))
print DnC(a)
