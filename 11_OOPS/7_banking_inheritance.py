# Inheritance - 'is a' relationship

class BankAccount:
    interest_rate = 4.0

    def __init__(self, fname, lname, amount):
        self.fname = fname
        self.lname = lname
        self.balance = amount
        self.transactions = [f"Account has been created with initial deposit of Rs.{self.balance}"]

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Amount of Rs.{amount} has been credited by deposit. Total balance is Rs.{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Amount of Rs.{amount} has been debited by withdraw. Total balance is Rs.{self.balance}")
        else:
            raise ValueError ("Insufficient Balance")

    def statement(self):
        print('*'*100)
        for item in self.transactions:
            print(item)
        print('*'*100)

    def roi(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount
        self.transactions.append(f"Amount of Rs.{interest_amount} has been credited by interest. Total balance is Rs.{self.balance}")


class SavingsBankAccount(BankAccount):
    def withdraw(self, amount):
        if amount > 10000:
            raise ValueError ("Can not withdraw more than 10000 at once")
        super().withdraw(amount)


# cust1 = SavingsBankAccount("Mary", "Joseph", 3000)
# cust1.deposit(15000)
# # cust1.withdraw(11000)       # ValueError: Can not withdraw more than 10000 at once
# cust1.withdraw(7000)
# cust1.statement()

class CurrentAccount(BankAccount):
    interest_rate = 0.0
    def __init__(self, fname, lname, amount):
        if amount >= 10000:
            super().__init__(fname, lname, amount)
        else:
            raise ValueError ("Minimum Balance must be Rs.10000")

    def withdraw(self, amount):
        if self.balance - amount < 10000:
            raise ValueError ("Minimum Balance of Rs.10000 must be maintained")
        else:
            super().withdraw(amount)


class SeniorCitizenAccount(BankAccount):
    interest_rate = 5.0

    def __init__(self, fname, lname, amount, age):
        super().__init__(fname, lname, amount)
        self.age = age

    def withdraw(self, amount):
        if amount > 20000:
            raise ValueError ("Can not withdraw more than 20000 at once")
        super().withdraw(amount)


# cust1 = SavingsBankAccount("Mary", "Joseph", 30000)
# cust2 = SeniorCitizenAccount("John", "Abraham", 30000, 65)
#
# cust1.roi()
# cust2.roi()
#
# cust1.statement()
# cust2.statement()
#
# # cust1.withdraw(12000)       # ValueError: Can not withdraw more than 10000 at once
# cust2.withdraw(12000)
#
# cust2.statement()


class SukanyaSamruddhiAccount(BankAccount):
    interest_rate = 10
    def withdraw(self, amount, age):
        if age < 18:
            raise Exception ("Can not withdraw before 18 years of age")
        super().withdraw(amount)


cust1 = SukanyaSamruddhiAccount("Mary", "Maria", 30000)
cust1.roi()
cust1.statement()

# cust1.withdraw(3000, 17)        # Exception: Can not withdraw before 18 years of age

#################################################################################

# composition - 'has a' relationship
# bank transactions - 'has a' customer but bank transactions is not a customer

class BankTransactions:
    """
    customer - object member
    can be an account holder of any of the account
    customer is an object of any kind of account
    """
    def __init__(self, customer):
        self.customer = customer

    def deposit(self, amount):
        self.customer.deposit(amount)

    def withdraw(self, *args):              # withdraw of sukanya samruddhi account takes age as argument
        self.customer.withdraw(*args)

    def statement(self):
        self.customer.statement()

    def roi(self):
        self.customer.roi()


cust1 = SavingsBankAccount("Mary", "John", 30000)
cust2 = SeniorCitizenAccount("Sita", "Ram", 67, 70000)
cust3 = CurrentAccount("Jolly", "Joseph", 50000)
cust4 = SukanyaSamruddhiAccount("Arati", "Akash", 100000)

bt_cust1 = BankTransactions(cust1)
bt_cust2 = BankTransactions(cust2)
bt_cust3 = BankTransactions(cust3)
bt_cust4 = BankTransactions(cust4)

bt_cust1.deposit(30000)
# bt_cust2.withdraw(15000)
bt_cust4.withdraw(2000, 16)

