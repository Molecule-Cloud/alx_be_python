class BankAccount: 
    def __init__(self, intial_balance=0): 
        self.account_balance = intial_balance

    def deposit(self, amount) -> None:
            self.account_balance += amount

    def withdraw(self, amount):
            if amount > self.account_balance:
                return False
            self.account_balance -= amount
            return True
        
    def display_balance(self):
            print(f"Current Balance: ${self.account_balance}.00")

