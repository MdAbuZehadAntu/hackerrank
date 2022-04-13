#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s , d , m):
    count = 0
    for i in range(len(s)):
        temp_arr = s[i:i + m]
        if sum(temp_arr) == d:
            count += 1
    return count


if __name__ == '__main__':
    result = birthday([2,2,1,3,2] , 4 , 2)
    print(result)
