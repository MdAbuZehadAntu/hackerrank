#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    res = list()
    for i in range(1 , len(p) + 1):
        res.append(p.index(p.index(i) + 1) + 1)
    return res


if __name__ == '__main__':
    result = permutationEquation([5 , 2 , 1 , 3 , 4])
    print(result)
