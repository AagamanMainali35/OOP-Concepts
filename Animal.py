class Animal:# class is blue print of real world objects or things 
    def __init__(self,weight , breed):
        self.breed=breed # initalizing values from arguments
        self.weight=weight

    def eat(self):print(f'The animal is eating') # class can have many methods that defines its actions such as sleep or eat 
    
    def sleep(self):print(f'The animal is sleeping') 
    
    def define(self):
        print(f'the animal is of {self.breed}, and its weight is  {self.weight}')
    
# Dog=Animal(12,'Husky') # passing arguments to constructor 
# Dog.define()

    
        