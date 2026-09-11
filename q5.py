class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass
class dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def make_sound(self):
        return "Woof!"

dog = dog("Buddy", "Canine", "Golden Retriever")
print(f"Name: {dog.name}, Species: {dog.species}, Breed: {
dog.breed}, Sound: {dog.make_sound()}") 