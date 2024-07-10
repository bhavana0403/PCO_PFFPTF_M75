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

# nums = [[1, 2], 3, 4]
# gen_copy = nums
#
# nums[0][1] = 22
# print(nums)         # [[1, 22], 3, 4]
# print(gen_copy)     # [[1, 22], 3, 4]
#
# nums[1] = 33
# print(nums)         # [[1, 22], 33, 4]
# print(gen_copy)     # [[1, 22], 33, 4]

########################################################################################

# 2) shallow copy operation
"""
-> In case of shallow copy, value space of one variable will be copied to another variable
-> Syntax:
            dest_var = source_var.copy()
-> Here, changes wrt one variable will not affect another variable in case of linear
   list. but, in case of nested list, chanegs wrt one variable will affect another
   variable
"""

# nums = [[1, 2], 3, 4]
# shallow_copy = nums.copy()

# nums[2] = 44
# print(nums)             # [[1, 2], 3, 44]
# print(shallow_copy)     # [[1, 2], 3, 4]
#
# nums[0][0] = 11
# print(nums)             # [[11, 2], 3, 44]
# print(shallow_copy)     # [[11, 2], 3, 4]

######################################################################################

# 3) Deep Copy
"""
-> In deep copy, the entire values of one variable will be copied to another variable 
   with different address
-> Syntax:
            import copy
            dest_var = copy.deepcopy(source_var)
-> Here, changes wrt one variable will not affect another variable
"""
# import copy
# nums = [[1, 2], 3, 4]
# deep_copy = copy.deepcopy(nums)
#
# nums[0][1] = 22
# print(nums)         # [[1, 22], 3, 4]
# print(deep_copy)    # [[1, 2], 3, 4]

#######################################################################################