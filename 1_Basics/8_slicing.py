# Slicing
"""
-> To get group of values
-> Syntax:
            Var[SI:EI+-1:SV]
            where,
                SI -> Start Index
                EI -> End Index
                SV -> Step Value - the difference between index numbers of 2 consecutive
                                   values that needs to be extracted
                                 - By default it is equal to 0
                                 - if SV == 1,
                                        Var[SI:EI+-1]
                EI+1 -> when we want to fetch the values from left to right of the collection
                EI-1 -> when we want to fetch the values from right to left of the collection
"""

st = 'harry potter'
"""
-12	-11	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1
h	a	r	r	y		p	o	t	t	e	r
0	1	2	3	4	5	6	7	8	9	10	11
"""

# # harry
# print(st[0:4+1:1])
# print(st[0:5])
# print(st[-12:-8+1:1])
# print(st[-12:-7])
#
# # potter
# print(st[6:12:1])
# print(st[6:12])
#
# # arry pot
# print(st[1:8+1:1])
# print(st[1:9])
# print(st[-11:-4+1:1])
# print(st[-11:-3])

#############################################################################

# slicing by ordered index

# # hrypte
# print(st[0:10+1:2])
# print(st[-12:-2+1:2])
#
# # ar otr
# print(st[1:12:2])
#
# # rettop
# print(st[11:6-1:-1])
# print(st[-1:-7:-1])
#
#
# # to ra
# print(st[9:1-1:-2])
# print(st[9:0:-2])
# print(st[-3:-11-1:-2])
# print(st[-3:-12:-2])


# # potter
# print(st[6:11+1:1])
# print(st[6:12])
# print(st[-6:-1+1:1])    # '' -> st[6:0:1]
# print(st[-6::1])        # potter
# print(st[-6:])          # potter
# print(st[6:])           # potter
#
#
# # yrrah
# print(st[-8:-13:-1])
# print(st[4:0-1:-1])         # '' -> st[4:11:-1]
# print(st[4::-1])            # yrrah
# print(st[-8::-1])           # yrrah

"""
-> When we want to fetch the values till the end of the collection (left or right end)
   using either positive or negative indexing we can ignore writing EI+-1
-> Syntax:
            Var[SI::SV]
"""

# print(st[0:5])      # harry
# print(st[:5])       # harry
# print(st[::2])      # hrypte
# print(st[-1:-6-1:-1])   # rettop
# print(st[:-7:-1])       # rettop

"""
-> When we want to fetch the values from start of the collection (left or right), 
   we can ignore wrting SI
                Var[:EI:SV]
"""


# print(st[::])       # harry potter
# print(st)           # harry potter

# # when SV==-1, EV==-12 or -len(coll), SV=-1
# print(st[::-1])     # rettop yrrah

"""
-> To reverse a given collection we make use of the syntax,
            Var[::-1]
"""

# # print first 2 characters
# print(st[0:2:1])        # ha
# print(st[:2])           # ha
#
# # print first 4 characters
# print(st[:4])           # harr

"""
-> To get first 'n' characters we make use of the syntax,
            Var[:n]
"""
"""
-12	-11	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1
h	a	r	r	y		p	o	t	t	e	r
0	1	2	3	4	5	6	7	8	9	10	11
"""

# # To get last 2 characters
# print(st[10:12])        # er
# print(st[-2:])          # er
#
# # To get last 5 characters
# print(st[-5:])      # otter
# print(st[7:])       # otter

"""
-> To get last 'n' characters we make use of the syntax,
            Var[-n:]
"""

######################################################################################

sam = [4, 9.75, 'hello', ['john', 'steve', 'mary'], {8, 56, 93}, (6, 3)]

# 4
print(sam[0])

# (6, 3)
print(sam[5])
print(sam[-1])
print(sam[5][::])

# 'mary'
print(sam[3][2])

# 'nhoj'
print(sam[3][0][::-1])
print('john'[::-1])

# ['mary', 'steve']
print(sam[3][:-2-1:-1])

# (3, 6)
print(sam[5][::-1])

# olleh
print(sam[2][::-1])


# [4]
print(sam[0])
print(sam[0:0+1])

# (6,)
print(sam[5][0:1])

# 56
# print(sam[4][1])        # TypeError: 'set' object is not subscriptable


#####################################################################################

pyspiders = {'development': ['python',
                             'sql',
                             {'web technology': ['html', 'css', 'java script']},
                             'django'],
             'testing': ['python',
                         'sql',
                         {'manual testing': ['sdlc', 'testing', 'stlc']},
                         'automation']
             }

# # python
# print(pyspiders['development'][0])
# print(pyspiders['testing'][0])
#
# # html
# print(pyspiders['development'][2]['web technology'][0])

# # clts
# print(pyspiders['testing'][2]['manual testing'][2][::-1])
#
# # tpircs avaj
# print(pyspiders['development'][2]['web technology'][2][::-1])
#
# # django
# print(pyspiders['development'][3])

######################################################################################

sam = {'a': ['java', 'python'],
       'b': ('manual', 'automation'),
       'c': {'data', 'sql', 'manual'},
       'd': {'e': {'f': [1, 2, [3, 4]]}}
       }

# 'automation'
print(sam['b'][1])

# 'manual'
print(sam['b'][0])

# 4
print(sam['d']['e']['f'][2][1])

# 2
print(sam['d']['e']['f'][1])

# [1, 2, [3, 4]]
print(sam['d']['e']['f'])

# [4]
print(sam['d']['e']['f'][2][1:])
