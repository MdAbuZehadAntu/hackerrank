#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k , height):
    max_height = max(height)
    if max_height - k > 0:
        return max_height - k
    else:
        return 0


if __name__ == '__main__':
    result = hurdleRace(4 , [1 , 6 , 3 , 5 , 2])
    print(result)
