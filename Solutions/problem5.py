# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from Solutions.util import isPrime
import Solutions as S
from functools import reduce

def problem5(n=20):
    return S.lcm(*list(range(1, n+1)))
