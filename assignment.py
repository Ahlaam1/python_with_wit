class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("oh no customer, you can only deposit money")
        self.balance += amount
        print(f"Congratulations, {amount} deposited and safe with us. Thank you for banking with us")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Oh no client, you can only withdraw money")
        if amount >= self.balance:
            raise ValueError("You think you are wise abi?")
        self.balance -= amount
        print("Amount withdrawn, thank you for banking with us")

myaccount = BankAccount("Ahlaam", 5000)
myaccount.withdraw(300)
myaccount.deposit(10000)
        
