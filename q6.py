class vehicle:
    def seating_capacity(self, capacity):
        print(f"The seating capacity of a vehicle is {capacity} passengers")

class bus(vehicle):
    def seating_capacity(self, capacity=50):
        print(f"The seating capacity of a bus is {capacity} passengers")
class car(vehicle):
    def seating_capacity(self, capacity=5):
        print(f"The seating capacity of a car is {capacity} passengers")

car1 = car()
car1.seating_capacity()
bus1 = bus()
bus1.seating_capacity()    