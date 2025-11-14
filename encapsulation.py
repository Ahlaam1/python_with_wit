class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BadBankAccount(0.0)
account.balance = -1

class BankAccount:
    def __init(self):
        self._balance = 0.0
    
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount >= self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -=amount




account = BankAccount()
print(account.balance)
