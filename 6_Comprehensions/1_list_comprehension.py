# list comprehension
"""
Syntax:
        [val_to_be_appended for_loop]
        [val_to_be_appended  for_loop   if <cond>]
        [true_value if <cond> else false_value  for_loop]
"""
st = 'hello world'
print(list(st))     # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

res = []
for ch in st:
    res.append(ch)
print(res)          # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

_res = [ch for ch in st]
print(_res)         # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# create a list of numbers from 1 to 10
print(list(range(1, 11)))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = []
for i in range(1, 11):
    res.append(i)
print(res)              # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

_res = [i for i in range(1, 11)]
print(_res)         # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


sentence = 'good evening everyone'
# o/p = [('good', 4), ('evening', 7), ('everyone', 8)]
res = []
for word in sentence.split():
    res += [(word, len(word))]
print(res)      # [('good', 4), ('evening', 7), ('everyone', 8)]

_res = [(word, len(word)) for word in sentence.split()]
print(_res)     # [('good', 4), ('evening', 7), ('everyone', 8)]

#########################################################################################

# WAP to extract all the even numbers from a given list

nums = [9, 876, 34, 11, 90, 55, 99, 44]
res = []
for num in nums:
    if num % 2 == 0:
        res.append(num)
print(res)      # [876, 34, 90, 44]

_res = [num for num in nums if num % 2 == 0]
print(_res)     # [876, 34, 90, 44]

#######################################################################################

# WAP to extract all the vowels from a given string using comprehensions

st = 'comprehensions'
vowels = []
for ch in st:
    if ch in 'aeiouAEIOU':
        vowels.append(ch)
print(vowels)       # ['o', 'e', 'e', 'i', 'o']
print(''.join(vowels))      # oeeio

_vowels = [ch for ch in st if ch in 'aeiouAEIOU']
print(_vowels)          # ['o', 'e', 'e', 'i', 'o']
print(''.join(_vowels))     # oeeio

_vowels1 = ''.join([ch for ch in st if ch in 'aeiouAEIOU'])
print(_vowels1)     # oeeio


# WAP to extract all the names starting with a in the given string

st = 'alex steve eve anthony alexander bob anitha aira'
res = []
for name in st.split():
    if name.startswith('a'):
        res.append(name)
print(res)      # ['alex', 'anthony', 'alexander', 'anitha', 'aira']


_res = [name for name in st.split() if name.startswith('a')]
print(_res)     # ['alex', 'anthony', 'alexander', 'anitha', 'aira']

# WAP to create a list of odd numbers in the range of 1 to 20
res1 = [num for num in range(1, 21) if num % 2 == 1]
print(res1)     # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

res2 = [num for num in range(1, 21) if num % 2]
print(res2)     # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# WAP to separate first names and last names from full names
names = ['steve jobs', 'bill gates', 'michael jackson', 'mukesh ambani', 'ratan tata']
first_name = [name.split()[0] for name in names]
last_name = [name.split()[1] for name in names]
print(first_name)       # ['steve', 'bill', 'michael', 'mukesh', 'ratan']
print(last_name)        # ['jobs', 'gates', 'jackson', 'ambani', 'tata']

# WAP to extract all the strings with even length from a given list
li = ['python', 'science', 'data', 'manual', 'webtech']
res = [word for word in li if len(word) % 2 == 0]
print(res)      # ['python', 'data', 'manual']

# WAP to create a list of numbers from 1 to 10 along with it's factorial

from math import factorial
print(factorial(7))     # 5040

res = [(i, factorial(i)) for i in range(1, 11)]
print(res)

######################################################################################

# WAP to create a list of numbers along with it's square if the number is even, if the number is odd extract it along with it's cube

# [(1, 1), (2, 4), (3, 27), (4, 16), .........., (9, 729), (10, 100)]

res = [(num, num**2) if num % 2 == 0 else (num, num**3) for num in range(1, 11)]
print(res)

# reverse the string in a list if length is even else keep it as it is

words = ['python', 'science', 'data', 'manual', 'webtech']
res = [word[::-1] if len(word) % 2 == 0 else word for word in words]
print(res)      # ['nohtyp', 'science', 'atad', 'launam', 'webtech']

#####################################################################################

# WAP to filter all the languages starting with 'p' or 'P'
languages = ['Python', 'persian', 'java', 'kannada', 'php', 'Pearl']
res1 = [language for language in languages if language[0] in 'pP']
res2 = [language for language in languages if language[0].lower() == 'p']
res3 = [language for language in languages if language.startswith('p') or language.startswith('P')]
print(res1, res2, res3, sep='\n')
"""
['Python', 'persian', 'php', 'Pearl']
['Python', 'persian', 'php', 'Pearl']
['Python', 'persian', 'php', 'Pearl']
"""

#######################################################################################




