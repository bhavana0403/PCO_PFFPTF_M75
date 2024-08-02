# nested loops

for i in 'abc':
    for j in '123':
        print(i, j)
"""
a 1
a 2
a 3
b 1
b 2
b 3
c 1
c 2
c 3
"""

for i in 'AB':
    for j in 'ab':
        for k in [10, 20]:
            print(i, j, k)
"""
A a 10
A a 20
A b 10
A b 20
B a 10
B a 20
B b 10
B b 20
"""

# 1) WAP to get the following output without using len

st = 'python programming language'
# o/p = [6, 11, 8]
words = st.split()      # ['python', 'programming', 'language']
res = []
for word in words:
    count = 0
    for ch in word:
        count += 1
    res.append(count)
print(res)          # [6, 11, 8]

# o/p = {'python': 6, 'programming': 11, 'language': 8}






