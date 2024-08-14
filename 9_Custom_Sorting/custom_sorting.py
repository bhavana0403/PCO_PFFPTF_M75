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


