from calculator.operations import add, subtract, multiply, divide

class Calculation:
    def __init__(self, x, y, operation):
        self.x=x
        self.y=y
        self.operation=operation

    def get_result(self):
        return self.operation(self.x, self.y)
    
class Calculator:
    @staticmethod
    def add(x,y):
        cal=Calculation(x, y, add)
        return cal.get_result()
    
    @staticmethod
    def subtract(x,y):
        cal=Calculation(x, y, subtract)
        return cal.get_result()
    
    @staticmethod
    def multiply(x,y):
        cal=Calculation(x, y, multiply)
        return cal.get_result()
    
    @staticmethod
    def divide(x,y):
        cal=Calculation(x, y, divide)
        return cal.get_result()