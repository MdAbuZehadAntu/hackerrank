#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    if n == 0:
        return 1
    else:
        x = 1
        for h in range(1 , n+1):
            if h % 2 != 0:
                x = x * 2
            else:
                x += 1
        return x


if __name__ == '__main__':
    result = utopianTree(5)
    print(result)
