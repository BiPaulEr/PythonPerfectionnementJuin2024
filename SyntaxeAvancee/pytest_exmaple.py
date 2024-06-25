import pytest

def diviser(a, b):
    if b == 0:
        raise ValueError("Division par zéro")
    return a / b

def test_division_par_zero():

    with pytest.raises(ValueError) as excinfo:
        diviser(10, 0)
    assert "Division par zéro" == str(excinfo.value)

test_division_par_zero()