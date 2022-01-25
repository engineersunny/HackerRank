#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#4
#5 4 3 2
#

def closestNumbers(arr):
    # Write your code here
    res_arr = []

    arr.sort()
    min = math.inf
    for idx, val in enumerate(arr):
        if idx != len(arr)-1:
            if abs(val - arr[idx+1]) < min:
                min = abs(val - arr[idx+1])



    for idx, val in enumerate(arr):
        if idx != len(arr)-1:
            if abs(val - arr[idx+1]) == min:
                res_arr.append(val)
                res_arr.append(arr[idx+1])

    return res_arr

print(closestNumbers([-5, 15, 25, 71, 63]))


# 63 71 = 8
# 25 63 = 40