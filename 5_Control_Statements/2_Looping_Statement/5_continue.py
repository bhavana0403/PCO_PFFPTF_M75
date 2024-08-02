# continue
"""
-> It is used to skip the current iteration and makes the control go for next iteration
"""

for i in range(1, 11):
    if i % 5 == 0:
        continue
    print(i)
"""
1
2
3
4
6
7
8
9
"""

# 1) WAP to print all the even numbers in the range 1 and 20 using continue
for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 2) WAP to print all the string dataitems in a given list
l = ['python', True, 8.86, '868']
for i in l:
    if type(i) != str:
        continue
    print(i)


# pass
"""
-> To validate an empty statement block we make use of pass
"""
a = 10
b = 5
if a > b:
    pass

for i in range(1, 10):
    pass


