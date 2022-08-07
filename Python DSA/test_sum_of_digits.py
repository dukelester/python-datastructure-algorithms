from sumofdigits import findSum, findPower

def test_sumofdigits():
    assert findSum(9871)
    assert findSum(-9871)
    assert findSum(98.71)
    assert findSum(0)

def test_findpower():
    assert findPower(2, 8)
    assert findPower(-2, 8)
    assert findPower(2, 0)
    assert findPower(2.8, 8)
    assert findPower(2, 8.9656)
    assert findPower(2, -8.9656)

