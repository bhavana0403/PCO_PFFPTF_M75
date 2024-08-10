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






