#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    shared = 5
    result = 0
    for i in range(1 , n + 1):
        if i != 1:
            shared = liked * 3
        liked = shared // 2
        result += liked

    return result


if __name__ == '__main__':
    result = viralAdvertising(5)
    print(result)
