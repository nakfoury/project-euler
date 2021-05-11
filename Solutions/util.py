from math import sqrt, ceil

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


def gcf(x, y):
    result = 1
    # using primeFactorization
    fx = primeFactorization(x)
    fy = primeFactorization(y)

    # loop through unique factors of each number
    for f in set(fx+fy):
        # take minimum power of each
        result *= f**min(fx.count(f), fy.count(y))

    return result
    