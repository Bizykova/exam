class Account:

    def __init__(self, accountName, phone, email, balance):
        self.accountName = accountName
        self.phone = phone
        self.email = email
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, Account):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return self.balance + other
        raise
