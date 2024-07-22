# Output Statement
"""
-> It is used to display the result
-> Syntax:
        print(Val1, Val2, ..., Valn, sep=" ")

"""

print(1, 2, 3, 4, 5)
"""
1 2 3 4 5
"""

print(1, 2, 3, 4, 5, sep='\n')
"""
1
2
3
4
5
"""

print(1, 2, 3, 4, 5, sep='')
"""
12345
"""

print(1, 2, 3, 4, 5, sep='hai')
"""
1hai2hai3hai4hai5
"""

print(1, 2, 3, 4, 5, sep='@')
"""
1@2@3@4@5
"""

# print(a, b, c, d)   # NameError

print('a', 'b', 'c', 'd')   # a b c d

print(1, 2, 3, 4)
print(5, 6, 7, 8)
"""
1 2 3 4
5 6 7 8
"""

print(1, 2, 3, 4, end=' ')
print(5, 6, 7, 8)
"""
1 2 3 4 5 6 7 8
"""
print(1, 2, 3, 4, end=' ')
print(5, 6, 7, 8, end=' ')

print(1, 2, 3, 4, sep='\t', end='end')
