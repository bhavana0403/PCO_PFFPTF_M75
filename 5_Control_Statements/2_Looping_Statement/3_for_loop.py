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

######################################################################################

# 1) WAP to extract all the vowels in a given string

st = 'thirtieth day of the month'
vowels = ''
for ch in st:
    if ch in 'aeiouAEIOU':
        vowels += ch
print(vowels)       # iieaoeo

for i in st:
    if i in 'aeiouAEIOU':
        print(i)

# 2) WAP to extract all the float numbers from a given list

"""
3) WAP to extract all the string present in  a tuple to a dictionary where each string
   is a key of the dictionary and the value is number of characters in the string
"""

t = ('apple', 'samsung', 'vivo', 'one plus')
# {'apple': 5, 'samsung': 7, 'vivo': 4, 'one plus': 8}
out = {}
for i in t:
    print(i)
    out[i] = len(i)
print(out)
"""
out['apple'] = 5
out['samsung'] = 7
.
.
"""

# 4) WAP to count the number of occurrence of a given character in a string without using count
st = 'mississippi'
ch = 's'
# o/p = 4
count = 0
for i in st:
    if i == ch:
        count += 1
print(f"The number of occurrence of '{ch}' in '{st}' is {count}")

# 5) WAP to get the following output
"""
st = 'abacaabbcaacb'
# o/p = 'a6b4c3'
"""
st = 'abacaabbcaacb'
res = ''
for i in st:
    if i not in res:
        res += i + str(st.count(i))
print(res)  # a6b4c3
"""
res = '' -> 'a6' -> 'a6b4' -> 'a6b4c3'

'a' not in ''
res = '' + 'a' + '6' = 'a6'

'b' not in 'a6'
res = 'a6' + 'b' + '4' = 'a6b4'

'a' not in 'a6b4' -> False

'c' not in 'a6b4' 
res = 'a6b4' + 'c' + '3' = 'a6b4c3'
"""

"""
6) 
st = 'abacaabbcaacb'
o/p = {'a': 6, 'b': 4, 'c': 3}
without using count
"""
st = 'abacaabbcaacb'
res = {}
for i in st:
    if i not in res:
        res[i] = 1
    else:
        res[i] += 1
print(res)

# 7) WAP to find the length of a list without using len

li = [89, 9.78, True, 'hai', (9+8j), 75]
count = 0
for _ in li:        # throw away variable
    count += 1
print(count)

# 8) WAP to remove the duplicate values from the string
st = 'mississippi'
# o/p = misp
res = ''
for ch in st:
    if ch not in res:
        res += ch
print(res)

# 9) WAP to create a tuple of 'n' natural numbers along with it's cube

# 10) WAP to extract all the even numbers present at odd indices of a given list

li = [2, 1, 4, 2, 7, 6, 3, 2, 9, 8, 22, 80, 88]
res = []
for i in range(len(li)):        # i takes all the index numbers of li
    if i % 2 != 0 and li[i] % 2  == 0:
        res.append(li[i])
print(res)

# 11) WAP to check if a given list is homogenous

# 12) WAP to create a list of all the factors of a given number
"""
8 -> [1, 2, 4, 8]
12 -> [1, 2, 3, 4, 6, 12]
7 -> [1, 7]
15 -> [1, 3, 5, 15]
"""
num = 343
factors = []
for n in range(1, num+1):
    if num % n == 0:
        factors.append(n)
print(factors)

# 13) WAP to check if a given number is a perfect number
"""
6 -> 1 + 2 + 3 = 6 -> perfect number
8 -> 1 + 2 + 4 = 7 -> not a perfect number
28 -> 1 + 2 + 4 + 7 + 14 = 28 -> perfect number
15 -> 1 + 3 + 5 = 8
"""

num = 128
sum_of_factors = 0
for i in range(1, num//2 + 1):
    if num % i == 0:
        sum_of_factors += i
if sum_of_factors == num:
    print('Perfect number')
else:
    print('not a perfect number')

# 14) WAP to reverse key and values of the dictionary

d = {'apple': 120, 'orange': 60, 'banana': 90, 'pineapple': 110}
# o/p = {120: 'apple', 60: 'orange', 90: 'banana', 110: 'pineapple'}

res = {}
for i in d:
    res[d[i]] = i
print(res)      # {120: 'apple', 60: 'orange', 90: 'banana', 110: 'pineapple'}

"""
res[120] = 'apple'
res[60] = 'orange'
"""

# 15) WAP to check if a given number is a prime number






