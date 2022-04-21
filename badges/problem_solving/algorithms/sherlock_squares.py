#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#
import math


def squares(a , b):
    if math.sqrt(a) % 1 == 0:
        return 1 + int(math.sqrt(b)) - int(math.sqrt(a))
    else:
        return int(math.sqrt(b)) - int(math.sqrt(a))


if __name__ == '__main__':
    result = squares(24 , 49)
    print(result)
