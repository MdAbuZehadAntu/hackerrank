#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    min_max = [float('-inf')]*2
    temp_result = [0] * 2

    for i in range(len(scores)):
        if i == 0:
            min_max[0] = scores[i]
            min_max[1] = scores[i]
        else:
            if scores[i] > min_max[0]:
                temp_result[0] += 1
                min_max[0] = scores[i]
            if scores[i] < min_max[1]:
                temp_result[1] += 1
                min_max[1] = scores[i]
    return temp_result


if __name__ == '__main__':
    result = breakingRecords([10 , 5 , 20 , 20 , 4 , 5 , 2 , 25 , 1])
    print(result)
