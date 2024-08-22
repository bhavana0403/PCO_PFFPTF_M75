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

def is_happy(num):
    if num == 1:
        return "Happy Number"
    elif num == 4:
        return "Not a happy number"
    else:
        s = 0
        for i in str(num):
            s += int(i)**2
        return is_happy(s)


print(is_happy(130))    # Happy Number
print(is_happy(20))     # Not a happy number

# Steps to convert any while loop program to recursion
"""
1) Initialise all the looping variables in the formal argument section
2) Write the termination condition exactly opposite to looping condition
3) Return the total result inside termination condition
4) Write the logic of the program as it is excluding looping condition and updation part
5) Increment or decrement must be done in formal argument section only
"""


# WAP to reverse a given string using recursion

# st = 'hello'
# rev = ''
# i = 0
# while i < len(st):
#     rev = st[i] + rev
#     i += 1
# print(rev)

def reverse_string(st, i=0, rev=''):
    if i >= len(st):
        return rev
    rev = st[i] + rev
    return reverse_string(st, i+1, rev)

print(reverse_string('hello'))

# 2) WAP to reverse the given number using recursion

num = 876
rev = 0
while num != 0:
    ld = num % 10
    rev = rev * 10 + ld
    num = num // 10
print(rev)

def reverse_num(num, rev=0):
    if num == 0:
        return rev
    ld = num % 10
    rev = rev * 10 + ld
    return reverse_num(num//10, rev)

print(reverse_num(876))

# 3) WAP to create a list of numbers from 10 to 1 using recursion

nums = []
i = 10
while i >= 1:
    nums.append(i)
    i -= 1
print(nums)

def create_list(nums=[], i=10):
    if i < 1:
        return nums
    nums.append(i)
    return create_list(nums, i-1)

print(create_list())        # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

