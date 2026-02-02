class Account:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer
        print(f"Customer {customer.name} added to {self.bank_name}.")

    def get_total_bank_assets(self):
        total = 0
        for customer in self.customers.values():
            for account in customer.accounts.values():
                total += account.balance
        return total

# --- Simulation ---

# 1. Setup the Bank
my_bank = Bank("Global Trust Bank")

# 2. Setup a Customer
sarah = Customer("Sarah Jenkins", "CUST001")
my_bank.add_customer(sarah)

# 3. Create and assign an Account
sarah_savings = Account("ACT-9988", 1000)
sarah.add_account(sarah_savings)

# 4. Perform Transactions
sarah_savings.deposit(500)
sarah_savings.withdraw(200)

# 5. Check Bank-wide Status
print(f"Total Bank Assets: ${my_bank.get_total_bank_assets()}")