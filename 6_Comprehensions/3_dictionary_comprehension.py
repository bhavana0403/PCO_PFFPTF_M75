# dictionary comprehension

st = 'hello'
for i in enumerate(st):
    print(i)
"""
(0, 'h')
(1, 'e')
(2, 'l')
(3, 'l')
(4, 'o')
"""

for index, val in enumerate(st):
    print(index, val)
"""
0 h
1 e
2 l
3 l
4 o
"""

for num, val in enumerate(st, start=1):
    print(num, val)
"""
1 h
2 e
3 l
4 l
5 o
"""

#########################################################################################

l = [10, 20, 30, 40]
st = 'abcd'
for i in zip(l, st):
    print(i)
"""
(10, 'a')
(20, 'b')
(30, 'c')
(40, 'd')
"""

for i, j in zip(st, l):
    print(i, j)
"""
a 10
b 20
c 30
d 40
"""

for i, j, k in zip('ABCD', 'abc', [1, 2, 3, 4, 5]):
    print(i, j, k)
"""
A a 1
B b 2
C c 3
"""
"""
The number of iterations of for loop when we use 'zip' will be equal to length of 
smallest collection
"""


