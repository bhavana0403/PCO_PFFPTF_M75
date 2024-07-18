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

print(41 < 41)      # False

# print((3+3j) < (2+2j))  # TypeError

print('B' < 'ABC')      # False -> 66 < 65 -> False

print('a' < 'A')        # False -> 97 < 65 -> False

print('A' < 'a')        # 65 < 97 -> True

print(ord('e'))         # 101

print(chr(78))          # N

print('apple' < 'orange')       # True

print('Apple' < 'aPPLE')        # True -> 65 < 97

print('python' < 'pythoN')      # False -> 110 < 78

print('pYTHON' < 'Python')      # p < P -> False

print('data' < 'data')          # False -> 'a' < 'a'

print('a' < 'abc')              # True

print('abc' < 'a')              # False

"""
For string,
s1 < s2
if ord(s1[0]) < ord(s1[0]) -> True
if ord(s1[0]) > ord(s2[0]) -> False
if ord(s1[0]) == ord(s2[0]) -> compares ascii values of s1[1] and s2[1] and so on...............
 .......if ord(s1[-1]) == ord(s2[-1]) -> False
"""





