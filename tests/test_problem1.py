import pytest
import Solutions as S


def test_problem1():
    # <10: 3, 5, 6, 9 = 23
    assert S.problem1(10) == 23
    # <20: 3, 5, 6, 9, 10, 12, 15, 18 = 78
    assert S.problem1(20) == 78
    # <1000: 
    assert S.problem1(1000) == 233168