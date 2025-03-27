class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print('Amount cannot be negative')

    def withdraw(self, deposit):
        if deposit <= self.__balance:
            self.__balance -= deposit
        else:
            print("Amount cannot be higher than balance")

    def get_balance(self):
        return f"You have {self.__balance} in your account"


account = BankAccount('Jan Kowalski', 10000)

account.deposit(500)
print(account.get_balance())

account.withdraw(11000)
