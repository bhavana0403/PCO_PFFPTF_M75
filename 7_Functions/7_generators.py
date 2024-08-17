# generators
"""
return -> stop the execution of the function and return the values to the function call
       -> control will come out of the function by taking the values
yield -> pause the execution, give the value to the function call and again go back to
         the same function and resume the execution
"""
def even():
    for num in range(1, 21):
        if num % 2 == 0:
            return num

# res = even()
# print(res)      # 2


def _even():
    for num in range(1, 21):
        if num % 2 == 0:
            yield num


# _res = _even()
# print(_res)     # <generator object _even at 0x000001C96F45FED0>
# print(type(_res))   # <class 'generator'>
# print(list(_res))       # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#
# _res = _even()
# for i in _res:
#     print(i)
"""
2
4
.
.
20
"""
# _res = _even()
# print(next(_res))   # 2
# print(next(_res))   # 4
# print(next(_res))
# print(next(_res))
# print(next(_res))
# print(next(_res))
# print(next(_res))
# print(next(_res))
# print(next(_res))
# print(next(_res))
# print(next(_res))       # StopIteration

"""
-> We can access the values present in generator object using 
1) Typecasting
2) for loop
3) next()
"""

_res = _even()
# print(len(_res))        # TypeError
# print(next(_res))       # 2
# print(next(_res))       # 4
# for i in _res:
#     print(i)
"""
6
8
.
.
20
"""

"""
1) Iterators
-> zip, enumerate, map, filter, generators
-> iterate over them using for loop
-> it does not have length
-> next() can be applied
-> can not re-initialise itself

2) Iterables
-> str, list, tuple, set, dictionary, range
-> iterate over them using for loop
-> it has length
-> next can not be applied
-> can re-initialised itself
"""

# st = 'hello'
# for i in st:
#     print(i)
#
# for i in st:
#     print(i)
#
# s = enumerate(st)
# for i in s:
#     print(i)
#
# for i in s:
#     print(i)


#####################################################################################

def spam():
    print('Hello')
    return 1
    return 2
    return 3
#
# res = spam()    # Hello
# print(res)      # 1

def _spam():
    print('Hello')
    yield 1
    yield 2
    yield 3

# _res = _spam()
# print(_res)     # <generator object _spam at 0x000001BA01F35480>
# print(next(_res))
"""
Hello
1
"""
# print(next(_res))   # 2
# print(next(_res))   # 3
# print(next(_res))       # StopIteration

########################################################################################d

def spam_gen():
    print('Hello')
    yield 10
    print('Good evening')
    yield 20
    print("how are you")
    yield 30


# res = spam_gen()
# print(next(res))
"""
Hello
10
"""

# print(next(res))
"""
Good evening
20
"""

# print(next(res))
"""
how are you
30
"""

# print(next(res))    # StopIteration

######################################################################################

# generate infinite even numbers

def even_gen():
    num = 1
    while True:
        if num % 2 == 0:
            yield num
        num += 1

print(even_gen())   # <generator object even_gen at 0x00000283BFF55480>
res = even_gen()
print(next(res))    # 2
for i in range(1, 101):
    print(next(res))

# list of names starting with vowel using generators

names = ['alex', 'iqual', 'eve', 'bob', 'clare', 'uday']

def vowel_names(iterable):
    for name in iterable:
        if name[0] in 'aeiouAEIOU':
            yield name

res = vowel_names(names)
print(next(res))       # alex
print(list(res))        # ['iqual', 'eve', 'uday']

###################################################################################

# generate infinte prime numbers
# extract all strings in given list using generators
