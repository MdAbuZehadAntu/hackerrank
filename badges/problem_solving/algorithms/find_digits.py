#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    tmp = n
    count = 0
    while tmp > 0:
        digit = tmp % 10
        tmp = tmp//10
        if digit != 0:
            if n % digit == 0:
                count += 1
        else:
            pass
    return count



if __name__ == '__main__':
    result = findDigits(n)

