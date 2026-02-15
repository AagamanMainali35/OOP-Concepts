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
        
    @abstractmethod
    def get_price(self):
        return self.price
    
class Physical(Product):
    def __init__(self, id, name, price, weight):
        self.weight = weight
        flat_rate = 250
        extra_rate = 60
        if weight <= 4:
            shipping = flat_rate
        else:
            shipping = flat_rate + ((weight - 4) * extra_rate)

        total_price = price + shipping
        super().__init__(id, name, total_price)
        

class Digital(Product):
    pass

class Subscription(Product):
    pass

class Cart():
    pass

class Checkout():
    pass

class Order():
    pass

