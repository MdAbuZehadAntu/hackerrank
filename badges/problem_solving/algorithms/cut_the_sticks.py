#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):

    res = []
    while len(arr) > 0:
        res.append(len(arr))
        min_val = min(arr)
        arr = filter(lambda x: x!= min_val,arr)
        arr = [i - min_val for i in arr]
    return res


if __name__ == '__main__':
    result = cutTheSticks([5,4,4,2,2,8])
    print(result)
