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

# hrypte
print(st[0:10+1:2])
print(st[-12:-2+1:2])

# ar otr
print(st[1:12:2])

# rettop
print(st[11:6-1:-1])
print(st[-1:-7:-1])

"""
-12	-11	-10	-9	-8	-7	-6	-5	-4	-3	-2	-1
h	a	r	r	y		p	o	t	t	e	r
0	1	2	3	4	5	6	7	8	9	10	11
"""

# to ra
print(st[9:1-1:-2])
print(st[9:0:-2])
print(st[-3:-11-1:-2])
print(st[-3:-12:-2])

