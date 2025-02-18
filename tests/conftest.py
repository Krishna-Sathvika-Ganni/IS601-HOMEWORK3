from decimal import Decimal
import pytest
from calculator.operations import add, subtract, multiply, divide

from faker import Faker

fake = Faker() # Initalizing the faker object

def generating_test_data(num_records):
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    for _ in range(num_records):
        x = Decimal(fake.random_number(digits=2))
        y = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))
        operation_name = fake.random_element(elements=list(operation_mappings.keys()))
        operation_func = operation_mappings[operation_name]

        if operation_func == divide:
            y = Decimal('1') if y == Decimal('0') else y  
        try:
            if operation_func == divide and y == Decimal('0'):
                expected = "ZeroDivisionError"
            else:
                expected = operation_func(x,y)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        
        yield x, y, operation_name, operation_func, expected

    def pytest_addoption(parser):
        parser.addoption("--num_records", action="store",default=5, type=int, help="Number of test records to generate")

    def pytest_generating_tests(metafunc):
        if {"x", "y", "expected"}.intersection(set(metafunc.fixturenames)):
            num_records = metafunc.config.getoption("num_records")
            parameters = list(generating_test_data(num_records))
            modified_parameters = [(x, y, op_name if 'operation_name' in metafunc.fixturenames else op_func, expected) for x, y, op_name, op_func, expected in parameters]
            metafunc.parametrize("x,y,operation,expected", modified_parameters)
