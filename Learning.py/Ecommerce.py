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

class DB:
    def __init__(self):
        self.productDatabase = {}  
        self.userDatabase = {}     

    # ---------------- Products ----------------
    def add_product(self, product):
        self.productDatabase[product.id] = product
        print(f"Product '{product.name}' added with ID: {product.id}")

    def show_products(self):
        if not self.productDatabase:
            print("No products in database.")
            return
        print("\nAvailable Products:")
        for prod in self.productDatabase.values():
            print(f"{prod.id} - {prod.name} - ${prod.get_price()}")
       
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
    def __init__(self):
        self.cart_Items={}
        self.cart_total=0
        
    def add_item(self,user_id,product_id,quantity):
        user=db.get_user(user_id)
        product=db.get_product(product_id)
        total+=product.price * int(quantity)
        print(total)
        print(user.balance)
        if product is None or user is None:
           print('Invalid UserID or product ID provided')
        if user_id not in self.cart_Items:
            self.cart_Items[user_id] = {}
        if product_id in self.cart_Items[user_id]:
            self.cart_Items[user_id][product_id] += quantity
        else:
            self.cart_Items[user_id][product_id] = quantity
        
    def clearcart(self,user_id):    
        try:
            del self.cart_Items[user_id]
        except Exception as e:
            print(e)
    
    def ListItems(self):
        print(self.cart_Items)

        
    
class Checkout():
    pass

class Order():
    pass


db=DB()
c = Cart()

db.add_user(User("U101","Aagaman"))
db.add_user(User("U102","Ram"))
db.add_user(User("U103","Sita"))
db.add_user(User("U104","Hari"))
db.add_user(User("U105","Gita"))
db.add_product(Physical("P101","Laptop",1200,5))
db.add_product(Physical("P102","Keyboard",50,1))
db.add_product(Physical("P103","Monitor",300,4))
db.add_product(Physical("P104","Chair",200,7))
db.add_product(Digital("D101","Python Course",50,200))
db.add_product(Digital("D102","Django Course",70,300))
db.add_product(Digital("D103","React Course",60,250))
db.add_product(Subscription("S101","Netflix Plan",3))
db.add_product(Subscription("S102","Gym Membership",6))
db.add_product(Subscription("S103","Cloud Storage",12))


while True:
    print("\n===== MENU =====")
    print("1 Add User")
    print("2 Add Product")
    print("3 Show Products")
    print("4 Add Product to Cart")
    print("5 Show Cart")
    print("6 Clear Cart")
    print("7 Checkout")
    print(" Exit")

    option = input('Enter Your option: ').lower().strip()

    if option == "1":
        name = input('Enter Name: ')
        id = input('Enter ID: ')
        u = User(id, name)
        db.add_user(u)
        db.show_users()

    elif option == "2":
        product_id = input("Enter Product ID: ")
        product_name = input("Enter Product Name: ")
        product_price=int(input("Enter the product Price: "))
        product_type = input("Enter Product Type Physical(p), Digital(d) or Subscription(s) : ").lower().strip()

        if product_type.lower().strip()=="digital" or product_type.lower().strip()=="d":
            file_size = float(input("Enter File size in mb: "))
            d=Digital(product_id,product_name,product_price,file_size)
            db.add_product(d)
        elif product_type.lower().strip()=="physical" or product_type.lower().strip()=="p":
            product_weight = float(input("Enter Product Weight in kg: "))
            p=Physical(product_id,product_name,product_price,product_weight)
            db.add_product(p)

        elif product_type.lower().strip()=="subcription" or product_type.lower().strip()=="s'":
            Months = float(input("Enter subscription period in months:"))
            p=Physical(product_id,product_name,product_price,product_weight)
            db.add_product(p)
        else: 
            print('Invalid Product Type')

    elif option == "3":
        db.show_products()

    elif option == "4":
        user_id = input("Enter User ID: ").strip()
        while True:
            product_id = input("Enter Product ID: ").strip()
            quantity = int(input("Enter Product quantity: "))
            c.add_item(user_id, product_id, quantity)
            more = input("Add more Product?(yes/no) ")
            if more.lower().strip() == "no":
                break
            
    elif option == "5":
        c.ListItems()
        
    elif option == "6":
        id=input('Insert Your userID : ')
        c.clearcart(id)
    
    elif option == "7":
        # Checkout
        pass

    elif option == "8":
        print("Exiting...")
        break

    else:
        print("Invalid option! Please try again.")
        
        
    