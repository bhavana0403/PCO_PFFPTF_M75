
st = 'hello'
for i in enumerate(st):
    print(i)
"""
(0, 'h')
(1, 'e')
(2, 'l')
(3, 'l')
(4, 'o')
"""

for index, val in enumerate(st):
    print(index, val)
"""
0 h
1 e
2 l
3 l
4 o
"""

for num, val in enumerate(st, start=1):
    print(num, val)
"""
1 h
2 e
3 l
4 l
5 o
"""

#########################################################################################

l = [10, 20, 30, 40]
st = 'abcd'
for i in zip(l, st):
    print(i)
"""
(10, 'a')
(20, 'b')
(30, 'c')
(40, 'd')
"""

for i, j in zip(st, l):
    print(i, j)
"""
a 10
b 20
c 30
d 40
"""

for i, j, k in zip('ABCD', 'abc', [1, 2, 3, 4, 5]):
    print(i, j, k)
"""
A a 1
B b 2
C c 3
"""
"""
The number of iterations of for loop when we use 'zip' will be equal to length of 
smallest collection
"""

#######################################################################################

# dictionary comprehension
"""
Syntax:
        {key: value     for_loop}
"""
# build a dictionary of word and length pair in the sentence
sentence = "the wings of fire"
word_len = {word: len(word) for word in sentence.split()}
print(word_len)     # {'the': 3, 'wings': 5, 'of': 2, 'fire': 4}

# flip the keys and values of the dictionary
d = {'the': 3, 'wings': 5, 'of': 2, 'fire': 4}
res = {d[key]: key for key in d}
print(res)      # {3: 'the', 5: 'wings', 2: 'of', 4: 'fire'}

res = {value: key for key, value in d.items()}
print(res)      # {3: 'the', 5: 'wings', 2: 'of', 4: 'fire'}

# word count
sentence = "hello world welcome to python world hello everyone this is python world"
print(sentence.split().count('hello'))      # 2

res = {word: sentence.split().count(word) for word in sentence.split()}
print(res)      # {'hello': 2, 'world': 3, 'welcome': 1, 'to': 1, 'python': 2, 'everyone': 1, 'this': 1, 'is': 1}

words = sentence.split()
res = {word: words.count(word) for word in words}
print(res)      # {'hello': 2, 'world': 3, 'welcome': 1, 'to': 1, 'python': 2, 'everyone': 1, 'this': 1, 'is': 1}

# count the number of times each character is repeated
st = 'mississippi'
res = {ch: st.count(ch) for ch in st}
print(res)      # {'m': 1, 'i': 4, 's': 4, 'p': 2}


