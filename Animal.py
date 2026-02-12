from abc import ABC,abstractmethod
class Animal(ABC):# class is blue print of real world objects or things 
    def __init__(self,weight , breed):
        self.breed=breed # initalizing values from arguments
        self.weight=weight
        
    @abstractmethod
    def eat(self):pass 
    
    @abstractmethod
    def sleep(self):pass
    
    
class Dog(Animal):
    
    def eat(self):
        print('The dog is eating dog food')
    
    def sleep(self):
        print('The Dog is sleeping in his Dog')
        
class Cat(Animal):
    
    def eat(self):
        print('The Cat is eating Cat food')
    
    def sleep(self):
        print('The cat is sleeping in his bed')
        
        
class Fish(Animal):
    
    def eat(self):
        print('The Fish is eating Fish food')
      
# Fish=Fish('Golden Fish', 2) Bceomes wrong since fish hasn't implemented fish method yet
Dog=Dog('Husky',12) # Is correct since ot has both implemntation of abstract methods ?
Dog.eat()