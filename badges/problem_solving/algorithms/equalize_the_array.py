#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from statistics import mode


def equalizeArray(arr):
    mode_val = mode(arr)
    count = 0
    for i in arr:
        if i != mode_val:
            count += 1
    return count


if __name__ == '__main__':
    result = equalizeArray([1 , 2 , 2 , 3])
    print(result)
