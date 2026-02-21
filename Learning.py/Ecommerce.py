from abc import ABC,abstractmethod
   
class User:
    def __init__(self,id,name):
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
    
# class DB:
#     def __init__(self):
#         self.Proddatabase={}
#         self.userDatabase={}
        
        
#     def add_product(self,product:Product):
#         self.database[product.id]=product
    
#     def show_products(self):
#         for key,data in self.database.items():
#             print(key,data)
    
#     def get_product(self,id):
#         pass
    
#     def remove(product,id):
#         pass


class DB:
    def __init__(self):
        self.productDatabase = {}  
        self.userDatabase = {}     

    # ---------------- Products ----------------
    def add_product(self, product):
        self.productDatabase[product.id] = product
        print(f"Product '{product.name}' added with ID: {product.id}")

    def show_products(self):
        for key,data in self.database.items():
            print(key,data)
       
    def get_product(self, prod_id):
        return self.productDatabase.get(prod_id, None)

    def remove_product(self, prod_id):
        if prod_id in self.productDatabase:
            removed = self.productDatabase.pop(prod_id)
            print(f"Product '{removed.name}' removed from database.")
        else:
            print("Product ID not found.")

    # ---------------- Users ----------------
    def add_user(self, user):
        self.userDatabase[user.id] = user
        print(f"User '{user.name}' added with ID: {user.id}")

    def show_users(self):
        for value in self.userDatabase.values():
            print(value)

    def get_user(self, user_id):
        return self.userDatabase.get(user_id, None)

    def remove_user(self, user_id):
        if user_id in self.userDatabase:
            removed = self.userDatabase.pop(user_id)
            print(f"User '{removed.name}' removed from database.")
        else:
            print("User ID not found.")
    
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
p1 = Physical("P1", "Custom Printer", 1430, 7)
p1 = Physical("P1", "Custom Printer", 1430, 7)

db=DB()
while True:
    print("\n===== MENU =====")
    print("1 Add User")
    print("2 Add Product")
    print("3 Show Products")
    print("4 Add Product to Cart")
    print("5 Show Cart")
    print("6 Checkout")
    print("7 Exit")
    option=input('Enter Your option : ')
    if option.lower().strip()=="1":
        name=input('Enter Name : ')
        id=input('Enter ID : ')
        u=User(id,name)
        db.add_user(u)
        db.show_users()
    break
        
        
    