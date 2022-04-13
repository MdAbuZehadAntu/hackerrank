#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a , b):
    total = 0
    for i in range(a[-1] , b[0] + 1):
        if len([x for x in a if i % x == 0]) == len(a) and len([x for x in b if x % i == 0]) == len(b):
            total += 1
    return total


if __name__ == '__main__':
    total = getTotalX([2 , 4] , [16,32,96])
    print(total)
