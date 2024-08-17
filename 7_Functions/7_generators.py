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



