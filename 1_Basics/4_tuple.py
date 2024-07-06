# Tuple(tuple)
"""
-> It is a homogeneous or heterogeneous collection of data-items enclosed between ()
-> Syntax:
            Var = (Val1, Val2, ........., Valn)
                        or
            Var = Val1, Val2, ........., Valn
-> The default value of tuple is ()
-> Tuple is a immutable collection
"""

t = (10, 'python', 'network', [1, 2])
print(type(t))      # <class 'tuple'>

a = 1, 2, 3, 5, 7, 8
print(a)        # (1, 2, 3, 5, 7, 8)
print(type(a))  # <class 'tuple'>

t = ()
print(t)        # ()
print(type(t))  # <class 'tuple'>

t = 8, 'hai', 9+7j, [1, 2, 3]
print(t[2])     # (9+7j)

# t[2] = 87       # TypeError -> tuple is immutable

l1 = [1]
t1 = (1)
print(type(l1))     # <class 'list'>
print(type(t1))     # <class 'int'>

l2 = ['python']
t2 = ('python')
print(type(l2))     # <class 'list'>
print(type(t2))     # <class 'str'>

"""
-> We can not store a single value inside a tuple directly, we make use of the syntax,
    Var = (Val,)
    Var = Val,
"""

t3 = 10,
t4 = ('python',)
print(type(t3))     # <class 'tuple'>
print(type(t4))     # <class 'tuple'>




