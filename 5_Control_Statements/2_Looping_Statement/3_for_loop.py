# for loop
"""
-> Syntax:
            for item in iterable:
                SB
-> initialisation and updation will be automated
-> for loop will get executed number of times which is equal to length of the collection
-> we can access the values of collection directly without the help of index numbers
"""

for ch in 'abcd':
    print(ch)
"""
a
b
c
d
"""

for val in [1, 'hai', True, [1, 2, 3]]:
    print(val)
"""
1
hai
True
[1, 2, 3]
"""

for val in (1, 2, 3, 4):
    print(val**2)
"""
1
4
9
16
"""

for val in {False, 'hello', (1, 2), 8+7j}:
    print(val)
"""
False
(1, 2)
(8+7j)
hello
"""

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for i in d:
    print(i)
"""
a
b
c
d
"""

for key in d.keys():
    print(key)
"""
a
b
c
d
"""

for key in d:
    print(d[key])
"""
1
2
3
4
"""

for val in d.values():
    print(val)
"""
1
2
3
4
"""

for key in d:
    print((key, d[key]))
"""
('a', 1)
('b', 2)
('c', 3)
('d', 4)
"""

for val in d.items():
    print(val)
"""
('a', 1)
('b', 2)
('c', 3)
('d', 4)
"""

for i in range(1, 5):
    print(i)
"""
1
2
3
4
"""

for i in range(5):
    print(i)
"""
0
1
2
3
4
"""
st = 'alex'
for i in range(len(st)):
    print(i)
"""
0
1
2
3
"""

for i in range(len(st)):
    print(i, st[i])
"""
0 a
1 l
2 e
3 x
"""

