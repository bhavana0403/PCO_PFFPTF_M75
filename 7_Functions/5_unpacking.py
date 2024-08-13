# unpacking

def sam():
    return 1, 2, 3

print(sam())    # (1, 2, 3)
a, b, c = sam()
print(a, b, c)  # 1 2 3

p, q, r = (10, 20, 30)
print(p, q, r)      # 10 20 30

name = 'eve'
c1, c2, c3 = 'eve'
print(c1, c2, c3)       # e v e

d = {'a': 1, 'b': 2}
k1, k2 = d
print(k1, k2)   # a b

v1, v2 = d.values()
print(v1, v2)   # 1 2

st = 'hello universe'
# first = st[0]
# second = st[1]
# last_second = st[-2]
# last = st[-1]

first, second, *rest, last_second, last = st
print(first, second, last_second, last)     # h e s e
print(rest)    # ['l', 'l', 'o', ' ', 'u', 'n', 'i', 'v', 'e', 'r']
""" values are packed in the form of a list """
print(''.join(rest))    # llo univer
print(*rest)    # l l o   u n i v e r

print('steve')     # steve
print(*'steve')     # s t e v e

print(*[10, 20, 30])    # 10 20 30

"""
* -> when used while declaring the function or outside the function it acts as packing
     operator
  -> when used while calling a function it acts as unpacking operator
"""

names = ['john', 'mary', 'steve', 'alex', 'joseph', 'stella', 'johnson']
name1, name2, *rest, name3 = names
print(name1, name2, name3)       # john mary johnson
print(rest)     # ['steve', 'alex', 'joseph', 'stella']
print(*rest)    # steve alex joseph stella

names1 = ['john', 'mary', 'steve']
names2 = ['alex', 'joseph', 'stella', 'johnson']
names = [*names1, *names2]
print(names)    # ['john', 'mary', 'steve', 'alex', 'joseph', 'stella', 'johnson']

print(*names1, *names2)     # john mary steve alex joseph stella johnson
print(*names)       # john mary steve alex joseph stella johnson

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
print(d1, d2)       # {'a': 1, 'b': 2} {'c': 3, 'd': 4}

d = {*d1, *d2}
print(d)        # {'d', 'b', 'c', 'a'}

d = {**d1, **d2}
print(d)        # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# print(**d1)     # TypeError

print(*d)               # a b c d
print(*d.values())      # 1 2 3 4
print(*d.items())       # ('a', 1) ('b', 2) ('c', 3) ('d', 4)

l1 = [11, 22, 33, 44, 55, 66]

*rest, a = l1
print(a, rest)  # 66 [11, 22, 33, 44, 55]

a, *rest, b = l1
print(a, b, rest)       # 11 66 [22, 33, 44, 55]




