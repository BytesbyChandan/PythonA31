class account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}")

class savings_account(account):
    def __init__(self, interest_rate, account_number, balance):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def display(self):
        super().display()
        print(f"Interest Rate: {self.interest_rate}%")
s = savings_account(2.5, "123456789", 1000.00)
s.display()