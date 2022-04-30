#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#
import re


def gridSearch(G , P):
    idx = None
    s_len = 0
    for i in range(len(G)):
        if P[0] in G[i]:
            idx = [m.start() for m in re.finditer('(?='+P[0]+')' , G[i])]
            for p in idx:
                st_idx = p
                end_idx = st_idx + len(P[0])
                s_len = 1
                for j in range(1 , len(P)):
                    try:
                        if P[j] in G[j + i] and G[j + i][st_idx:end_idx] == P[j]:
                            s_len += 1
                    except:
                        pass
                if s_len == len(P):
                    return 'YES'

    return 'NO'


if __name__ == '__main__':
    result = gridSearch([
        "111111111111111" ,
        "111111111111111" ,
        "111111011111111" ,
        "111111111111111" ,
        "111111111111111"
    ] ,
        [
            "11111" ,
            "11111" ,
            "11110"

        ])
    print(result)
