# Input Statement
"""
-> To consider user input at the time of execution we make use of input function
            Var = input('message')
            where, writing the message is not mandatory
-> By default input will be taken in the form of string datatype
-> To consider input for a specific datatype we make use of typecasting
"""

# var = input()
# print(var)

# var = input('Enter the value : ')
# print(var)
# print(type(var))
"""
Enter the value : hai
hai
<class 'str'>

Enter the value : 35
'35'
<class 'str'>
"""

# integer input
# var = int(input('Enter the value : '))
# print(var)
# print(type(var))
"""
Enter the value : 75
75
<class 'int'>
"""

# float input
# var = float(input('Enter the value : '))
# print(var)
# print(type(var))
"""
Enter the value : 86
86.0
<class 'float'>

Enter the value : 7.86
7.86
<class 'float'>
"""

# complex -> complex(input())
# bool -> bool(input())

# list input
# var = list(input('Enter the value : '))
# print(var)
# print(type(var))
"""
Enter the value : [1, 2, 3]
['[', '1', ',', ' ', '2', ',', ' ', '3', ']']
<class 'list'>
"""

# to consider generalized input we make use of the eval function

var = eval(input('Enter the value : '))
print(var)
print(type(var))
"""
Enter the value : 87
87
<class 'int'>

Enter the value : {'a':1, 'b': 2}
{'a': 1, 'b': 2}
<class 'dict'>

Enter the value : False
False
<class 'bool'>

Enter the value : 'hai'
hai
<class 'str'>
"""

