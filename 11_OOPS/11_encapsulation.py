# public members/ public attributes
"""
-> These are the members which can be accessed both inside and outside the class
   as well as in child class
"""

class Demo:
    value = 10

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name, self.value)

d1 = Demo("Steve")
print(d1.name)
print(d1.value)
d1.display()
"""
Steve
10
Steve 10
"""

class Demo1(Demo):
    pass

# d2 = Demo1("Mary")
# print(d2.name)
# print(d2.value)
# d2.display()
"""
Mary
10
Mary 10
"""

###############################################################################

# protected members/ protected attributes
"""
-> These are the members that should be accessed inside the class or in the child class 
   but not outside the class
-> But we can access them outside the class if we know how the attribute is stored in the dictionary (_attributename)
"""
class Demo:
    _value = 11
    def __init__(self, name):
        self._name = name

    def _display(self):
        print(self._name, self._value)

# d1 = Demo("John")
# # print(d1.name)      # AttributeError
# print(d1.__dict__)      # {'_name': 'John'}
# print(d1._name)     # John
# print(d1._value)    # 11
# d1._display()    # John 11

#######################################################################################

# private members/ private attributes
"""
-> These are the members that can not be accesses outside the class or in the
   child class
-> 
"""

class Demo:
    _value = 10

    def __init__(self, name):
        self.__name = name

    def display(self):
        print(self._value, self.__name)


d1 = Demo("Bob")
# print(d1.name)      # AttributeError
# print(d1.__name)    # AttributeError
print(d1.__dict__)      # {'_Demo__name': 'Bob'}
print(d1._Demo__name)   # Bob
d1.display()        # 10 Bob

class Demo1(Demo):
    def spam(self):
        print(self._Demo__name)

# d2 = Demo1("Mary")
# d2.spam()




