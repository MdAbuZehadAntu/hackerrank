#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s , n):
    tmp = s
    n_a = s.count('a')
    if (n / len(s)) % 1 == 0:
         n_a = n_a * (n // len(s))
    else:
        n_a = n_a * (n // len(s)) + tmp[:n % len(tmp)].count('a')

    return n_a


if __name__ == '__main__':
    result = repeatedString('a' , 1000000000000)
    print(result)
