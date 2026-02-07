class Electric():
    Total_charge=0
    def __init__(self):
        pass    
    
    def charge(self,Time):
        print(f'The car will take {self.Time} to charge fully at {Electric.Total_charge}')
        
class fuel():
    def __init__(self):
        pass
   
    def Refuel(self,time):
        print(f'The car will take {time} seconds to Fuel fully at {self.fuel_capacity} liters')
        
    
    
class Car(Electric,fuel):
    def __init__(self,Brand,Color,milage,speed,Cruise_control,seat,fuel_capacity):
        self.Brand=Brand
        self.Color=Color
        self.milage=milage
        self.speed=speed
        self.Cruise_control=Cruise_control
        self.seat=seat
        self.fuel_capacity=fuel_capacity
        
    def show_sepcs(self):
        pass
    
    def start(self):
        print(f'The car started')
        
    def stop(self):
        print('The car stopped')
   
Honda=Car('Honda','Green',42,130,True,2,500)
Honda.Refuel(100)
        
    