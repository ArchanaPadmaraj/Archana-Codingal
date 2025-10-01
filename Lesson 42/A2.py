class BankAccount:
    def __init__ (self,owner,balance):
        self.owner = owner
        self.__balance = balance
        # private attribute
    
    def getbalance (self):
        return self.__balance
    
    def deposit (self,amount):
        if amount > 0:
            self.__balance +=amount
            print(f"Deposited amount is {amount} and balance is {self.__balance}")
        else:
            print("Insufficient funds")
    
    def withdraw (self,amount):
        if 0<amount<=self.__balance:
            self.__balance-= amount
            print(f"withdrawn amount is {amount} and remaining balance is {self.__balance}")
        else:
            print("insufficient funds")

account = BankAccount("Archana", 109890)
print("account owner",account.owner)
print("inital balnce:",account.getbalance())
account.deposit(20103)
account.withdraw(10)
