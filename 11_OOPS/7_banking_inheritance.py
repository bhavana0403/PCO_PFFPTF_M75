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

