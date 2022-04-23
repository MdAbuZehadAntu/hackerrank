#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p , q):
    res = list()
    for i in range(p , q + 1):
        if i == 1:
            res.append(i)
        else:
            if len(str(int(math.pow(i , 2)))) >= 2:
                right = str(int(math.pow(i , 2)))[-(len(str(i))):]
                left = str(int(math.pow(i , 2)))[:-(len(str(i)))]
                if int(left) + int(right) == i:
                    res.append(i)

    if len(res) == 0:
        print("INVALID RANGE")
    else:
        for item in res:
            print(item,end=' ')


if __name__ == '__main__':
    kaprekarNumbers(1 , 100)
