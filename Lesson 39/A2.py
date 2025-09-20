class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.accountno = acc

    def debit(self,amount):
        self.balance = self.balance - amount 
        print("Rs",amount,"from account number",self.accountno,"was debited")
        print("Total Balance is - ", self.get_bal())
    
    def credit(self,amount):
        self.balance = self.balance + amount
        print("Rs",amount,"from account number",self.accountno," was credited")
        print("Total Balance is - ", self.get_bal())
    
    def get_bal(self):
        return self.balance
    

acc1 = Account(100000, 482010)
acc1.debit(2010)

acc2 = Account(34890,987031)
acc2.credit(2004)

    