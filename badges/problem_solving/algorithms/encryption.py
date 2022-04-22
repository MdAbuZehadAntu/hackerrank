#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):

    L = s.replace(' ' , '')
    print(len(L))
    col = max(math.floor(math.sqrt(len(L))) , math.ceil(math.sqrt(len(L))))
    row = min(math.floor(math.sqrt(len(L))) , math.ceil(math.sqrt(len(L))))
    if abs(row*col - len(L)) >= 1:
        row = col
    res = []
    st = 0
    end = col
    print(L,row,col)
    for i in range(row):
        res.append(L[st:end])
        st = end
        end += col
    rest = ""
    print(res)
    for i in range(col):
        for j in res:
            try:
                rest += j[i]
            except:
                pass
        rest += ' '

    return rest


if __name__ == '__main__':
    result = encryption("roqfqeylxuyxjfyqterizzkhgvngapvudnztsxeprfp")
    print(result)
