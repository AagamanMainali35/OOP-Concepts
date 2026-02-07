#Create a base class Product with attributes name and price. Create a child class DiscountedProduct that applies a discount.

class Product():
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
class DiscountedProduct(Product):
    def __init__(self,name,price,discount):
        Product.__init__(self,name,price)   
        self.discount=discount
        self.Discountedprice=self.price- int( self.price * self.discount/100 )
        
    def show_balnace(self):
        print(f'The original price is {self.price} and after {self.discount}% discount is {self.Discountedprice}')
        
    
Redbull=DiscountedProduct('redbull',100,10)
Redbull.show_balnace()