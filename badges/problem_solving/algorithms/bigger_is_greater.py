#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    w = list(w)
    wid = len(w)
    pivot = None
    for i in range(1 , wid):
        if w[wid - i] > w[wid - i - 1]:
            pivot = w[wid - i - 1]
            break
    if pivot is None:
        return 'no answer'
    sub_wid = len(w[wid - i:])
    j = wid - 1
    while j >= wid - i:
        if w[j] > pivot:
            break
        j -= 1
    replacement_index = j
    w[wid - i - 1] , w[replacement_index] = w[replacement_index] , w[wid - i - 1]
    w = w[:wid - i] + sorted(w[wid - i:])
    w = ''.join(w)
    return w


if __name__ == '__main__':
    result = biggerIsGreater('ecdigf')
    print(result)
