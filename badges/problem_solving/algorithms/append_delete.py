# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

import difflib


def appendAndDelete(s , t , k):
    match_len = len(os.path.commonprefix([s,t]))
    mis_match_s = len(s) - match_len
    mis_match_t = len(t) - match_len
    e = k - (mis_match_t + mis_match_s)

    if e < 0:
        return 'No'
    if e < 2 * match_len and e % 2 != 0:
        return 'No'
    else:
        return 'Yes'


if __name__ == '__main__':
    result = appendAndDelete('y' , 'yu' , 2)
    print(result)
