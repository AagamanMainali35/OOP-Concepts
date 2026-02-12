from abc import ABC, abstractmethod

# Abstract Engine class
class Engine(ABC):
    @abstractmethod
    def operate(self):
        pass


# Electric engine
class Electric(Engine):
    def __init__(self, charging_capacity):
        self.charging_capacity = charging_capacity

    def operate(self):
        print(f'The car is charging at {self.charging_capacity}%')


# Fuel engine
class Fuel(Engine):
    def __init__(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity

    def operate(self):
        print(f'The car has been refueled fully at {self.fuel_capacity} liters')


# Car class
class Car:
    def __init__(self, brand, color, mileage, speed, cruise_control, seats, engine: Engine):
        self.brand = brand
        self.color = color
        self.mileage = mileage
        self.speed = speed
        self.cruise_control = cruise_control
        self.seats = seats
        self.engine = engine

    def operate_engine(self):
        self.engine.operate()


# Example usage
car_type = input("What is the car type? (fuel/electric): ").lower()

if car_type == 'fuel':
    fuel_level = int(input("What is the current fuel level? "))
    engine = Fuel(fuel_level)
elif car_type == 'electric':
    charge_capacity = int(input("What is the charging capacity? "))
    engine = Electric(charge_capacity)
else:
    raise ValueError("Car type can only be Fuel or Electric")

honda = Car("Honda", "Green", 42, 130, True, 2, engine)
honda.operate_engine()
