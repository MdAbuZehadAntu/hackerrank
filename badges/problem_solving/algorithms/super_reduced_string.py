#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
sys.setrecursionlimit(10 ** 6)


def superReducedString(s):
    stack = []
    for i in s:
        if len(stack) > 0 and stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)
    if len(stack)==0:
        return 'Empty String'
    return ''.join(item for item in stack)


if __name__ == '__main__':
    result = superReducedString('acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveul'
                                'qfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj')
    print(result)
