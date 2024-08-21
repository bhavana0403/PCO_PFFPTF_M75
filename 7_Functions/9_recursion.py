# recursion
"""
-> calling a function within itself until the termination condition is True is called
   recursion
-> Syntax:
            def fname(args):
                if <cond>:
                    return values
                ---------
                ---------
                return fname(args)

            def fname(args):
                if <cond>:
                    return
                ----------
                ----------
                fname(args)
"""

# Find the sum of first 'n' numbers using recursion
"""
Logic
n = 1 -> sum(1) -> 1
n = 2 -> 2 + 1 -> 2 + sum(1)
n = 3 -> 3 + 2 + 1 -> 3 + sum(2)
.
.
n -> n + sum(n-1)
"""

def _sum(n):
    if n == 1:
        return 1
    return n + _sum(n-1)


print(_sum(4))

# find the product of first 'n' natural numbers using recursion

def prod(n):
    if n == 1:
        return 1
    return n * prod(n-1)

print(prod(5))      # 120


#####################################################################################

nums = [1, 2, [3, 4, [5, 6]]]
# o/p = 21
s = 0
for i in nums:
    if type(i) == int:
        s += i
    elif type(i) == list:
        for j in i:
            if type(j) == int:
                s += j
            elif type(j) == list:
                for k in j:
                    if type(k) == int:
                        s += k

print(s)

nums = [1, 2, [3, 4, [5, 6]]]
def find_sum(li):
    s = 0
    for i in li:
        if type(i) == int:
            s += i
        elif type(i) == list:
            s += find_sum(i)
    return s

find_sum(nums)

# WAP to check whether a given number is a happy number
"""
49 -> 16 + 81 ->  97
              -> 81 + 49 -> 130
                         -> 1 + 9 + 0 -> 10
                                      -> 1 + 0 -> 1 -> happy number

51 -> 25 + 1 -> 26
             -> 4 + 36 -> 40
                       -> 16 + 0 -> 16
                                 -> 1 + 36 -> 37
                                           -> 9 + 49 = 58
                                                     -> 25 + 64 -> 89
                                                                -> 64 + 81 -> 145
                                                                           -> 1 + 16 + 25 -> 42
                                                                                          -> 16 + 4 = 20
                                                                                                    -> 4 + 0 -> 4 -> Not a happy number 
"""

