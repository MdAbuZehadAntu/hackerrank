#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    jumps = 0
    i = 0

    while i < len(c) - 2:
        # print(i)
        if c[i + 2] != 1:
            jumps += 1
            i += 2
        else:
            jumps += 1
            i += 1
    for j in range(i , len(c)):

        if j == len(c) - 1:
            break
        if c[j + 1] == 0:
            jumps += 1

    return jumps


if __name__ == '__main__':
    result = jumpingOnClouds([0 , 0 , 0 , 1 , 0 , 0])
    print(result)
