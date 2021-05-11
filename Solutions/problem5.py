# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import Solutions as S
from functools import reduce

def problem5(n=20):
    # compute the greatest common factor
    gcf = reduce(S.gcf, range(1, n+1))
    # compute the least common multiple (product/gcf)
    return reduce(lambda x,y: x*y, range(1, n+1)) // gcf