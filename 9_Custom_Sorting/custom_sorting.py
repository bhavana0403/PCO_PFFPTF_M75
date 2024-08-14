# custom sorting

nums = [12, 5, 23, 97, 65, 28, 29, 92]
print(nums.sort())      # None
print(nums)     # [5, 12, 23, 28, 29, 65, 92, 97]

names = ['alex', 'joseph', 'stella', 'johnson']
# names.sort()
# print(names)        # ['alex', 'johnson', 'joseph', 'stella']

s = 'abcd'
# print(s.sort())     # AttributeError  -> sort is a method of list

nums = [12, 5, 23, 97, 65, 28, 29, 92]
print(sorted(nums))     # [5, 12, 23, 28, 29, 65, 92, 97]
print(nums)     # [12, 5, 23, 97, 65, 28, 29, 92]

words = ['python', 'manual', 'c', 'java', 'pearl', 'ruby', 'javascript']
print(sorted(words))        # ['c', 'java', 'javascript', 'manual', 'pearl', 'python', 'ruby']
print(words)            # ['python', 'manual', 'c', 'java', 'pearl', 'ruby', 'javascript']

words.sort(key=len)
print(words)        # ['c', 'java', 'ruby', 'pearl', 'python', 'manual', 'javascript']

nums = [(22, 1), (2, 12), (3, 4), (7, 97), (22, 0), (86, 23)]
print(sorted(nums))     # [(2, 12), (3, 4), (7, 97), (22, 0), (22, 1), (86, 23)]

s = 'hello'
print(sorted(s))        # ['e', 'h', 'l', 'l', 'o']
print(sorted(s, reverse=True))     # ['o', 'l', 'l', 'h', 'e']

s = {12, 5, 23, 97, 65, 28, 29, 92}
print(sorted(s))    # [5, 12, 23, 28, 29, 65, 92, 97]

d = {'hello': 5, 'everyone': 8, 'good': 4, 'evening': 7}
print(sorted(d))        # ['evening', 'everyone', 'good', 'hello']
print(sorted(d.values()))   # [4, 5, 7, 8]
print(sorted(d.items()))    # [('evening', 7), ('everyone', 8), ('good', 4), ('hello', 5)]

####################################################################################

words = ['hello', 'everyone', 'welcome', 'to', 'python', 'class']

print(sorted(words))                            # ['class', 'everyone', 'hello', 'python', 'to', 'welcome']

print(sorted(words, reverse=True))              # ['welcome', 'to', 'python', 'hello', 'everyone', 'class']

print(sorted(words, key=len))                   # ['to', 'hello', 'class', 'python', 'welcome', 'everyone']

print(sorted(words, key=len, reverse=True))     # ['everyone', 'welcome', 'python', 'hello', 'class', 'to']

#####################################################################################

words = ['hello', 'everyone', 'welcome', 'to', 'python', 'class']

def find_len(st):
    c = 0
    for _ in st:
        c += 1
    return c

print(sorted(words, key=find_len))      # ['to', 'hello', 'class', 'python', 'welcome', 'everyone']

######################################################################################

names = ['alex', 'steve', 'eve', 'joseph', 'john', 'stella']

def first_char(st):
    return st[0]


print(sorted(names))                    # ['alex', 'eve', 'john', 'joseph', 'stella', 'steve']

print(sorted(names, key=first_char))    # ['alex', 'eve', 'joseph', 'john', 'steve', 'stella']

print(sorted(names, key=lambda st: st[0]))  # ['alex', 'eve', 'joseph', 'john', 'steve', 'stella']

####################################################################################

d = {'hello': 5, 'everyone': 8, 'good': 4, 'evening': 7}

print(d.items())    # [('hello', 5), ('everyone', 8), ('good', 4), ('evening', 7)]

print(sorted(d.items()))    # [('evening', 7), ('everyone', 8), ('good', 4), ('hello', 5)]

# sort based on keys
print(sorted(d.items(), key=lambda val: val[0]))        # [('evening', 7), ('everyone', 8), ('good', 4), ('hello', 5)]

# sort based on values
print(sorted(d.items(), key=lambda val: val[-1]))       # [('good', 4), ('hello', 5), ('evening', 7), ('everyone', 8)]

# sort based on last character of the key
print(sorted(d.items(), key=lambda val: val[0][-1]))    # [('good', 4), ('everyone', 8), ('evening', 7), ('hello', 5)]

#####################################################################################

d = {'hello': 'everyone', 'happy': 'holidays', 'well': 'done', 'good': 'handwriting'}

# sort based on length of key
# sort based on length of value
# sort based on first character of key
# sort based on last character of value

##################################################################################

