from abc import ABC,abstractmethod

class user:
    def __int__(self,id,name):
        self.id=id
        self.name=name
        self._balance=0
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def set_balance(self,new_balance):
        if new_balance<0:
            print('Balnace cant be less Than 0 ')
        self._balance=new_balance
            
class Product(ABC):
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
        
    def __str__(self):
        return f'Instance of {self.name} serial no :({self.id})'
        
    @abstractmethod
    def get_price(self):
        pass
    @abstractmethod
    def details():
        pass
    
class Physical(Product):
    def __init__(self, id, name, Baseprice, weight):
        self.weight = weight
        self.Baseprice=Baseprice
        self.total=0
        flat_rate = 250
        extra_rate = 60
        if weight <= 4:
            self.shipping = flat_rate
        else:
            self.shipping = flat_rate + ((weight - 4) * extra_rate)

        self.total_price = self.Baseprice + self.shipping
        super().__init__(id, name, self.total_price)
        
    def get_price(self):
        return self.price
        
    def details(self):
        print("\n" + "="*40)
        print(f"Product Bill")
        print("="*40)
        print(f"Product ID     : {self.id}")
        print(f"Product Name   : {self.name}")
        print(f"Base Price     : ${self.Baseprice}")
        print(f"Weight         : {self.weight} kg")
        print(f"Shipping Cost  : ${self.shipping}")
        print("-"*40)
        print(f"Total Price    : ${self.get_price()}")
        print("="*40 + "\n")
   
class Digital(Product):
    def __init__(self, id, name, price, file_size):
        self.size = file_size  
        super().__init__(id, name, price)  

    def get_price(self):
        return self.price  

    def details(self):
        print("\n" + "="*40)
        print("Digital Product Bill")
        print("="*40)
        print(f"Product ID     : {self.id}")
        print(f"Product Name   : {self.name}")
        print(f"Price          : ${self.price}")
        print(f"File Size      : {self.size} MB")
        print("-"*40)
        print(f"Total Price    : ${self.get_price()}")
        print("="*40 + "\n")     

class Subscription(Product):
    def __init__(self, id, name, months):
        self.Monthlyprice=900
        price=self.Monthlyprice*months
        super().__init__(id, name, price)

    def get_price(self):
        return self.price
    
    def details(self):
        print("\n" + "="*40)
        print("Subscription Product Bill")
        print("="*40)
        print(f"Product ID     : {self.id}")
        print(f"Product Name   : {self.name}")
        print(f"Monthly Price  : {self.Monthlyprice} ")
        print(f"Price          : ${self.price}")
        print("="*40 + "\n")
        
class Cart():
    pass

class Checkout():
    pass

class Order():
    pass


s = Subscription("S1", "Netflix Plan", 3)
s.details()