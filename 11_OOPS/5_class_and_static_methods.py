# class method
"""
-> It is used to access and modify the members of the class
-> for all class methods we pass cls as an argument to store the address of the class
-> to create a class method we have to make use of the decorator 'classmethod'
"""


class Company:
    Company_Name = "ABC"
    main_branch = "Bengaluru"
    other_branches = ["Mumbai", "Chennai", "Hyderabad", "Delhi"]
    designations = ["Developer", "Test Engineer", "Team Lead", "Manager"]
    company_employees = []

    def __init__(self, emp_name, emp_id, branch, designation):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.designation = designation
        Company.company_employees.append(self)

    @classmethod
    def comp_details(cls):
        print(f"Company Name : {cls.Company_Name}")
        print(f"Branches : {len(cls.other_branches) + 1}")
        print(f"Main Branch : {cls.main_branch}")
        print(f"No of Employees : {len(cls.company_employees)}")

    @classmethod
    def display_branches(cls):
        print(cls.main_branch, *cls.other_branches, sep='\n')


# emp1 = Company("Amar", "TY123", "Bengaluru", "Test Engineer")
# emp2 = Company("Akbar", "TY124", "Mumbai", "Developer")
# emp3 = Company("Anthony", "TY125", "Chennai", "Team Lead")
# emp4 = Company("Alex", "TY235", "Bengaluru", "Manager")
# emp5 = Company("Akhil", "TY345", "Delhi", "Developer")

# Company.comp_details()
# emp1.comp_details()
#
# Company.display_branches()

# display the names of employees working as Developer
# display the names of employees working in Bengaluru Branch


#####################################################################################

class ShoppingCart:
    items = {'mobile': 5, 'laptop': 15, 'watch': 7, 'tablet': 10}
    prices = {'mobile': 1000, 'laptop': 5000, 'watch': 500, 'tablet': 1500}

    def __init__(self):
        self.cart = {}

    def add_item(self, item, quantity):
        if item not in ShoppingCart.items or quantity > ShoppingCart.items[item]:
            raise ValueError ("Item out of stock")
        self.cart[item] = quantity
        ShoppingCart.items[item] -= quantity

    def remove_item(self, item, quantity):
        if quantity <= self.cart[item]:
            self.cart[item] -= quantity
            ShoppingCart.items[item] += quantity
        else:
            raise ValueError

    def total_cost(self):
        total_cost = 0
        for item in self.cart:
            price = ShoppingCart.prices[item]
            no_of_items = self.cart[item]
            total_cost += price * no_of_items
        print(f"The total price of the cart is {total_cost}")

    def summary(self):
        print('*' * 100)
        for item, quantity in self.cart.items():
            price = ShoppingCart.prices[item]
            print(f"{item}  {quantity}  {price} {price*quantity}")
        self.total_cost()
        print('*' * 100)

    @classmethod
    def display_items(cls):
        for i, j in zip(cls.items.items(), cls.prices.items()):
            print(i[0], i[1], j[1], sep='\t')

    @classmethod
    def add_items(cls, item, quantity, price):
        if item in cls.items:
            cls.items[item] += quantity
        else:
            cls.items[item] = quantity
            cls.prices[item] = price


# ShoppingCart.display_items()
# ShoppingCart.add_items("mobile", 8, 1000)
# ShoppingCart.add_items("smart watch", 4, 2000)
#
# ShoppingCart.display_items()

#####################################################################################

# static method
"""
-> Static method neither belongs to class nor object but acts as a supporting method for
   both class and objects
-> passing self or cls is not required
-> we make use of a decorator called 'staticmethod' 
"""

class Calculator:
    @staticmethod
    def add(a, b):
        if type(a) in [int, float] and type(b) in [int, float]:
            print(a + b)
        else:
            raise TypeError ("Can add only real numbers")

    @staticmethod
    def sub(a, b):
        raise TypeError ("Can not subtract the values")

    @staticmethod
    def mul(a, b):
        if type(a) in [int, float] and type(b) in [int, float]:
            print(a * b)
        else:
            raise TypeError ("Can multiply only real numbers")



# # Calculator.add('a', 'b')
# print('a' + 'b')

c1 = Calculator()
c1.mul(4, 9.86)

