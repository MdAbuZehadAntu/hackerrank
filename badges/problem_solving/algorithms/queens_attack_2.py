#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n , k , r_q , c_q , obstacles):
    # when no obstacles
    left = c_q - 1
    right = n - c_q
    up = n - r_q
    down = r_q - 1

    up_left = left if left <= up else up
    up_right = right if right <= up else up
    down_left = left if left <= down else down
    down_right = right if right <= down else down

    # obstacles are present

    for obstacle in obstacles:
        row = obstacle[0]
        col = obstacle[1]

        # left side
        if row == r_q and c_q > col:
            left = c_q - col - 1 if c_q - col - 1 < left else left
        # right side
        elif row == r_q and col > c_q:
            right = col - c_q - 1 if col - c_q - 1 < right else right
        # upside
        elif col == c_q and row > r_q:
            up = row - r_q - 1 if row - r_q - 1 < up else up
        # downside
        elif col == c_q and row < r_q:
            down = r_q - row - 1 if r_q - row - 1 < down else down
        # up left
        elif col < c_q and row > r_q:
            if c_q - col == row - r_q:
                up_left = row - r_q - 1 if row - r_q - 1 < up_left else up_left
        elif col > c_q and row > r_q:
            if col-c_q == row - r_q:
                up_right = row - r_q - 1 if row - r_q - 1 < up_right else up_right
        elif row < r_q and col < c_q:
            if r_q - row == c_q - col:
                down_left = c_q - col - 1 if c_q - col - 1 < down_left else down_left
        elif row < r_q and col > c_q:
            if r_q - row == col - c_q:
                down_right = col - c_q - 1 if col - c_q - 1 < down_right else down_right
    return left + right + up + down + up_left + up_right + down_left + down_right


if __name__ == '__main__':
    result = queensAttack(5 , 3 , 4 , 3 , [(5 , 5) , (4 , 2) , (2 , 3)])
    print(result)
