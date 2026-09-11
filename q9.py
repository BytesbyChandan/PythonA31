class camera:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
class phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")
class smartphone(camera, phone):
    def __init__(self, brand, model):
        camera.__init__(self, brand, model)
        phone.__init__(self, brand, model)

    def display(self):
        camera.display(self)
        phone.display(self)

smartphone1 = smartphone("Apple", "iPhone 13")
smartphone1.display()