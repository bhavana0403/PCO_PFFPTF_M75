# list method

# 1) append
"""
-> It is used to add the value to the last position of the list
-> Syntax:
            Var.append(Val)
-> The return type of append is None
-> append will modify the original list
"""

l = [1, 2, 'hai', 8+7j]
print(id(l))    # 2297409785344
print(l.append(10))     # None
print(l)    # [1, 2, 'hai', (8+7j), 10]
print(id(l))    # 2297409785344

