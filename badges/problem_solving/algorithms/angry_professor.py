#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'angryProfessor' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY a
#

def angryProfessor(k , a):
    on_time = [time for time in a if time <= 0]
    if len(on_time) >= k:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    result = angryProfessor(3 , [-1 , -3 , 4 , 2])
    print(result)
