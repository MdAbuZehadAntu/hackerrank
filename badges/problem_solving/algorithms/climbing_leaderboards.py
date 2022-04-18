#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

import bisect


def climbingLeaderboard(ranked , player):
    ranked = sorted(list(set(ranked)) , reverse=True)
    player.sort(reverse=True)
    # print(player)
    score = list()
    idx = 0
    for i in range(len(player)):
        while idx < len(ranked) and player[i] < ranked[idx]:
            idx += 1
        score.append(idx + 1)
        print(player[i] , score)
    return score[::-1]


if __name__ == '__main__':
    result = climbingLeaderboard([100 , 90 , 90 , 80] , [70 , 80 , 105])
    print(result)
