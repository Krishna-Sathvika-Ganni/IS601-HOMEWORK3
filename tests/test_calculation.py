'''The test_calculation.py module contains tests for the calculator operations and calculation class'''
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("x, y, operation, expected", [
    (Decimal('29'), Decimal('13'), add, Decimal('42')),
    (Decimal('29'), Decimal('25'), subtract, Decimal('4')),
    (Decimal('3'), Decimal('4'), multiply, Decimal('12')),
    (Decimal('39'), Decimal('3'), divide, Decimal('13')),
    (Decimal('28.5'), Decimal('13.5'), add, Decimal('42.0')),
    (Decimal('29.7'), Decimal('25.6'), subtract, Decimal('4.1')),
    (Decimal('3.2'), Decimal('6'), multiply, Decimal('19.2')),
    (Decimal('39.3'), Decimal('0.3'), divide, Decimal('131'))
])
def test_calculation_operations(x, y, operation, expected):
    '''Calculation operations with various cases'''
    calc = Calculation(x, y, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {x} and {y}"

def test_calculation_repr():
    '''Test the string representation (__repr__) of the Calculation class.'''
    calc=Calculation(Decimal('29'), Decimal('13'), add)
    expected_repr="Calculation(29, 13, add)"
    assert repr(calc) == expected_repr, "The __repr__ method is not matching the expected string."

def test_divide_by_zero():
    ''' Division by zero raises a Valueerror'''
    calc=Calculation(Decimal('15'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot be divided by Zero"):
        calc.perform()

#End
