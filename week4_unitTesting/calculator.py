''' Have to create classes because of the java heritage of unit testing'''
import decimal

''' Write simple calc Class with + - * /'''

import unittest

class Calculator:
    def add(self, x, y):
        if isinstance(x, str) or isinstance(y, str):
            raise TypeError
        else:
            return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y



