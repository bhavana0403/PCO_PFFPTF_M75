# set comprehension
"""
-> set comprehension is almost same as that of list comprehension in terms of syntax
   but the output list will be unordered and has unique values in case of set
"""
st = 'hello world'
res1 = [ch for ch in st]
print(res1)     # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

res2 = {ch for ch in st}
print(res2)     # {'o', 'd', 'h', 'e', 'w', 'l', ' ', 'r'}

