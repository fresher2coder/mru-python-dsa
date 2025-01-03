class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow! Meow!")

# Using polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
# Output:
# Woof! Woof!
# Meow! Meow!
