#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n , k):
    if k == 0:
        return [i for i in range(1 , n + 1)]
    elif (n % (2 * k)) != 0:
        return [-1]
    else:
        res = [None] * (n + 1)
        for i in range(1 , n + 1):
            if res[i] is None:
                res[i] = i + k
                res[i + k] = i
        return res[1:]


if __name__ == '__main__':
    result = absolutePermutation(4 , 2)
    print(result)
