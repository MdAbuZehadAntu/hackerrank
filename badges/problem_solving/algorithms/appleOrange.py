#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s , t , a , b , apples , oranges):
    apples_dist = [x + a for x in apples]
    oranges_dist = [x + b for x in oranges]
    apple_count = 0
    orange_count = 0

    for _ in apples_dist:
        if s <= _ <= t:
            apple_count += 1
    for _ in oranges_dist:
        if s <= _ <= t:
            orange_count += 1
    print(apple_count)
    print(orange_count)


if __name__ == '__main__':
    countApplesAndOranges(7 , 10 , 4 , 12 , [2 , 3, - 4] , [3 , -2 , -4])
