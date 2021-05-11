import Solutions as S


def test_isPrime():
    assert S.isPrime(2) == True
    assert S.isPrime(3) == True
    assert S.isPrime(4) == False
    assert S.isPrime(10) == False
    assert S.isPrime(11) == True
    assert S.isPrime(55) == False


def test_primeFactorization():
    assert S.primeFactorization(4) == [2, 2]
    assert S.primeFactorization(16) == [2, 2, 2, 2]
    assert S.primeFactorization(105) == [3, 5, 7]

def test_lcm():
    assert S.lcm(1, 1) == 1
    assert S.lcm(2, 4) == 4
    assert S.lcm(2, 2, 2) == 2
    assert S.lcm(2, 2, 2, 4) == 4
    assert S.lcm(5, 3, 6) == 30
