#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

def saveThePrisoner(n , m , s):
    if m > n:
        res = (m % n + (s - 1)) % n
        if res == 0:
            return n
        else:
            return res
    else:

        res = (m + (s - 1)) % n
        if res == 0:
            return n
        else:
            return res


if __name__ == '__main__':
    result = saveThePrisoner(5,2,1)
    print(result)
