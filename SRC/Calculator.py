from calculations.add import *
from calculations.divide import *
from calculations.multiply import *
from calculations.square import *
from calculations.square_root import *
from calculations.subtract import *


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a,b ):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = divisioin(a, b)
        return self.result

    def squareroot(self, x):
        self.result = sqrt(x)
        return self.result

    def square(self, x):
        self.result = x*x
        return self.result
