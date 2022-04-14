#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n , ar):
    sock_color = dict()
    for sock in ar:
        if sock in sock_color:
            sock_color[sock] += 1
        else:
            sock_color[sock] = 1
    return sum([x // 2 for x in sock_color.values()])


if __name__ == '__main__':
    result = sockMerchant(7 , [1 , 2 , 1 , 2 , 1 , 3 , 2])
    print(result)
