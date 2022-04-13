#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill , k , b):
    anna_ate = bill.copy()
    anna_ate.remove(bill[k])
    anna_pays = sum(anna_ate)//2

    if anna_pays == b:
        print("Bon Appetit")
    else:
        print(b-anna_pays)


if __name__ == '__main__':
    bonAppetit([3 , 10 , 2 , 9] , 1 , 12)
