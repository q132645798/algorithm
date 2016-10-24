#!/usr/bin/env python3
# encoding: utf8

"""
Author: Linwz
Question:
    Write an algorithm that finds both the smallest and largest numbers in a list.
    Try to find a method that does at most 1.5n comparisons of array items.
"""

import sys 

#finds smaillest and largest numbers in a list
def findLS(items):
    l = s = items[0]
    try:
        for i in range(0, len(items), 2):
            if(i + 1 >= len(items)):
                if(l < items[i]): l = items[i]
                if(s > items[i]): s = items[i]
                break
            if(items[i] > items[i+1]):
                if(l < items[i]): l = items[i]
                if(s > items[i+1]): s = items[i+1]
            else:
                if(l < items[i+1]): l = items[i+1]
                if(s > items[i]): s = items[i]
    except TypeError as e:
        print('Please input a numbers\'s array! Error: {}'.format(e))
        sys.exit(0)
    return l, s,

data = [60, 10, 6, 212, 612312, 4, 1212, 123123,123213,3213]
data = [312, 143, 4321321]
#data = [1]
#data = [1, 'Q___Q']
print('Array data: {}, len is {}'.format(data, len(data)))
print('Must at most {} comparisons'.format(int(len(data) * 1.5)))
l, s = findLS(data)
print('-' * 20)
print('Largest: {}, Smaillest: {}'.format(l, s))
