#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k , s):
    rem = [0] * k
    for item in s:
        rem[item % k] += 1
    res = min(rem[0] , 1)
    for i in range(1 , (k // 2) + 1):
        if i != k - i:
            res += max(rem[i] , rem[k - i])
        else:
            res += min(rem[i] , 1)
    return res


if __name__ == '__main__':
    result = nonDivisibleSubset(4 , [19 , 10 , 12 , 10 , 24 , 25 , 22])
    print(result)
