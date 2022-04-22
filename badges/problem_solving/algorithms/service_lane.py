#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#

def serviceLane(n , cases , width):
    res = []
    for item in cases:
        res.append(min(width[item[0]:item[1] + 1]))
    return res


if __name__ == '__main__':
    result = serviceLane(8 , [[0 , 3] , [4 , 6] , [6 , 7] , [3 , 5] , [0 , 7]] , [2 , 3 , 1 , 2 , 3 , 2 , 3 , 3])
    print(result)
