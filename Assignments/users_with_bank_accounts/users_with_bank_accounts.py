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

class User:
    all_users = []
    def __init__(self, first_name, email):
        self.first_name = first_name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        User.all_users.append(self)

    @classmethod
    def print_all_users(cls):
        for individual_user in cls.all_users:
            individual_user.display_info()
            

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.email}")
        self.account.display_account_info()
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self

user1 = User("Katie","katie@gmail.com")
user1.make_deposit(90)
user1.make_withdraw(50)


User.print_all_users()


# BankAccount.print_all()

