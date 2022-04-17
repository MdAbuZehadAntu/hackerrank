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

def get_score(ranked):
    return dict(zip(ranked,[i+1 for i in range(len(ranked))]))

def climbingLeaderboard(ranked , player):
    score = list()

    for item in player:
        ranked = sorted(list(set(ranked)) , reverse=True)
        tmp = get_score(ranked)

        # print(ranked)
        if item not in ranked:
            ranked.append(item)
            ranked = sorted(list(set(ranked)) , reverse=True)
            tmp = get_score(ranked)
        score.append(tmp[item])
    return score







if __name__ == '__main__':
    result = climbingLeaderboard([100 , 90 , 90 , 80 ] , [70,80,105])
    print(result)
