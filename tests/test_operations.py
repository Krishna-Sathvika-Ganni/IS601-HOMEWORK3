'''Testing operations'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation(x, y, operation, expected):
    '''Testing various operations'''
    calculation = Calculation.create(x, y, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot be divided by Zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()