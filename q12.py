class animal:
    def make_sound(self):
        print("Animal makes a sound")
class mammal:
    def make_sounds(self):
        print("Mammal makes a sound")
class dog(animal, mammal):
    def make_soundoo(self):
        animal.make_sound(self)
        mammal.make_sounds(self)  

d = dog()
d.make_soundoo()
