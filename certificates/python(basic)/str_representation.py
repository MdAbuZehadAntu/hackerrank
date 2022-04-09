#!/bin/python3

import math
import os
import random
import re
import sys


class Car:
    def __init__(self , max_speed , units):
        self.max_speed = max_speed
        self.units = units

    def __str__(self):
        return "Car with max speed of " + str(self.max_speed) + " and " + str(self.units) + " units"


class Boat:
    def __init__(self , max_speed):
        self.max_speed = max_speed

    def __str__(self):
        return "Boat with the maximum speed of " + str(self.max_speed) + " knots"


car = Car(100 , "km/h")
print(car)
