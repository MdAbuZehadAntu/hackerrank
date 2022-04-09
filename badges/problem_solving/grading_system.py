#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents():
    grades = [73 , 67 , 38 , 33]
    upgraded_grades = []

    for grade in grades:
        if grade > 37 and grade % 5 != 0:
            count = 0
            temp_grade = grade
            while count < 3:
                if temp_grade % 5 == 0:
                    upgraded_grades.append(temp_grade)
                    break
                temp_grade += 1
                count += 1
            if count == 3:
                upgraded_grades.append(grade)
        else:
            upgraded_grades.append(grade)

    return upgraded_grades


# Write your code here

if __name__ == '__main__':
    gradingStudents()
