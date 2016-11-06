#!/usr/bin/env python
# encoding: utf8


def getLargest(ary):
    lm = max(ary[:len(ary)/2+1])
    rm = max(ary[len(ary)/2+1:])
    return lm if(lm > rm) else rm

ary = [10, 2, 3, 4, 5]
print getLargest(ary)
