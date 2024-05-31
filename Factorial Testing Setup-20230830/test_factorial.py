import pytest
from factorial import factorial

def test_type_float():
    with pytest.raises(TypeError):
        factorial(1.0)

def test_type_str():
    with pytest.raises(TypeError):
        factorial("abc")

def test_value_0():
    with pytest.raises(ValueError):
        factorial(0)

def test_value_neg():
    with pytest.raises(ValueError):
        factorial(-1)

testdata = [
    (1, 1),
    (5, 120),
    (6, 720)
]

@pytest.mark.parametrize("n,exp", testdata)
def test_fact(n, exp):
    assert factorial(n) == exp, "Factorial computation wrong"
