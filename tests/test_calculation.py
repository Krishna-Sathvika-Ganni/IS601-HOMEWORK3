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
    Cal = Calculation(x, y, operation)
    assert Cal.perform() == expected, f"Failed {operation.__name__} operation with {x} and {y}"

def test_calculation_repr():
    Cal=Calculation(Decimal('29'), Decimal('13'), add)
    expected_repr="Calculation(29, 13, add)"
    assert Cal.__repr__() == expected_repr, "The __repr__ method is not matching the expected string."

def test_divide_by_zero():
    Cal=Calculation(Decimal('15'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Division by zero cannot be done"):
        Cal.perform()