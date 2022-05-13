from taxi import Taxi

def main():
    #taxi(name,fuel,price per km)
    taxi = Taxi("Prui 1",100 ,1.23)
    #drive drive 40 km
    taxi.drive(40)
    #Print the taxi's detail and current fare
    print(taxi)
    print(f"Current fare : ${taxi.get_fare():.2f}")

    #Restart the meter (start a new fare ) and then drive the car 100 km
    taxi.start_fare() #  restart the current fare to 0
    print("===New trip ( before the taxi starts to drive)===")
    print(taxi)
    print(f"Current fare : ${taxi.get_fare():.2f}")

    autual_distance_driven = taxi.drive(100)
    print(f"After attempt to drive 100km...autual:{autual_distance_driven}") # it is 100km?

    #Print the detail and current fare
    print(taxi) #print(taxi.__str__())
    print(f"Current fare : ${taxi.get_fare():.2f}")
main()