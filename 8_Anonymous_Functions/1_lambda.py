# lambda
"""
-> Syntax:
            lambda arguments: expression
"""

def even(num):
    return num % 2 == 0


print(even(87))     # False
print(even(88))     # True

_even = lambda num: num % 2 == 0
print(_even(87))    # False
print(_even(88))    # True

def square(num):
    return num ** 2

print(square(12))   # 144

_square = lambda num: num**2
print(_square(12))  # 144

sq_cube = lambda num: (num**2, num**3)
print(sq_cube(2))       # (4, 8)

# num and it's factorial

from math import factorial
fact = lambda num: factorial(num)

print(fact(8))      # 40320

# lambda expression to check if a string is starting with vowel
check = lambda st: st[0] in 'aeiouAEIOU'
print(check('alex'))    # True
print(check('philmon'))     # False

# lambda expression to check if a string is a palindrome
check = lambda st: st == st[::-1]
print(check('malayalam'))   # True
print(check('hindi'))       # False

# lambda expression to check if value is present in the collection
check = lambda val, coll: val in coll
print(check(10, [10, 20, 30]))  # True

# expression to return the last value of the sequence
res = lambda seq: seq[-1]
print(res([10, 20, 30]))    # 30
print(res('aujsdgfjasdc'))  # c
print(res((10, 20, 'hai'))) # hai

# lambda expression to return square if a number is even else return cube of a number

res = lambda num: num**2 if num % 2 == 0 else num **3
print(res(7))   # 343
print(res(8))   # 64

