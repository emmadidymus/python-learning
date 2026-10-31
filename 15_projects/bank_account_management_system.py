class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance

    def __str__(self):
        return f"Account Holder:{self.account_holder}, Account Number: {self.account_number}, Balance:{self.__balance} "

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} has been deposited into your account")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdraw amount!")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn from your account")

    @property
    def balance(self):
        return self.__balance

    def transfer(self, amount):






account1 = BankAccount("Tobias", 10000001, 20000)
account2 = BankAccount("John", 10000002, 34000)




