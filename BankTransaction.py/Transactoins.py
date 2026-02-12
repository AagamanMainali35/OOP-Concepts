from abc import ABC, abstractmethod
class Account(ABC):
       
    def __init__(self):
        self.balance=0
        
    @abstractmethod
    def add_balance(self,AmountAdded):
        pass
        
    @abstractmethod
    def Withdraw(self,Amounttaken):
        pass
    
    @abstractmethod
    def showbalance(self):
        pass
        
    
class savings(Account):
    def __init__(self,SavingBalnace):
        super().__init__()
        self.SavingBalnace=SavingBalnace
        
    def claculate_intrest(self):
        self.SI = (self.SavingBalnace * self.rate * self.time) / 100
        
    def show_intrest(self):
        print(f'Interest added: {self.SI}')
        
    def add_balance(self,AmountAdded):
        self.SavingBalnace+=AmountAdded
        print(f'Added {AmountAdded}$ in saving blance the new balance is {self.SavingBalnace}$')
        
    def Withdraw(self,Amounttaken):
        self.SavingBalnace-=Amounttaken
        print('Sucessfuly withdrawn from saving account')
        
    def transfer(self,TransferAmount):
        self.balance+= self.SavingBalnace + TransferAmount
        print(f'Transferred {TransferAmount}$ to Checking Account')
        
    def showbalance(self):
        print(f'The Saving account balance is: {self.SavingBalnace}')
        

class Checking(Account):
    def __init__(self,currentBalance):
        super().__init__()
        self.currentBalance=currentBalance
    
    def add_balance(self,AmountAdded):
        self.currentBalance+=AmountAdded
        print(f'Added {AmountAdded}$ in current blance the new balance is {self.currentBalance}$')

    def Withdraw(self,Amounttaken):
        self.currentBalance-=Amounttaken
        print('Sucessfuly withdrawn from saving account')

    def showbalance(self):
        print(f'The current account balance is: {self.currentBalance}')
        
        
class AccountService():
    @staticmethod
    def Transfer(from_acc,to_acc,Amount):
        from_acc.Withdraw(Amount)
        to_acc.add_balance(Amount) 
        print(f'Transferred {Amount}$ from {from_acc} to {to_acc}')       
        
saving=savings(5000)
Check=Checking(10000)
saving.add_balance(1000)
saving.Withdraw(5000)
saving.showbalance()
Check.showbalance()
Check.add_balance(700)
AccountService.Transfer(saving,Check,1000)
saving.showbalance()
Check.showbalance()


        
        

    
        
        


        
        

        

