from abc import ABC,abstractmethod
from datetime import datetime
import string
import random
class User:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self._balance=0
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, new_balance):  # Changed from set_balance to balance
        if new_balance < 0:
            print('Balance cannot be less than 0')  # Fixed spelling
            return
        self._balance = new_balance
                  
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
        self.orderDatabase = {}  # Added


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
            
    # ---------------- Orders ----------------
    def add_order(self, order):
        self.orderDatabase[order.order_id] = order
        print(f"Order #{order.order_id} added for user: {order.customer.name}")
    
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
        self.cart_Items = {}
        self.cart_total = {}
        
    def add_item(self, user_id, product_id, quantity):
        user = db.get_user(user_id)
        product = db.get_product(product_id)
        
        if product is None or user is None:
            print('Invalid UserID or product ID provided')
            return
        
        if user_id not in self.cart_Items:
            self.cart_Items[user_id] = {}
            self.cart_total[user_id] = 0

        if product_id in self.cart_Items[user_id]:
            self.cart_Items[user_id][product_id] += quantity
            self.cart_total[user_id] += product.price * quantity
        else:
            self.cart_Items[user_id][product_id] = quantity
            self.cart_total[user_id] += product.price * quantity
           
    def showbill(self, user_id):
        user = db.get_user(user_id)

        if user is None:
            print("Invalid User ID")
            return

        if user_id not in self.cart_Items or not self.cart_Items[user_id]:
            print("Cart is empty")
            return

        print("\n------ BILL ------")

        for product_id, quantity in self.cart_Items[user_id].items():
            product = db.get_product(product_id)
            price = product.price
            subtotal = price * quantity
            print(f"{product.name} | Qty: {quantity} | Price: {price} | Subtotal: {subtotal}")

        print("------------------")
        print(f"TOTAL = {self.cart_total[user_id]}")
        
    def clearcart(self, user_id):
        if user_id in self.cart_Items:
            del self.cart_Items[user_id]
        if user_id in self.cart_total:
            del self.cart_total[user_id]
                    
    def get_total(self, user_id):
        if user_id not in self.cart_total:
            return 0
        return self.cart_total[user_id]

# Add after db initialization:
c = Cart()

class Checkout():
    def __init__(self, user_id):
        self.user = db.get_user(user_id)
        self.Cart_total = c.get_total(user_id) if self.user else 0
        
    def process(self):
        if not self.user:
            print('❌ User not found!')
            return False
        
        if self.Cart_total <= 0:
            print('❌ Your cart is empty!')
            return False
        
        if self.user.balance < self.Cart_total:
            print(f'❌ Insufficient funds! Balance: ${self.user.balance:.2f}, Needed: ${self.Cart_total:.2f}')
            return False

        print('✅ Processing items...')
        self.user.balance -= self.Cart_total
        print('📄 Creating Order Bill...')
        order_instance = Order(self.user, self.Cart_total)
        db.add_order(order_instance)
        return True

class Order():
    def __init__(self, user: User, Total_Amount):
        self.order_id = "".join(random.choices(string.ascii_letters + string.digits, k=9))
        self.customer = user
        self.Billtotal = Total_Amount
        self.dateProcessed = datetime.now().strftime("%Y%m%d%H%M%S")
        print(f"✅ ORDER SUCCESSFUL!")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"Order ID      : {self.order_id}")
        print(f"Customer      : {self.customer.name}")
        print(f"Total Amount  : ${self.Billtotal:.2f}")
        print(f"Date/Time     : {self.dateProcessed}")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"Thank you for your order, {self.customer.name}!")
        
    def __str__(self):
        return f'Order of {self.customer.name} made on {self.dateProcessed}'


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

        elif product_type.lower().strip() in ["subscription", "s"]:  # Fixed spelling
            months = float(input("Enter subscription period in months: "))
            s = Subscription(product_id, product_name, months)  # Create Subscription, not Physical
            db.add_product(s)
        else:
            print('Invalid Product Type')

    elif option == "3":
        db.show_products()

    elif option == "4":
        # Add Product to Cart
        pass

    elif option == "5":
        # Show Cart
        pass

    elif option == "6":
        # Checkout
        pass

    elif option == "7":
        print("Exiting...")
        break

    else:
        print("Invalid option! Please try again.")