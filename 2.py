#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestDivisor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

#Get all the factors
def factors(n):
 self_copy = n
 result = [1]
 for i in range(2,n+1):
  s = 0;
  while n/i == math.floor(n/float(i)):
   n = n/float(i)
   s += 1
  if s > 0:
   for k in range(s):
    result.append(i)
   if n == 1:
    result.append(self_copy)
    #remove duplicate primes
    return list(set(result))


def findSmallestDivisor(s, t):
    # Write your code here

    # non-divisible cases
    if len(s) % len(t) != 0:
        return -1
    if len(s) % len(t) == 0:
        concat_times = int(len(s) / len(t))
        res_str = ''
        for i in range(concat_times):
            res_str = res_str + t
        if res_str != s:
            return -1

    # divisible case => find the smallest u
    else:
        primes = factors(len(t))
        for prime in primes:
            concat_times = int(len(t)/prime)
            sub_str = t[:(prime)]
            res_str = ''
            for i in range(concat_times):
                res_str= res_str + sub_str
            if res_str == t:
                return prime



print(findSmallestDivisor('abcabc', 'abc'))
print(findSmallestDivisor('abcabc', 'de'))