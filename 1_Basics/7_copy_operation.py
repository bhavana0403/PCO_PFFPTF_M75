# Copy Operation
"""
-> Here we copy the content of one variable to another variable
-> The content can be either variable space or value space
-> 1) General Copy/ Normal Copy
   2) Shallow Copy
   3) Deep Copy
"""

# 1) General Copy/ Normal Copy
"""
-> In case of general copy, variable space of one variable will be copied to another
   variable
-> Syntax:
            dest_var = source_var
-> In case of general copy, changes wrt one variable will change other variable
"""

nums = [[1, 2], 3, 4]
gen_copy = nums

nums[0][1] = 22
print(nums)         # [[1, 22], 3, 4]
print(gen_copy)     # [[1, 22], 3, 4]

nums[1] = 33
print(nums)         # [[1, 22], 33, 4]
print(gen_copy)     # [[1, 22], 33, 4]





