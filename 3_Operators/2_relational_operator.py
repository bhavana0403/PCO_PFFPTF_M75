# Relational Operator

# 1) Relational equal to operator (==)

print(6 == 6+0j)        # True

print((4+4j) == (4+4j))     # True

print(True == 1.0)      # True

print(28 == True)       # False

print('abc' == 'abc')   # True

print('abc' == 'bca')   # False

print('ab' == 'abc')    # False

print([1, 2, 'hello'] == ['hello', 1, 2])   # False

print([1, 2, 'hello'] == [1, 2, 'hello'])   # True

print({2, 3, 4} == {3, 4, 2})       # True

print({'a': 1} == {'a': 1})         # True

print({'a': 1} == {'a': 3})         # False

####################################################################################

# 2) Relational not equal to operator (!=)

print('abc' != 'bca')       # True

print({5, 7, 5.0} != {7, 5.0})      # False -> {5, 7} != {7, 5.0}

####################################################################################

# 3) Relational less than operator (<)



