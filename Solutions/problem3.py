# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

from . import util

def problem3(n=600851475143):
    result = 0
    f = 2
    while n / f >= f:
        if n % f == 0 and util.isPrime(f):
            result = f
        f += 1
    return result
