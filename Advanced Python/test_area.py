
from  Assert import  squareRoot

import pytest

# @pytest.mark.one
# @pytest.skip(reason="Do not test")
def test_squareRoot():
    print('squareRoot')
    assert squareRoot(16) == 4 , " We can only take the squareroot of positive numbers"

def test_squareRoot_negative():
    print('squareRoot of negative numbers')
    assert squareRoot(500)  , " We can only take the squareroot of positive numbers"