# abstraction
"""
-> abstract class acts as a design specification
-> ABC - Abstract Base Class
-> abstract method - method which has function declaration but not definition
-> abstract class - class which has atleast 1 abstract method
-> to create an abstract class we have to inherit ABC
-> to create an abstract method we have to make use of decorator called abstractmethod
-> we can not create an object for abstract class
-> until all the methods are over-rided we will not be able to create an object for the class
"""

from abc import ABC, abstractmethod

class Calc(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def sub(self, a, b):
        pass

    @abstractmethod
    def mul(self, a, b):
        pass

    @abstractmethod
    def div(self, a, b):
        pass


class Calculator(Calc):
    def add(self, a, b):
        if type(a) == dict and type(b) == dict:
            print({**a, **b})
        elif type(a) == set and type(b) == set:
            print(a.union(b))
        else:
            print(a + b)

    def sub(self, a, b):
        raise TypeError ("Can not subtract")

    def mul(self, a, b):
        print(a * b)

    def div(self, a, b):
        if type(a) == int and type(b) == int and b != 0:
            print(a / b)
        else:
            raise TypeError ("Can not divide a and b")


c1 = Calculator()

c1.add({'a':10}, {'b':20})
c1.sub(3, 8)

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def transfer(self, amount):
        pass

    @abstractmethod
    def transaction(self):
        pass

    @abstractmethod
    def roi(self):
        pass


