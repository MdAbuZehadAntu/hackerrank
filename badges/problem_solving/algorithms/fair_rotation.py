#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    count = 0
    for i in range(len(B)):
        if B[i] % 2 == 0:
            pass
        else:
            try:
                B[i] += 1
                B[i+1] += 1
                count += 2
            except:
                return 'NO'
    return str(count)


if __name__ == '__main__':
    result = fairRations([2, 3, 4, 5, 6] )
    print(result)
