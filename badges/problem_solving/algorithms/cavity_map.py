#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    new_grid = list()
    f_grid = list()
    row_col = list()
    for item in grid:
        new_grid.append([int(i) for i in item])
    for item in grid:
        f_grid.append([int(i) for i in item])

    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            if i != 0 and i != len(new_grid) - 1 and j != 0 and j != len(new_grid[0]) - 1:

                if new_grid[i][j] > new_grid[i - 1][j] and new_grid[i][j] > new_grid[i + 1][j] \
                        and new_grid[i][j] > new_grid[i][j + 1] and \
                        new_grid[i][j] > new_grid[i][j - 1]:
                    f_grid[i][j] = "X"

    grid = list()
    for item in f_grid:
        grid.append(''.join(str(i) for i in item))

    return grid


if __name__ == '__main__':
    result = cavityMap(['1112' , '1912' , '1892' , '1234'])
    print(result)

