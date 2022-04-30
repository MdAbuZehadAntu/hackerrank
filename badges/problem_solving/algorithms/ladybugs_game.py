#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    st = b
    flag = 0
    for i in st:
        if st.count(i) == 1 and i != '_':
            return 'NO'
    if '_' not in st:
        for i in range(1 , len(st) - 1):
            if st[i] == st[i - 1] or st[i] == st[i + 1]:
                print(st[i] , st)
                pass
            else:
                flag = 1
        if st[0] != st[1]:
            flag = 1
        if st[-1] != st[-2]:
            flag = 1

    if flag == 0:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    result = happyLadybugs('DDFQQQF')
    print(result)
