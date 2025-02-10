'''Calculator Test'''
from calculator import add, subtract

def test_addition():
    '''Test that addition function works '''    
    assert add(5,2) == 7

def test_subtraction():
    '''Test that subtraction function works '''    
    assert subtract(3,2) == 1

def test_multiplication():
    '''Test that Multiplication function works'''
    assert multiply(3,4) == 12

def test_division():
    '''Test that Division function works'''
    assert divide(10,5) == 2

#End
