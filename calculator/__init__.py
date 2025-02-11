from calculator.operations import add, subtract, multiply, divide
from calculator.calculations import Calculations
from calculator.calculation import Calculation
from decimal import Decimal
from typing import Callable

class Calculator:
    @staticmethod
    def _perform_operation(x: Decimal, y: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        cal=Calculation.create(x, y, operation)
        Calculations.add_calculation(calculation)
        return cal.perform()

    @staticmethod
    def add(x: Decimal,y: Decimal) -> Decimal:
        return cal._perform_operation(x, y, add)
    
    @staticmethod
    def subtract(x: Decimal,y: Decimal) -> Decimal:
        return cal._perform_operation(x, y, subtract)
    
    @staticmethod
    def multiply(x: Decimal,y: Decimal) -> Decimal:
        return cal._perform_operation(x, y, multiply)
    
    @staticmethod
    def divide(x: Decimal,y: Decimal) -> Decimal:
        return cal._perform_operation(x, y, divide)