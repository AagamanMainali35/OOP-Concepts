class Electric():
    Total_charge=0
    def __init__(self,Chargin_capacity=0):
        self.Chargin_capacity=Chargin_capacity
        
    def charge(self,Time):
        self.Time=Time
        print(f'The car will take {self.Time} minutes to charge fully at {self.Chargin_capacity}%')
        
class fuel():
    def __init__(self,fuel_capacity):
        self.fuel_capacity=fuel_capacity
        
    def Refuel(self):
        print(f'The car  has been Refueled fully at {self.fuel_capacity} liters')
         
class Car(Electric,fuel):
    def __init__(self,Brand,Color,milage,speed,Cruise_control,seat,Car_Type='Fuel',chargin_capacity=0,fuel_capacity=0):
        self.Brand=Brand
        self.Color=Color
        self.milage=milage
        self.speed=speed
        self.Cruise_control=Cruise_control
        self.seat=seat
        self.car_type=Car_Type
        
        if self.car_type.lower()=='fuel':
            fuel.__init__(self,fuel_capacity)
        elif self.car_type.lower()=='electric':
            Electric.__init__(self,chargin_capacity)
        else:            
            raise ValueError('Car Type can only be Elcetric or Fuel')
             
try:
    Car_Type=input(' What is the Car type ? : ')
    question=''
    Time=''
    if Car_Type.lower()=='fuel':
        question=' What is the current fuel level ? '
        Fuel_level=input(question) 
        Honda=Car('Honda','Green',42,130,True,2,Car_Type,fuel_capacity=Fuel_level)
        Honda.Refuel()  
    elif Car_Type.lower()=='electric':
        question=' whats is the Time to fully charge the vehicle ? '  
        Time=input(question)  
        Honda=Car('Honda','Green',42,130,True,2,Car_Type,100)
        Honda.charge(Time) 
    else:  
        raise ValueError(' Car type can only be Electric or Fuel ')
except ValueError as e:
    print(e)
        
    