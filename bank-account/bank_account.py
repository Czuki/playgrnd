class BankAccount:
    def __init__(self):
        self.is_open = False
        self.balance = 0

    def get_balance(self):
        if not self.is_open:
            raise ValueError('Account is closed')
        return self.balance

    def open(self):
        if self.is_open:
            raise ValueError('Account is already open')
        self.is_open = True

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError('Account is closed')
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError('Deposit amount cannot be 0 or lower')

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError('Account is closed')
        if amount > self.balance:
            raise ValueError('Not enough funds')
        elif amount <= 0:
            raise ValueError('Withdraw amount must be more than 0')
        else:
            self.balance = self.balance - amount if amount < self.balance else self.balance - self.balance

    def close(self):
        if not self.is_open:
            raise ValueError('Account is already closed')
        self.is_open = False
        self.balance = 0


