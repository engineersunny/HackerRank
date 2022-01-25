#!/bin/python3

import math
import os
import random
import re
import sys
from sklearn.linear_model import LogisticRegression
#
# Complete the 'calcMissing' function below.
#
# The function accepts STRING_ARRAY readings as parameter.
#

def calcMissing(readings):
    # Write your code here
    val_arr = []
    for line in readings:
        #'Missing' in line.split()[2]
        val_arr.append(line.split()[2])

    model = LogisticRegression(solver='liblinear', random_state=0)
    #model.fit(x, y)
    #model.predict(x)


if __name__ == '__main__':
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = input()
        readings.append(readings_item)

    calcMissing(readings)