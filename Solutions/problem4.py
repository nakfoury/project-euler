# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

from . import util

def problem4(n=3):
    pals = []
    for x in range(10**n - 1, 10**(n-1) + 1, -1):
        for y in range(10**n - 1, 10**(n-1) + 1, -1):
            if util.isPalindrome(x * y):
                pals.append(x *y)
    return list(reversed(sorted(pals)))[0]