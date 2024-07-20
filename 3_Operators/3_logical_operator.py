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

print(4>3 and 8>10)     # True and False - False


ch = 'Y'

# check whether the character is uppercase
print(ord(ch) >= 65 and ord(ch) <= 90)
print(65 <= ord(ch) <= 90)
print('A' <= ch <= 'Z')

# check whether character is lowercase
print('a' <= ch <= 'z')

# check whether character is a number
print('0'<=ch<='9')

ch = '9'
# check whether character is an alphabet
print('A' <= ch <= 'Z' or 'a' <= ch <= 'z')

# check whether character is alphanumeric

###################################################################################

# 3) not operator
"""
-> It gives the result as True if the operand is default value and vice versa
"""

print(not 7)        # False

print(not 76>90)        #  True

print(not 'hai')        # False

# check if ch is a special character

ch = '@'
print(not('A' <= ch <= 'Z' or 'a' <= ch <= 'z' or '0' <= ch <= '9'))



