from DynamicProgr_memo import numberFactor

def test_number_factor():
    assert numberFactor(0, {5:''})
    assert numberFactor(2, {})
    assert numberFactor(-12, {})