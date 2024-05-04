class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")
        self.breed = breed

    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, color):
        super().__init__("Cat")
        self.color = color

    def speak(self):
        print("Meow!")

# Creating instances of the subclasses
dog = Dog("Labrador")
cat = Cat("Black")

# Accessing attributes and invoking methods
print(dog.species)  # Output: Dog
print(dog.breed)    # Output: Labrador
dog.speak()         # Output: Woof!

print(cat.species)  # Output: Cat
print(cat.color)    # Output: Black
cat.speak()         # Output: Meow!
