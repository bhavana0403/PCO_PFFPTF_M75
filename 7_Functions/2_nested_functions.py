# nested functions
"""
-> Calling a function inside another function is called nested function
-> Syntax:
            def func1():
                --------
                --------
                return values
            def func2():
                --------
                --------
                func1()
                --------
                return values
            func2()
                    or
            def func1():
                --------
                def func2():
                    ---------
                    ---------
                    return values
                ----------
                func2()
                return values
            func1()
"""

def extract_vowels(st):
    vowels = ''
    for ch in st:
        if ch in 'aeiouAEIOU':
            vowels += ch
    return vowels

words = ['good', 'evening', 'how', 'are', 'you']
# o/p = ['oo', 'eei', 'o', 'ae', 'ou']

def result(li):
    res = []
    for word in li:
        res += [extract_vowels(word)]
    print(res)

result(words)       # ['oo', 'eei', 'o', 'ae', 'ou']

#####################################################################################

# WAP to get the following output

nums = [86, 345, 7, 89, 26, 957]
# o/p = [68, 543, 7, 98, 62, 759]

def reverse(num):
    rev = 0
    while num != 0:
        rev = rev * 10 + num % 10
        num = num // 10
    return rev

def result(li):
    res = []
    for num in li:
        res += [reverse(num)]
    print(res)

result(nums)        # [68, 543, 7, 98, 62, 759]





