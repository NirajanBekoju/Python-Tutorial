class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name 
        self.balance = balance

    
    def viewBalance(self):
        print(f'Your balance is {self.balance}')