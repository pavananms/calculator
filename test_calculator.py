from calculator import Calculator 

def test_zero_sum():
    assert Calculator.add("") == 0

def test_single_num():
    assert Calculator.add("4") == 4
