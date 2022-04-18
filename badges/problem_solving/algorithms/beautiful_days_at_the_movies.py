#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def get_reverse(num):
    test_num = 0
    while num > 0:
        remainder = num % 10
        test_num = (test_num * 10) + remainder
        num = num // 10
    return test_num


def beautifulDays(i , j , k):
    count = 0
    for p in range(i , j + 1):
        if abs(p - get_reverse(p)) % k == 0:
            count += 1
    return count


if __name__ == '__main__':
    result = beautifulDays(20 , 23 , 6)
    print(result)
