class person:
    def __init__(self):
        self.__name = ""
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
p = person()
p.set_name("Alice")
print(p.get_name()) 

