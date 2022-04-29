# used_cars.py
from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180) #Create a Car object with 180 units of fuel
    my_car.drive(30)  #Attempt to drive 30kms (180 - 30 = 150)
    print("fuel =", my_car.fuel)  # fuel = 150
    print("odo =", my_car.odometer)  # odeo = 30
    print(my_car) #print(my_car.___str__())     <--- not implement

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car)) # using f string