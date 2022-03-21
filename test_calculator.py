from calculator import Calculator 
from exceptions import NegativeAdder
import pytest

def test_zero_sum():
    assert Calculator.add("") == 0

def test_single_num():
    assert Calculator.add("4") == 4

def test_pair_of_nums():
    assert Calculator.add("4,3") == 7

def test_many_nums():
    assert Calculator.add("4,3,5,6,8") == 26

def test_new_line():
    assert Calculator.add("4,3,5\n6\n8") == 26

def test_custom_delemiter():
    assert Calculator.add("//;\n4;3;5;6;8") == 26

def test_report_negatives():
    with pytest.raises(NegativeAdder):
        assert Calculator.add("//;\n4;3;5;-6;-8")
    
