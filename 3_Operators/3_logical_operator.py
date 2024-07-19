# Logical Operator

# 1) and operator
"""
-> and gives the result as False if any one of the operand is internally equal to
   False(default value), it gives True only if all the operands are internally
   equal to True(non-default val)
-> Truth Table
        op1     op2     o/p
        False   False   False - op1
        False   True    False - op1
        True    False   False - op2
        True    True    True - op2
-> The output will be the operand itself
-> The output will be the first default operand or the last non-default operand
   which ever comes first
"""

print(True and False)       # False

print(True and True)        # True

print(6 and 7)              # 7

print(6 and 0)              # 0

print(8 and 9 and 10)       # 10

print(0 and 10)             # 0

print(100 and 39 and 0 and 0j and 87)   # 0

print('hello' and '0' and 'happy' and 'evening')        # evening

#####################################################################################

# 2) or operator
"""
-> 'or' gives the result as True if any one of the operand is True, it gives the
   result as False if all the operands are False
-> Truth Table
        op1     op2     o/p
        False   False   False - op2 
        False   True    True - op2
        True    False   True - op1
        True    True    True - op1
-> The output will be first non-default value or last default value 
   which ever comes first

"""

print(False or True)       # True

print(10 or 20 or 0 or 0.0)     # 10

print('' or 'python' or 'java')     # python

print(0 or [] or {} or (0.0) or [0.0] or 0j)    # [0.0]

print(0 or [] or {} or (0.0)  or 0j)        #  0j

