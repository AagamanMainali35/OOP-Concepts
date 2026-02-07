#Create a base class Product with attributes name and price. Create a child class DiscountedProduct that applies a discount.

class Product(): # Creted base calss witha  variables
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
class DiscountedProduct(Product): # inherited the parent class 
    def __init__(self,name,price,discount): # added parameters to run main parent class constructor
        Product.__init__(self,name,price)   # called main parent class constructor and intialized argumets 
        self.discount=discount
        self.Discountedprice=self.price- int( self.price * self.discount/100 )
        
    def show_balnace(self): # Print the final balance 
        print(f'The original price is {self.price} and after {self.discount}% discount is {self.Discountedprice}')
        
    
Redbull=DiscountedProduct('redbull',100,10) # creatingg the object
Redbull.show_balnace() # show the fnial price 