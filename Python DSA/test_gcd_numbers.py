from GCDof2numbers import findGCD

def test_GCD():
    assert findGCD(9, 3)
    assert findGCD(9, -3)
    assert findGCD(9, 0)
    assert findGCD(0, 0)
    assert findGCD(90.45678, 0)