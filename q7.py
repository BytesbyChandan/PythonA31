class car:
    def __init__(self, __speed):
        self.__speed = __speed
    def set_speed(self, speed):
        if speed <=200:
            self.__speed = speed
    def get_speed(self):
        return self.__speed

c = car(100)
print(c.get_speed())