# while loop
"""
-> TSB gets executed until the given condition is False
-> Syntax:
            initialise
            while <cond>:
                TSB
                updation
-> If we do not initialise the looping variable, control will throw NameError
-> If we do not update the variable, the loop becomes infinite
"""


# 1) WAP to print the numbers from 1 to 10

# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1       # i += 1

# 2) WAP to print the numbers from 1 to 10 along with its square
"""
(1, 1)
(2, 4)
.
.
.
(10, 100)
"""
# i = 1
# while i <= 10:
#     print((i, i**2))
#     i = i + 1


# 3) WAP to print the tables of a given number
"""
n = 5
5 * 1 = 5
5 * 2 = 10
.
.
.
5 * 10 = 50
"""

# n = int(input("Enter the number : "))
# i = 1
# while i <= 10:
#     print(f"{n} x {i} = {n*i}")
#     i += 1

# 4) WAP to print the numbers from 10 to 1

i = 10
while i >= 1:
    print(i)
    i -= 1

# 5) WAP to print the sum of first 'n' natural numbers

n = 4





