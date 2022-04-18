#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#
import string


def designerPdfViewer(h , word):
    res = [h[string.ascii_lowercase.index(i)] for i in word]
    return len(res) * max(res)


if __name__ == '__main__':
    result = designerPdfViewer(
        [1 , 3 , 1 , 3 , 1 , 4 , 1 , 3 , 2 , 5 , 5 , 5 , 5 , 1 , 1 , 5 , 5 , 1 , 5 , 2 , 5 , 5 , 5 , 5 , 5 , 5] ,
        'torn')
    print(result)
