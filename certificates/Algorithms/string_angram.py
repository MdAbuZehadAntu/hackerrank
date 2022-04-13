#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary , query):
    sorted_dict = ["".join(sorted(item)) for item in dictionary]
    sorted_query = ["".join(sorted(item)) for item in query]
    fin_result = [0] * len(sorted_query)
    for i in range(len(sorted_query)):
        fin_result[i] = sorted_dict.count(sorted_query[i])
    return fin_result


if __name__ == '__main__':
    result = stringAnagram(['heater' , 'cold' , 'clod' , 'reheat' , 'docl'] , ['codl' , 'heater' , 'abcd'])
    print(result)
