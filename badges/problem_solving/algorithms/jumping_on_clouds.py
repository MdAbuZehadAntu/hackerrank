#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c , k):
    e = 100
    i = 0
    l = len(c)
    while i < l:
        i = (i + k) % l
        if c[i] == 1:
            e -= 3
        else:
            e -= 1
        if i == 0:
            break
    return e


if __name__ == '__main__':
    result = jumpingOnClouds([1 ,1, 1, 0, 1, 1, 0, 0, 0, 0] , 3)
    print(result)
