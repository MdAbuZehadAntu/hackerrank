#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    val = 0
    for item in A:
        item.insert(0 , 0)
        item.append(0)

    A.insert(0 , [0] * len(A[0]))
    A.append([0] * len(A[0]))
    for i in range(1 , len(A) - 1):
        for j in range(1 , len(A[0]) - 1):
            total = A[i][j] * 6
            left = A[i][j] if A[i][j] < A[i][j - 1] else A[i][j - 1]
            right = A[i][j] if A[i][j] < A[i][j + 1] else A[i][j + 1]
            up = A[i][j] if A[i][j] < A[i - 1][j] else A[i - 1][j]
            down = A[i][j] if A[i][j] < A[i + 1][j] else A[i + 1][j]
            val += total - ((A[i][j] - 1) * 2 + left + right + up + down)

    return val


if __name__ == '__main__':
    result = surfaceArea([[1 , 3 , 4] , [2 , 2 , 3] , [1 , 2 , 4]])
    print(result)
