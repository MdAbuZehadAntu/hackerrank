#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
import numpy as np


def generate_magic_squares(n):
    magic = [[8 , 1 , 6] , [3 , 5 , 7] , [4 , 9 , 2]]
    rotations = [list(map(list , zip(*np.rot90(magic , i)))) for i in range(n + 1)]
    reflections = [list(map(list , zip(*np.fliplr(m)))) for m in rotations]
    all_squares = rotations + reflections
    return all_squares


def get_cost(s1 , s2):
    cost = 0
    for i in range(len(s1)):
        for j in range(len(s1[i])):
            cost += abs(s1[i][j] - s2[i][j])
    return cost


def formingMagicSquare(s):
    all_squares = [
        [[8 , 1 , 6] , [3 , 5 , 7] , [4 , 9 , 2]] ,
        [[6 , 7 , 2] , [1 , 5 , 9] , [8 , 3 , 4]] ,
        [[2 , 9 , 4] , [7 , 5 , 3] , [6 , 1 , 8]] ,
        [[4 , 3 , 8] , [9 , 5 , 1] , [2 , 7 , 6]] ,
        [[6 , 1 , 8] , [7 , 5 , 3] , [2 , 9 , 4]] ,
        [[8 , 3 , 4] , [1 , 5 , 9] , [6 , 7 , 2]] ,
        [[2 , 7 , 6] , [9 , 5 , 1] , [4 , 3 , 8]] ,
        [[4 , 9 , 2] , [3 , 5 , 7] , [8 , 1 , 6]]
    ]
    print(all_squares)
    min_cost = float('inf')
    for square in all_squares:
        cost = get_cost(s , square)
        if cost < min_cost:
            min_cost = cost
    return min_cost


if __name__ == '__main__':
    result = formingMagicSquare([[4,5,8] , [2,4,1] , [1,9,7]])
    print(result)
