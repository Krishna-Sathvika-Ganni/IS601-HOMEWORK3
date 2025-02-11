from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

@pytest.fixture
def setup_calculations():
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('29'), Decimal('13'), add))
    Calculations.subtract_calculation(Calculation(Decimal('29'), Decimal('25'), subtract))

def test_add_calculation(setup_calculations):
    Cal=Calculation(Decimal('3'), Decimal('2'), add)
    Calculations.add_calculation(Cal)
    assert Calculations.get_latest() == Cal, "Adding the calculation to history failed."

def test_get_history(setup_calculations):
    history = Calculations.get_history()
    assert len(history) == 2, "History does not contain expected number of calculations"

def test_clear_history(setup_calculations):
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History is not cleared"

def test_get_latest(setup_calculations):
    latest = Calculations.get_latest()
    assert latest.x == Decimal('15') and latest.y == Decimal('5'), "Haven't got the correct latest calculation"

def test_find_by_operation(setup_calculations)
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Correct number of calculations with add operation are not found"
    subtract_operations = Calculations.find_by_operation("subtract")
    assert len(subtract_operations) == 1, "Correct number of calculations with subtract operation are not found"

def test_get_latest_with_empty_history():
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history"

