class Account:
        def __init__(self,name,balance,minimumbalance):
                self.name=name
                self.balance=balance
                self.minimumbalance
                 
        def deposit(self,money):
                currentbalance=self.balance+money
                return currentbalance
         
        def withdraw(self,money):
                currentbalance=self.balance-money
                return currentbalance
         
        def enquirey(self):
                return self.balance
                 
        def current(self):
                current=self.balance
                print("current balance",current)
         
        def saving(self):
                save=self.balance
                print("saving balanc",save)
                 
class Current(Account):
        def __init__(self,name,balance,minimumbalance):
                self.name=name
                self.balance=balance
                self.minimumbalance=minimumbalance
         
        def check(self):
                super().current()
class Savings(Account):
        def __init__(self,name,balance,minimumbalance):
                self.name=name
                self.balance=balance
                self.minimumbalance=minimumbalance
                 
        def save(self):
                super().saving()
         
name=input("enter account holder name : ")
dm=int(input("enter deposit money : "))
wm=int(input("enter withdraw money : "))        
 
c=Current(name,1000,100)
print("deposite Money",c.deposit(dm))
print("withdraw Money",c.withdraw(wm))
c.check()
 
s=Savings(name,1000,100)
s.save()
