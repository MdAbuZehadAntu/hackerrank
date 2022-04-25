#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h , m):
    time = None
    times = ["zero" ,
             "one" ,
             "two" ,
             "three" ,
             "four" ,
             "five" ,
             "six" ,
             "seven" ,
             "eight" ,
             "nine" ,
             "ten" ,
             "eleven" ,
             "twelve" ,
             "thirteen" ,
             "fourteen" ,
             "fifteen" ,
             "sixteen" ,
             "seventeen" ,
             "eighteen" ,
             "nineteen" ,
             "twenty" ,
             "twenty one" ,
             "twenty two" ,
             "twenty three" ,
             "twenty four" ,
             "twenty five" ,
             "twenty six" ,
             "twenty seven" ,
             "twenty eight" ,
             "twenty nine"]

    if 2 <= int(m) < 30 and int(m) != 15:
        time = f'{times[int(m)]} minutes past {times[h]}'
    if int(m) == 1:
        time = f'{times[int(m)]} minute past {times[h]}'
    if int(m) == 0:
        time = f'{times[h]} o\' clock'
    if int(m) == 15:
        time = f'quarter past {times[h]}'
    if int(m) == 30:
        time = f'half past {times[h]}'
    if int(m) > 30 and int(m) != 45:
        time = f'{times[60 - int(m)]} minutes to {times[h + 1]}'
    if int(m) == 45:
        time = f'quarter to {times[h + 1]}'

    return time


if __name__ == '__main__':
    result = timeInWords(5 , 45)
    print(result)
