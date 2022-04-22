#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

from itertools import combinations


def acmTeam(topic):
    max_val = 0
    count = 0
    for i in range(len(topic)):
        for j in range(i , len(topic)):
            subject = 0
            for k , v in zip(topic[i] , topic[j]):
                if k == '1' or v == '1':
                    subject += 1
            if subject > max_val:
                max_val = subject
                count = 1
            elif subject == max_val:
                count += 1

    return [max_val , count]


if __name__ == '__main__':
    result = acmTeam(['10101' , '11110' , '00010'])
    print(result)
