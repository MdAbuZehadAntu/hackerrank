#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p , d , m , s):
    # Return the number of games you can buy
    bought = 0
    sum = 0
    while True:
        # print(sum,bought)
        if sum >= s:
            break
        else:
            if p > m:
                sum += p
                p -= d
                if sum <= s:
                    bought += 1
            else:
                if sum < s:
                    p = m
                    sum += p
                    if sum <= s:
                        bought += 1

    return bought


if __name__ == '__main__':
    answer = howManyGames(16,2,1,9981)
    print(answer)
