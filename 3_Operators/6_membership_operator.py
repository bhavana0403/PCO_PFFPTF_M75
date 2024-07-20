# Membership Operator
"""
-> It is an operator which is used to check whether a value is present in the collection
-> 1) in operator
   2) not in operator
"""

# 1) in operator
"""
-> It is an operator which gives the result as True if value is present in the
   collection
-> Syntax:
        Val in collection
"""

# print(5 in 587)     # TypeError

# print(5 in '585')       # TypeError

print('5' in '597')     # True

print('e' in 'science')     # True

print('e' in ['science'])       # False

print('science' in ['science'])     # True

print('e' in ['science'][0])        # 'e' in 'science' -> True

print('a' in {'a': 10, 'b': 20})        # True

print(20 in {'a': 10, 'b': 20})         # False - for control the visible layer is key layer

print(10 in [10, 20, 40])       # True

###################################################################################################################

# 2) not in operator

print(10 not in [[10, 20], 30, 40])     # True

print(10 not in [10, 20, 30])       # False




