#Get all the prime factors
import math
import os
import random
import re
import sys

def factors(n):
 result = [1]
 for i in range(2,n+1): # test all integers between 2 and n
  s = 0;
  while n/i == math.floor(n/float(i)): # is n/i an integer?
   n = n/float(i)
   s += 1
  if s > 0:
   for k in range(s):
    result.append(i) # i is a pf s times
   if n == 1:
    #return result
    #remove duplicate primes
    return list(set(result))

print(factors(3))


str = 'abcd'
print(str[:0])
print(str[:1])
str[:1]
