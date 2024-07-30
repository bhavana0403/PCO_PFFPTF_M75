# while loop
"""
-> TSB gets executed until the given condition is False
-> Syntax:
            initialise
            while <cond>:
                TSB
                updation
-> If we do not initialise the looping variable, control will throw NameError
-> If we do not update the variable, the loop becomes infinite
"""


# 1) WAP to print the numbers from 1 to 10

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1       # i += 1

# 2) WAP to print the numbers from 1 to 10 along with its square
"""
(1, 1)
(2, 4)
.
.
.
(10, 100)
"""
# i = 1
# while i <= 10:
#     print((i, i**2))
#     i = i + 1


# 3) WAP to print the tables of a given number
"""
n = 5
5 * 1 = 5
5 * 2 = 10
.
.
.
5 * 10 = 50
"""

# n = int(input("Enter the number : "))
# i = 1
# while i <= 10:
#     print(f"{n} x {i} = {n*i}")
#     i += 1

# 4) WAP to print the numbers from 10 to 1

# i = 10
# while i >= 1:
#     print(i)
#     i -= 1

# 5) WAP to print the sum of first 'n' natural numbers

n = 10
s = 0
i = 1
while i <= n:
    s += i
    i += 1
print(f"The sum of first {n} natural numbers is {s}")
"""
n = 4
s = 0 -> 1 - > 3 -> 6 -> 10
i = 1 -> 2 -> 3 -> 4 -> 5

1 <= 4
s = 0 + 1 = 1

2 <= 4
s = 1 + 2 = 3

3 <= 4
s = 3 + 3 = 6

4 <= 4
s = 6 + 4 = 10

5 <= 4 -> False
"""

# 6) WAP to print the product of first 'n' natural numbers
n = 4
p = 1
i = 1
while i <= n:
    p *= i
    i += 1
print(f"The product of first {n} natural numbers is {p}")

# 7) WAP to print the characters of a string one by one
st = 'hello'
i = 0
while i < len(st):
    print(st[i])
    i += 1

# 8) WAP to print the values present at odd index numbers
vals = [19, 1, 28, 'hello', 'data', 'python', 9+7j, 6j]
i = 0
while i < len(vals):
    if i % 2 != 0:
        print(vals[i])
    i += 1

i = 1
while i < len(vals):
    print(vals[i])
    i += 2

# 9) WAP to print the values present at even index number in a tuple

# 10) WAP to print all the uppercase characters in a given string
st = 'HeLLo WoRLd'
i = 0
while i < len(st):
    if 'A'<=st[i]<='Z':
        print(st[i])
    i += 1

# 11) WAP to print all the lowercase characters in a given string
# 12) WAP to print all the numeric characters in a given string
# 13) WAP to print all the special characters in a given string
# 14) WAP to print all the alphabets in a given string

# 15) WAP to extract all the vowels from a given string

st = 'HEro'
vowel = ''
i = 0
while i < len(st):
    if st[i] in 'aeiouAEIOU':
        vowel += st[i]
    i += 1
print(vowel)

"""
vowel = '' -> 'E' -> 'Eo'
i = 0 -> 1 -> 2 -> 3 -> 4

0 < 4
'H' in 'aeiouAEIOU'

1 < 4
'E' in 'aeiouAEIOU'
vowel = '' + 'E' = 'E'

2 < 4
'r' in 'aeiouAEIOU'

3 < 4
'o' in 'aeiouAEIOU'
vowel = 'E' + 'o' = 'Eo'

4 < 4 -> False
"""

# 16) WAP to extract all the consonants in a given string

# 17) WAP to extract al the even numbers in a given homogenous list

nums = [1, 2, 3, 4, 5, 4, 5, 3, 2, 10, 12, 56]
res = []
i = 1
while i < len(nums):
    if nums[i] % 2 == 0:
        res += [nums[i]]
    i += 1
print(res)

"""
res = [] + [2] = [2]
res = [2] + [4] = [2, 4]
"""
res = []
i = 1
while i < len(nums):
    if nums[i] % 2 == 0:
        res.append(nums[i])
    i += 1
print(res)

# 18) WAP to extract all the string data-items in a given tuple to another tuple

t = ('hai', 'universe', 90, 9.23, False, 'True')
out = ()
i = 0
while i < len(t):
    if type(t[i]) == str:
        out += (t[i],)
    i += 1
print(out)

# 19) WAP to create a list of all the numbers between 1 and 200 which are divisible by 3

# 20) WAP to count all the numbers between 105 and 3000 which are divisible by both 5 and 7

# 21) WAP to separate all the even numbers and odd numbers into 2 lists from a given homogenous list collection

# 22) WAP to separate all the characters from a given string
st = 'HelLo Wo$lD 7%$76'
uc, lc, num, sc = '', '', '', ''
i = 0
while i < len(st):
    if 'A' <= st[i] <= 'Z':
        uc += st[i]
    elif 'a' <= st[i] <= 'z':
        lc+= st[i]
    elif '0' <= st[i] <= '9':
        num+= st[i]
    else:
        sc+= st[i]
    i += 1
print(uc, lc, num, sc, sep='\n')

# 23) WAP to reverse a given string without using slicing

# method 1
st = 'alex'
rev = ''
i = len(st) - 1
while i >= 0:
    rev = rev + st[i]
    i -= 1
print(f"The reverse of a given string '{st}' is '{rev}'")

"""
st = 'alex'
rev = '' -> 'x' -> 'xe' -> 'xel' -> 'xela'
i = 3 -> 2 -> 1 -> 0 -> -1

3 >= 0
rev = '' + 'x' = 'x'

2 >= 0
rev = 'x' + 'e' = 'xe'

1 >= 0
rev = 'xe' + 'l' = 'xel'

0 >= 0
rev = 'xel' + 'a' = 'xela'

-1 >= 0 -> False
"""

# method 2
st = 'alex'
rev = ''
i = -1
while i >= -len(st):
    rev = rev + st[i]
    i -= 1
print(f"The reverse of a given string '{st}' is '{rev}'")


# method 3
st = 'alex'
rev = ''
i = 0
while i < len(st):
    rev = st[i] + rev
    i += 1
print(f"The reverse of a given string '{st}' is '{rev}'")

"""
st = 'alex'

rev = 'a' + '' = 'a'
rev = 'l' + 'a' = 'la'
rev = 'e' + 'la' = 'ela'
rev = 'x' + 'ela' = 'xela'
"""

# 24) WAP to check if a given string is a palindrome or not without using slicing

st = 'racecar'
rev = ''
i = 0
while i < len(st):
    rev = st[i] + rev
    i += 1
if rev == st:
    print('The given string is a palindrome')
else:
    print('The given string is not a palindrome')

# 25) WAP to check if a given number is a palindrome without typecasting or slicing

num = 757
temp = num
rev = 0
while temp > 0:    # temp != 0
    rev = rev*10 + temp%10
    temp = temp // 10
if num == rev:
    print('Palindrome')
else:
    print('Not a palindrome')

"""
num = 758
temp = 758 -> 75 -> 7 -> 0
rev = 0 -> 8 -> 85 -> 857

758 > 0 
rev = 0*10 + 8 = 8
temp = 758 // 10 = 75

75 > 0
rev = 8*10 + 5 = 85
temp = 75 // 10 = 7

7 > 0
rev = 85*10 + 7 = 857
temp = 7 // 10 = 0

0 > 0 -> False
"""

