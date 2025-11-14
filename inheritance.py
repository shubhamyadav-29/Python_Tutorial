<<<<<<< HEAD
# Parent class (Superclass)
class Animal:
    def __init__(self, name):
        self.name = name  # All animals have a name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Child class (Subclass)
class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor (initializing name)
        self.breed = breed  # Add an additional attribute for breed

    def bark(self):
        print(f"{self.name} is barking!")

# Creating objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

# Calling methods from both parent and child class
dog1.eat()       # Inherited from Animal class
dog1.sleep()     # Inherited from Animal class
dog1.bark()      # Defined in Dog class

dog2.eat()       # Inherited from Animal class
dog2.bark()      # Defined in Dog class
=======
# Parent class (Superclass)
class Animal:
    def __init__(self, name):
        self.name = name  # All animals have a name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Child class (Subclass)
class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor (initializing name)
        self.breed = breed  # Add an additional attribute for breed

    def bark(self):
        print(f"{self.name} is barking!")

# Creating objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

# Calling methods from both parent and child class
dog1.eat()       # Inherited from Animal class
dog1.sleep()     # Inherited from Animal class
dog1.bark()      # Defined in Dog class

dog2.eat()       # Inherited from Animal class
dog2.bark()      # Defined in Dog class
>>>>>>> b59cf522c424fbf6a2d18df329f6d34c6480da25
