class vehicle:
    def __init__(Self, brand, speed):
        Self.brand = brand
        Self.speed = speed
    def display(Self):
        print("Brand:", Self.brand)
        print("Speed:", Self.speed)
class car(vehicle):
    def __init__(Self, fuel_type, brand, speed):
        super().__init__(brand, speed)
        Self.fuel_type = fuel_type
    def display(Self):
        super().display()
        print("Fuel Type:", Self.fuel_type)
c = car("Petrol", "Toyota", 120)
c.display()