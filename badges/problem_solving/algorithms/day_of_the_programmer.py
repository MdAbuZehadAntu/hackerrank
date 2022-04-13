#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    st_year = str(year)
    if 1700 <= year <= 1917:
        if year % 4 == 0:
            day = "12"
            month = "09"
        else:
            day = "13"
            month = "09"
    elif year == 1918:
        day = "26"
        month = "09"
    elif 1919 <= year <= 2700:
        if year % 400 == 0:
            day = "12"
            month = "09"
        elif year % 4 == 0 and year % 100 != 0:
            day = "12"
            month = "09"
        else:
            day = "13"
            month = "09"

    date = f"{day}.{month}.{st_year}"
    return date


if __name__ == '__main__':
    result = dayOfProgrammer(1984)
    print(result)
