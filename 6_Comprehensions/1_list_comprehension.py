# list comprehension
"""
Syntax:
        [val_to_be_appended for_loop]
        [val_to_be_appended  for_loop   if <cond>]
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








