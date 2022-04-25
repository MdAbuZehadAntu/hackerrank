#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    chapters = [item for item in range(1,len(arr)+1)]
    f_dict = []
    page = []

    for i in chapters:
        problems = arr[i-1]
        if problems % k ==0:
            page_needed = problems // k
        else:
            page_needed = problems // k + 1
        page.append(page_needed)

    last_page = 1
    problem = 1
    for i,p in zip(chapters,page):
        f_dict.append({'pages':[x for x in range(last_page,last_page+p)],'problems' : [x for x in range(problem,arr[i-1]+1)]})
        last_page = last_page+p
    f = []
    for item in f_dict:
        item['problems'] = [item['problems'][i:i + k] for i in range(0, len(item['problems']), k)]
        f.append(dict(zip(item['pages'],item['problems'])))
    # print(f)
    result = 0
    for item in f:
        for key,val in item.items():
            if key in val:
                result += 1
    return result




if __name__ == '__main__':
    result = workbook(5, 3, [4,2,6,1,10])
    print(result)
