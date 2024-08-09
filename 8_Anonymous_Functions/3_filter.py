# filter
"""
-> Syntax:
            filter_object = filter(func, iterable)
-> if the return from the function is a non-default value then the corresponding input
   will be stored in filter object, if the return is a default value, the corresponding
   input will be ignored
"""

nums = [1, 2, 3, 4]
even = lambda num: num % 2 == 0

print(list(map(even, nums)))      # [False, True, False, True]
print(list(filter(even, nums)))     # [2, 4]

a = lambda num: num**2 if num % 2 == 0 else 0
# print(a(2))     # 4
# print(a(7))     # 0

res = filter(a, nums)
print(list(res))        # [2, 4]

# filter only those words whose length is equal to 5

sentence = "hello steve where are you going"
check = lambda word: len(word) == 5
res = filter(check, sentence.split())
print(list(res))    # ['hello', 'steve', 'where', 'going']

# extract the names starting with vowel

names = ['steve', 'eve', 'alex', 'uday', 'paul']
res = filter(lambda name: name[0] in 'aeiouAEIOU', names)
print(list(res))      # ['eve', 'alex', 'uday']

# extract the names which is a palindrome
names = ['steve', 'eve', 'alex', 'uday', 'paul']
print(list(filter(lambda name: name==name[::-1], names)))       # ['eve']

# WAP to extract all the odd numbers in the range 1 to 10
res = filter(lambda num: num % 2 != 0, range(1, 11))
print(list(res))    # [1, 3, 5, 7, 9]

# extract all the square of even numbers between the range 1 to 20
evens = filter(lambda num: num % 2 == 0, range(1, 21))
# print(list(evens))
square = map(lambda num: num ** 2, evens)
print(list(square))     #

# WAP to extract all prime numbers in the range of 1 to 100

def is_prime(num):
    if num > 1:
        for i in range(2, num//2 + 1):
            if num % i == 0:
                return False
        return True

prime_nos = filter(is_prime, range(1, 101))
print(list(prime_nos))

# WAP to count the number of occurrences of a given character in a string using typ2 and type 4 functions

st = 'mississippi'
ch = 's'
c = 0
for i in st:
    if i == ch:
        c += 1
print(c)

