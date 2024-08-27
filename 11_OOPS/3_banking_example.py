class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.balance = amount
        self.transactions = [f"Account has been created with initial deposit of Rs.{self.balance}"]

    def deposit(self, amount):
        if amount < 0:
            raise ValueError ("Amount must be more than 0")
        self.balance += amount
        self.transactions.append(f"Amount of Rs.{amount} has been credited by deposit. Total Balance is Rs.{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError ("Insufficient Balance")
        self.balance -= amount
        self.transactions.append(f"Amount of Rs.{amount} has been debited by withdraw. Total Balance is Rs.{self.balance}")

    def statement(self):
        print('*' * 100)
        print(f"Statement of {self.name} Account")
        for item in self.transactions:
            print(item)
        print('*' * 100)

    def check_balance(self):
        print(f"Total available balance is Rs.{self.balance}")

    def transfer(self, other, amount):
        if amount > self.balance:
            raise ValueError ("Insufficient Balance")
        self.balance -= amount
        other.balance += amount
        self.transactions.append(f"Amount of Rs.{amount} has been transferred to {other.name}'s account. Total Balance is Rs.{self.balance}")
        other.transactions.append(f"Amount of Rs.{amount} credited by transfer from {self.name}'s account. Total Balance is Rs.{other.balance}")





acc1 = BankAccount("John", 3000)
acc2 = BankAccount("Mary", 5000)

print(acc1.__dict__)
print(acc2.__dict__)

acc1.deposit(3000)
# acc1.withdraw(20000)        # ValueError: Insufficient Balance
acc1.withdraw(2000)
acc1.deposit(12000)

acc1.transfer(acc2, 5000)

acc3 = BankAccount("Steve", 1000)

acc2.transfer(acc3, 4000)

# print(acc1.transactions)


acc1.statement()
acc2.statement()
acc3.statement()

acc1.check_balance()
acc2.check_balance()
acc3.check_balance()



