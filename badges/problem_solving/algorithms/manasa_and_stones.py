#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n , a , b):
    res = []
    h = min(a,b) * (n - 1)
    gap = abs(b-a)
    res.append(h)
    if gap == 0:
        return res
    for i in range(1,n):
        res.append(h+i*gap)
    return res


if __name__ == '__main__':
    result = stones(5 , 58 , 59)
    print(result)
