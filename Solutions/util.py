from math import sqrt, ceil
from functools import reduce
from itertools import chain

def isPrime(n):
    if n == 2:
        return True
    f = 2
    while n / f >= f:
        if n % f == 0:
            return False
        f += 1
    return True


def isPalindrome(n):
    return True if [c for c in str(n)] == list(reversed([c for c in str(n)])) else False


def primeFactorization(n):
    result = []
    while not isPrime(n):
        for f in range(2, ceil(sqrt(n)) + 1):
            if isPrime(f) and n % f == 0:
                result.append(f)
                n = n // f
                break
    result.append(n)
    return result


def lcm(*argv):
    result = 1
    prime_factorizations = list(map(primeFactorization, argv))

    for f in set(list(chain.from_iterable(prime_factorizations))):  # loop through unique factors of any number
        result *= f**max([pf.count(f) for pf in prime_factorizations])  # take maximum power of each

    return result