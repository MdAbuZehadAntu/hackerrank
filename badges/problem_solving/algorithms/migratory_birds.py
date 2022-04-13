#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    temp_dict = dict()
    for item in arr:
        if item not in temp_dict.keys():
            temp_dict[item] = 1
        else:
            temp_dict[item] += 1

    max_sighted = max(temp_dict.values())
    min_type = float('inf')
    for key, val in temp_dict.items():
        if val == max_sighted and key < min_type:
            min_type = key
    return min_type


if __name__ == '__main__':
    result = migratoryBirds([1 , 1 , 2 , 2 , 3])
    print(result)
