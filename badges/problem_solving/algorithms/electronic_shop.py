#!/bin/python3

import os
import sys


#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards , drives , b):
    max_buy = -1

    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if b >= (keyboards[i] + drives[j]) > max_buy:
                max_buy = (keyboards[i] + drives[j])
    return max_buy


if __name__ == '__main__':
    moneySpent = getMoneySpent([3,1] , [5 , 2, 8] , 10)
    print(moneySpent)
