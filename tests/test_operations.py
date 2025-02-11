from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    calculation = Calculation(Decimal('29'), Decimal('13'), add)
    assert calculation.perform() == Decimal('42'), "Addition operation failed"

def test_operation_subtract():
    calculation = Calculation(Decimal('29'), Decimal('25'), subtract)
    assert calculation.perform() == Decimal('4'), "Subtraction operation failed"

def test_operation_multiply():
    calculation = Calculation(Decimal('3'), Decimal('4'), multiply)
    assert calculation.perform() == Decimal('12'), "Multiplication operation failed"

def test_operation_divide():
    calculation = Calculation(Decimal('39'), Decimal('3'), divide)
    assert calculation.perform() == Decimal('12'), f"Division operation failed"

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot be divided by Zero"):
        calculation = Calculation(Decimal('15'), Decimal('0'), divide)
        calculation.perform()