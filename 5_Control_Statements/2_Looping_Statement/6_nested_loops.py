# nested loops

for i in 'abc':
    for j in '123':
        print(i, j)
"""
a 1
a 2
a 3
b 1
b 2
b 3
c 1
c 2
c 3
"""

for i in 'AB':
    for j in 'ab':
        for k in [10, 20]:
            print(i, j, k)
"""
A a 10
A a 20
A b 10
A b 20
B a 10
B a 20
B b 10
B b 20
"""

# 1) WAP to get the following output without using len

st = 'python programming language'
# o/p = [6, 11, 8]
words = st.split()      # ['python', 'programming', 'language']
res = []
for word in words:
    count = 0
    for ch in word:
        count += 1
    res.append(count)
print(res)          # [6, 11, 8]

# o/p = {'python': 6, 'programming': 11, 'language': 8}

# 2) WAP to create a list of numbers from 1 to 5 along with it's factorial

# o/p = [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120)]

num_factorial = []      # [] -> [(1, 1)] -> [(1, 1), (2, 2)] -> [(1, 1), (2, 2), (3, 6)] -> [(1, 1), (2, 2), (3, 6), (4, 24)] -> [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120)]

# num = 1
# fact = 1
# for i in range(1, num+1):
#     fact *= i
# num_factorial.append((num, fact))
#
# num = 2
# fact = 1
# for i in range(1, num+1):
#     fact *= i
# num_factorial.append((num, fact))
#
# num = 3
# fact = 1
# for i in range(1, num+1):
#     fact *= i
# num_factorial.append((num, fact))
#
# num = 4
# fact = 1
# for i in range(1, num+1):
#     fact *= i
# num_factorial.append((num, fact))
#
# num = 5
# fact = 1
# for i in range(1, num+1):
#     fact *= i
# num_factorial.append((num, fact))

num_factorial = []
for num in range(1, 6):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    num_factorial.append((num, fact))
print(num_factorial)        # [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120)]


# 3) WAP to get the following output

num_list = [[1, 2, 3, 4], [10, 12, 18], [8, 9], [10, 3, 4, 2, 1]]
# o/p = [10, 40, 17, 20]
res = []
for li in num_list:
    s = 0
    for num in li:
        s += num
    res.append(s)
print(res)      # [10, 40, 17, 20]


# 4) WAP to print all the prime numbers between the range m and n
"""
m = 1
n = 20
# o/p -> 2 3 5 7 11 13 17 19
"""
from math import sqrt
m, n = 1, 20
for num in range(m, n+1):
    if num > 1:
        for i in range(2, round(sqrt(num))+1):
            if num % i == 0:
                break
        else:
            print(num)

# 5) WAP to print all the perfect numbers between the range m, n
# 6) WAP to print all the Armstrong numbers between the range m, n
"""
370 -> 3**3 + 7**3 + 0**3 = 27 + 343 + 0 = 370 -> Armstrong
371 -> 3**3 + 7**3 + 1**3 = 27 + 343 + 1 = 371 -> Armstrong
123 -> 1**3 + 2**3 + 3**3 = 1 + 8 + 27 = 36 -> no
1634 -> 1**4 + 6**4 + 3**4 + 4**4 = 1634 -> Armstrong
"""
# 7) WAP to print all the harshad numbers between the range m, n
"""
if a number is exactly divisible by sum of it's digits then the number is called as
Harshad number 
45 -> 4 + 5 = 9 -> 45 % 9 == 0 -> True -> Harshad number
80 -> 8 + 0 = 8 -> 80 % 8 == 0 -> True -> Harshad number
22 -> 2 + 2 = 4 -> 22 % 4 == 0 -> False -> No
"""

# 8) WAP to print 'n' prime numbers
"""
n = 5 -> 2 3 5 7 11
n = 10 -> 2 3 5 7 11 13 17 19 23 29
"""
n = 10
num = 2
count = 0
while True:
    for i in range(2, round(sqrt(num)) + 1):
        if num % i == 0:
            break
    else:
        print(num)
        count += 1
    if count == n:
        break
    num += 1

# 9) WAP to print 'n' perfect numbers
# 10) WAP to print 'n' Armstrong numbers
# 11) WAP to print 'n' Harshad numbers

# 12) WAP to print 'n'th prime number
"""
n = 7 -> 17
n = 10 -> 29 
n = 4 -> 7
"""
n = 5
num = 2
count = 0
while True:
    for i in range(2, round(sqrt(num)) + 1):
        if num % i == 0:
            break
    else:
        count += 1
    if count == n:
        print(num)
        break
    num += 1

# 13) WPA to print 'n'th perfect number
# 14) WAP to print 'n'th Armstrong number
# 15) WAP to print 'n'th Harshad number

# 16) WAP to print 'n' fibonacci numbers
"""
0 1 1 2 3 5 8 13 21 34.............. 
n = 5 -> 0 1 1 2 3
n = 10 -> 0 1 1 2 3 5 8 13 21 34
"""

n = 6
num1 = 0
num2 = 1
if n == 1:
    print(num1)
else:
    print(num1, num2, sep='\n')
    count = 2       # 2 fibonacci numbers are printed
    while count < n:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        print(num2)
        count += 1

"""
n = 6
num1 = 0 -> 1 -> 1 -> 2 -> 3
num2 = 1 -> 1 -> 2 -> 3 -> 5
o/p -> 0 1 1 2 3 5
count = 2 -> 3 -> 4 -> 5 -> 6

2 < 6 -> True
num3 = 0 + 1 = 1
num1 = 1
num2 = 1
count = 2 + 1 = 3

3 < 6 -> True
num3 = 1 + 1 = 2
num1 = 1
num2 = 2

4 < 6 -> True
num3 = 1 + 2 = 3
num1 = 2
num2 = 3

5 < 6 -> True
num3 = 2 + 3 = 5
num1 = 3
num2 = 5

6 < 6 -> False -> Exit
"""

# 17) WAP to print 'n' th fibonacci number









