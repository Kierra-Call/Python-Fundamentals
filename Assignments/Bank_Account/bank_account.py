class BankAccount:
    all_bank_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_bank_accounts.append(self)

    @classmethod
    def print_all(cls):
        for individual_account in cls.all_bank_accounts:
            individual_account.display_account_info()

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        return self

user1 = BankAccount(.02, 2000)
user2 = BankAccount(.032, 5000)

user1.deposit(500).deposit(1000).deposit(1200).withdraw(50).display_account_info() # 3 deposits and a withdraw
user2.deposit(100).deposit(9000).withdraw(10).withdraw(300).withdraw(200).withdraw(900).yield_interest().display_account_info()

BankAccount.print_all()