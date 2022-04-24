#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d , arr):
    length = len(arr)
    count = 0
    for i in range(length):
        if arr[i] + d in arr and  arr[i] + 2*d in arr:
            count += 1
    return count


if __name__ == '__main__':
    result = beautifulTriplets(3 , [1, 2, 4, 5, 7, 8, 10])
    print(result)
