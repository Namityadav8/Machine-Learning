class Bank:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Amount {amount} is deposited in {self.owner}'s account and total balance now is {self.balance}")
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Amount {amount} has been deducted and remaining balance is {self.balance}")
    
bank = Bank('Raj',1000)
bank.deposit(500)
bank.withdraw(200)