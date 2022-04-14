#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    result = "Mouse C"
    if abs(x-z) < abs(y-z):
        result = "Cat A"
    elif abs(x-z) > abs(y-z):
        result = "Cat B"
    return result


if __name__ == '__main__':
    result = catAndMouse(1, 3, 2)
    print(result)

