# Relational Operator

# 1) Relational equal to operator (==)

# print(6 == 6+0j)        # True
#
# print((4+4j) == (4+4j))     # True
#
# print(True == 1.0)      # True
#
# print(28 == True)       # False
#
# print('abc' == 'abc')   # True
#
# print('abc' == 'bca')   # False
#
# print('ab' == 'abc')    # False
#
# print([1, 2, 'hello'] == ['hello', 1, 2])   # False
#
# print([1, 2, 'hello'] == [1, 2, 'hello'])   # True
#
# print({2, 3, 4} == {3, 4, 2})       # True
#
# print({'a': 1} == {'a': 1})         # True
#
# print({'a': 1} == {'a': 3})         # False

####################################################################################

# 2) Relational not equal to operator (!=)

# print('abc' != 'bca')       # True
#
# print({5, 7, 5.0} != {7, 5.0})      # False -> {5, 7} != {7, 5.0}

####################################################################################

# 3) Relational less than operator (<)

# print(41 < 41)      # False
#
# # print((3+3j) < (2+2j))  # TypeError
#
# print('B' < 'ABC')      # False -> 66 < 65 -> False
#
# print('a' < 'A')        # False -> 97 < 65 -> False
#
# print('A' < 'a')        # 65 < 97 -> True
#
# print(ord('e'))         # 101
#
# print(chr(78))          # N
#
# print('apple' < 'orange')       # True
#
# print('Apple' < 'aPPLE')        # True -> 65 < 97
#
# print('python' < 'pythoN')      # False -> 110 < 78
#
# print('pYTHON' < 'Python')      # p < P -> False
#
# print('data' < 'data')          # False -> 'a' < 'a'
#
# print('a' < 'abc')              # True
#
# print('abc' < 'a')              # False

"""
For string,
s1 < s2
if ord(s1[0]) < ord(s2[0]) -> True
if ord(s1[0]) > ord(s2[0]) -> False
if ord(s1[0]) == ord(s2[0]) -> compares ascii values of s1[1] and s2[1] and so on...............
 .......if ord(s1[-1]) == ord(s2[-1]) -> False 
"""

# print([10, 2, 3] < [1, 90, 30])     # False
#
# print([10, 2, 30] < [10, 20, 3])    # True
#
# print(['apple', 'yaho0', 'gmail'] < ['apple', 'yahoO', 'gmail'])        # 0 < O -> True

# print(['apple', 34, 'gmail'] < ['apple', 'yahoO', 'gmail'])     # TypeError

"""
For list,
l1 < l2
if l1[0] < l2[0] -> True
if l1[0] > l2[0] -> False
if l1[0] == l2[0] -> compare l1[1] and l2[1] and so on.........
"""

# print({0, 1, 2} < {1, 2, 3})        # False
#
# print({33, 1} < {32, 1, 33})        # True
#
# print({1, 2} < {33, 44, 55})        # False
#
# print({0, 1} < {0.9, 0.6, 0.0, 0.67, 1})        # True

"""
For set,
s1 < s2
True -> if s1 is a subset of set2 or s2 is a superset of s1
"""

###################################################################################

# 4) Relational greater than operator (>)

################################################################################

# 5) Relational less than equal to (<=)

print(6 <= 9)       # True

# print((8+8j) <= (8+8j))     # TypeError

print('APPLE' <= 'APPLe')    # True -> 'E' < 'e'

print('python' <= 'Python')     # False - 'p' < 'P'

print([6, 'pandas', 8.75] <= [5, 'pandas', 8.75])   # FAlse -> 6 <= 5

print((9.3, 'hello', 98) <= (9.3, 'hello', 98))     # True -> compare 98 <= 98

print({2, 3} <= {1, 2, 3})  # True -> s1 is subset of s2

print({2, 3, 1} <= {1, 2, 3})   # True -> s1 is equal to s2

print({3, 4} < {10, 20, 4, 30})     # False -> s1 is not subset of s2

#############################################################################

# 6) Relational greater than or equal to operator (>=)

############################################################################


