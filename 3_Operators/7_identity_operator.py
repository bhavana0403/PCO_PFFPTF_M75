# Identity Operator
"""
-> It is an operator which give the result as 2 if both are operands are pointing
   to the same address
-> 1) is operator
   2) is not operator
"""

a = 10
b = 10
c = 20
d = c

print(a is b)       # True

print(c is d)       # True

print(d is not a)   # True

print(d is not c)   # False

st = 'mister perfect'
print(st[4] is st[-3])      # True

li = [10, 20, [30, 40]]
gen_copy = li
shallow_copy = li.copy()
import copy
deep_copy = copy.deepcopy(li)

print(li is gen_copy)       # True

print(shallow_copy is deep_copy)    # False

print(shallow_copy[2] is not gen_copy[2])   # FAlse

print(li[0] is deep_copy[0])    # True



