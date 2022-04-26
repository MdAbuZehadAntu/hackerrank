#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n , c):
    c = sorted(c)
    max_dist = c[0]
    for i in range(1 , len(c)):
        cur_dist = (c[i] - c[i - 1]) // 2 + 1
        max_dist = cur_dist if cur_dist > max_dist else max_dist
    max_dist = max_dist if max_dist > (n - 1) - c[len(c) - 1] else (n - 1) - c[len(c) - 1]
    return max_dist


if __name__ == '__main__':
    result = flatlandSpaceStations(95 ,
                                   [68 , 81 , 46 , 54 , 30 , 11 , 19 , 23 , 22 ,
                                    12 , 38 , 91 , 48 , 75 , 26 , 86 , 29 ,
                                    83 , 62])
    print(result)
