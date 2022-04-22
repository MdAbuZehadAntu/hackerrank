#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

def taumBday(b , w , bc , wc , z):
    if bc + z < wc:
        wc = (bc + z)
    elif wc + z < bc:
        bc = (wc + z)
    cost = b * bc + w * wc
    return cost


if __name__ == '__main__':
    result = taumBday(10 , 10 , 1 , 1 , 1)
    print(result)
