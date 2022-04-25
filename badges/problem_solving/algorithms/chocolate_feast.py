#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n , c , m):
    chocolates = n // c
    count = 0
    wp = 0

    while chocolates > 0:
        wp += chocolates
        count += chocolates
        chocolates = wp // m
        wp = wp % m

    return count


if __name__ == '__main__':
    result = chocolateFeast(6,2,2)
    print(result)
