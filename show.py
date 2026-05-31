from abc import ABC, abstractmethod

class Animal(ABC):
    
    def __init__(self,name,habitat):
        self.name = name
        self.habitat = habitat

    # Concrete method
    def display(self):
        print(f"Name: {self.name} | Habitat: {self.habitat}")

    # Abstract method
    @abstractmethod
    def speak(self):
        pass

# Child class 1-------------
class Dog(Animal):

    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat) # Call the parent class constructor
        self.breed = breed

    def speak(self):
        print(f"{self.name} ({self.breed}) says: Woof! Woof!")

# Child class 2-------------
class Parrot(Animal):
    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase
    
    def speak(self):
        print(f"{self.name} says: {self.phrase}! {self.phrase}!")
    

#Child class 3-------------
class Lion(Animal):
    def __init__(self,name,habitat,pride):
        super().__init__(name,habitat)
        self.pride = pride

    def speak(self):
        print(f"{self.name} (Pride: {self.pride}) says: Roar! Roar!")
    
#Create object and start the show

dog = Dog("Miko", "House", "Labrador")
parrot = Parrot("Zazu", "Jungle", "Squawk")
lion = Lion("Leonix", "Savannah", "Pride rock")

print("\n--- Animal sound Show ---")

for animal in (dog, parrot, lion):
    animal.display()
    animal.speak()
    print()