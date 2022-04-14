#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    check_dict = dict()
    for item_1 in list(set(a)):
        for item_2 in sorted(a):
            if abs(item_1 - item_2) <= 1:
                if item_1 not in check_dict.keys():
                    check_dict[item_1] = [item_2]
                else:
                    if max([(item_2-i) for i in check_dict[item_1]]) <= 1:
                        check_dict[item_1].append(item_2)
    return max([len(item) for item in check_dict.values()])


if __name__ == '__main__':
    result = pickingNumbers([4,6,5,3,3,1])
    print(result)
