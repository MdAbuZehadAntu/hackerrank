
# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#
def rotate( l, n):
    return l[n:] + l[:n]

def circularArrayRotation( a, k, queries):
    k %= len(a)
    a[k:] , a[:k] = a[:-k] , a[-k:]
    res = []
    for i in queries:
        res.append(a[i])
    return res


if __name__ == '__main__':
    result = circularArrayRotation([3 , 4 , 5] , 2 , [1 , 2])

    print(result)
