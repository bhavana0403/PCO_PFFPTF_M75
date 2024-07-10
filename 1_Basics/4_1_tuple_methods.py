# Tuple Methods

t = ('hai', '19', 19, 786, 8+7j, 98, 89, 19, '19', 19, 786, 'python', 'python')

# 1) Index

print(t.index(19))      # 2

# print(t.index(786, 4, 6))   # ValueError: tuple.index(x): x not in tuple

#########################################################################################

# 2) count

t = ('hai', '19', 19, 786, 8+7j, 98, 89, 19, '19', 19, 786, 'python', 'python')

print(t.count('python'))    # 2

print(t.count('java'))      # 0


print(dir(tuple))
print(dir(list))
print(dir(str))