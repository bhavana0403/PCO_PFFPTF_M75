# Arithmetic Operator

# 1) Addition Operator (+)

print(2 + True)         # 3

print((7+7j) + True + False + 12)       # (20+7j)

print(2 + 2)        # 4

print('2' + '2')        # '22' -> concatenation

print([1, 2, 3, 4] + [2, 3, 4])     # [1, 2, 3, 4, 2, 3, 4]

print([1, 2, 3] + ['a', 'b', 'c'])  # [1, 2, 3, 'a', 'b', 'c']

# print([1, 2, 3] + 'abc')        # TypeError

print((1, 2) + (3, 4))      # (1, 2, 3, 4)

# print((1, 2) + (3))     # TypeError: -> 2nd operand is not a tuple, it is an integer

# print({1, 2, 3} + {4, 5})       # TypeError -> set doesn't support concatenation

# print({'a': 1} + {'a': 2})      # TypeError

####################################################################################

# 2) Subtraction Operator (-)

print(6 - True - (8+7j))    # (-3-7j)

# print('hai' - 'h')      # TypeError

# print([1, 2, 3] - [2, 3])   # TypeError

# print((1, 2, 3) - (3, 2))   # TypeError

print({1, 2, 3} - {2, 3})       # {1}
print({1, 2, 3}.difference({2, 3}))     # {1}

# print({'a': 10} - {'a': 4})     # TypeError

##################################################################################

# 3) Multiplication Operator (*)

print(2 * 2)        # 4

# print('2' * '2')    # TypeError

print('hai' * 2)        # haihai

print([1, 2, 3] * 2)    # [1, 2, 3, 1, 2, 3]

print((1, 2, 'hai', (3+1j), 8) * 3)     #

print((2+2j) * (1-3j))      # (8-4j)

# print({1, 2} * 2)       # TypeError

# print({'a': 1} * 3)     # TypeError

#####################################################################################

# 4) True Division (/)

print(40 / 2)       # 20

print((2+3j)/(1+1j))    # (2.5+0.5j)

# print('hai' / 'h')      # TypeError

# print(10 / 0)       # ZeroDivisionError

####################################################################################

# 5) Floor Division (//)

print(34 / 3)       # 11.33333334

print(34 // 3)      # 11

print(9999 / 1000)      # 9.999

print(9999 // 1000)     # 9

print(24 / 5)       # 4.8 -> 4 < 4.8 < 5

print(-24 / 5)      # -4.8 -> -5 < -4.8 < -4

print(24 // 5)      # 4

print(-24 // 5)     # -5


######################################################################################

# 6) Modulus (%)

print(18 / 10)      # 1.8

print(18 // 10)     # 1

print(18 % 10)      # 8

print(98756432134578 % 100)     # 78

###################################################################################

# 7) Power Operator (**)

print(3.2 ** 8)

print((-1)**0.5)    # (6.123233995736766e-17+1j)

print((4+3j) ** 2.5)    # (-2.121320343559637+55.86143571373726j)

# print('hai' ** 2)   # TypeError

####################################################################################

