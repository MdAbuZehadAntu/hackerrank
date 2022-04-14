#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps , path):
    s = 0
    v_check = 0
    v_count = 0
    for i in range(len(path)):
        if path[i] == "D":
            s -= 1
        else:
            s += 1
        if s < 0:
            v_check = 1
        if v_check == 1 and s == 0:
            v_count += 1
            v_check = 0
    return v_count


if __name__ == '__main__':
    result = countingValleys(12 , "DDUUDDUDUUUD")
    print(result)
