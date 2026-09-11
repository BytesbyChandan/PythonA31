class temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def set_temperature(self, celsius):
        self.celsius = celsius
    def convert_to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

t = temperature(25)
print(t.convert_to_fahrenheit())