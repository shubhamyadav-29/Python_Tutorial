<<<<<<< HEAD
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # The balance is now private (can't be accessed directly)

    # Getter method to access balance
    def get_balance(self):
        return self.__balance

    # Setter method to update balance (controlled way)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")

# Create a BankAccount object
account = BankAccount(1000)

# Accessing the balance using getter method
print(account.get_balance())  # Output: 1000

# Deposit money using deposit method
account.deposit(500)
print(account.get_balance())  # Output: 1500

# Trying to withdraw more money than available
account.withdraw(2000)  # Output: Invalid withdrawal amount.


=======
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # The balance is now private (can't be accessed directly)

    # Getter method to access balance
    def get_balance(self):
        return self.__balance

    # Setter method to update balance (controlled way)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")

# Create a BankAccount object
account = BankAccount(1000)

# Accessing the balance using getter method
print(account.get_balance())  # Output: 1000

# Deposit money using deposit method
account.deposit(500)
print(account.get_balance())  # Output: 1500

# Trying to withdraw more money than available
account.withdraw(2000)  # Output: Invalid withdrawal amount.


>>>>>>> b59cf522c424fbf6a2d18df329f6d34c6480da25
