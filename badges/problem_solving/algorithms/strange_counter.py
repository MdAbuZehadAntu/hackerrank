import math
import os
import random
import re
import sys


#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    st = 1
    x = 1
    while True:
        if st <= t <= (st + 3 * x) - 1:
            break
        else:
            st = (st + 3 * x)
        x *= 2

    v = 2 * st - t + 2
    return v


if __name__ == '__main__':
    result = strangeCounter(4)
    print(result)
