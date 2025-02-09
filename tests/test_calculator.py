'''Calculator Test'''
from calculator import add, subtract

def test_addition():
    '''Test that addition function works '''    
    assert add(5,2) == 7

def test_subtraction():
    '''Test that subtraction function works '''    
    assert subtract(3,2) == 1

#End
