#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n , p):
    # Write your code here
    # pages = [i for i in range(1,n+1)]
    pages = [(i - 1 , i) for i in range(1 , n + 1 , 2)]
    if n not in pages[-1]:
        pages.append((n , n + 1))
    l_count = 0
    s_count = 0
    # print(pages)
    if n == p:
        return 0
    elif p == 0 or p == 1:
        return 0
    else:
        for item in pages[::-1]:
            # print(item)

            if p in item:
                break
            l_count += 1
        for item in pages:

            if p in item:
                break
            s_count += 1
        if l_count >= s_count:
            return s_count
        else:
            return l_count


if __name__ == '__main__':
    result = pageCount(5 , 3)
    print(result)
