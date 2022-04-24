#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
from operator import itemgetter


def minimumDistances(a):
    f_dict = dict()
    if len(set(item for item in a if a.count(item) > 1)) == 0:
        return -1
    for item in a:
        if item not in f_dict.keys():
            f_dict[item] = {"idx" : a.index(item),'count' : 1,'dist' : float('inf')}
            a[a.index(item)] = 'x'
        else:
            f_dict[item]['count'] += 1
            if f_dict[item]['dist'] >= (a.index(item) - f_dict[item]['idx']):
                f_dict[item]['dist'] = (a.index(item) - f_dict[item]['idx'])
                f_dict[item]['idx'] = a.index(item)
            a[a.index(item)] = 'x'
    print(f_dict)
    minimum = float('inf')

    for key,val in f_dict.items():
        if val['count'] > 1 and minimum > val['dist']:
            minimum = val['dist']
    return minimum






if __name__ == '__main__':
    # l = open('test_case' , 'r')
    # x = [int(i) for i in l.read().split()]
    result = minimumDistances([7,1,3,4,1,7])
    print(result)
