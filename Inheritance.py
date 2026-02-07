from Animal import Animal
 
class Cat(Animal): # Cat class inheritance from parent class named Animal
    def __init__(self):
        pass
    
    def meow(self):
        print(f'The cat meowed')
    

class Dog(Animal): # One parent can have multiple child so Animal is inherited by multiple Child 
    def __init__(self):
        pass
    
    def bark(self):
        print(f'The dog barked')
        

suzu=Cat() # creating an object of class 
subaru=Dog()

suzu.eat()
suzu.sleep() # Accesing its methods
suzu.meow()
subaru.eat()
subaru.sleep()
suzu.run() # AttributeError: 'Cat' object has no attribute 'run' since there is no run metjod in both object dan parent class

    