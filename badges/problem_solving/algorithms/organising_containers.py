#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    col = sorted([ sum(x) for x in zip(*container)])
    row = sorted([sum(x) for x in container])
    if col ==  row:
        return 'Possible'
    else:
        return 'Impossible'


if __name__ == '__main__':
    result = organizingContainers([[1,4],[2,3]])
    print(result)
