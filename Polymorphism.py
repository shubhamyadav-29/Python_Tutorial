<<<<<<< HEAD

#MethodOverloading 

class MathOperations:
    def add(self, a, b=0, c=0):
        # Default values for b and c to simulate overloading
        return a + b + c

# Creating an object of MathOperations class
math_obj = MathOperations()

# Calling add() with 2 arguments
result1 = math_obj.add(10, 5)
print(f"Result 1 (2 arguments): {result1}")  # Output: 15

# Calling add() with 3 arguments
result2 = math_obj.add(10, 5, 3)
print(f"Result 2 (3 arguments): {result2}")  # Output: 18

# Calling add() with 1 argument (using defaults for b and c)
result3 = math_obj.add(10)
print(f"Result 3 (1 argument): {result3}")  # Output: 10


#MethodOverriding

# Parent class
class Animal:
    def speak(self):
        print("The animal makes a sound")

# Child class 1 (Dog)
class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

# Child class 2 (Cat)
class Cat(Animal):
    def speak(self):
        print("Meow! Meow!")

# Creating objects of Dog and Cat
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the speak() method on different objects
animal.speak()  # Output: The animal makes a sound
dog.speak()     # Output: Woof! Woof!
cat.speak()     # Output: Meow! Meow!





    



  
    
=======

# #MethodOverloading 

# class MathOperations:
#     def add(self, a, b=0, c=0):
#         # Default values for b and c to simulate overloading
#         return a + b + c

# # Creating an object of MathOperations class
# math_obj = MathOperations()

# # Calling add() with 2 arguments
# result1 = math_obj.add(10, 5)
# print(f"Result 1 (2 arguments): {result1}")  # Output: 15

# # Calling add() with 3 arguments
# result2 = math_obj.add(10, 5, 3)
# print(f"Result 2 (3 arguments): {result2}")  # Output: 18

# # Calling add() with 1 argument (using defaults for b and c)
# result3 = math_obj.add(10)
# print(f"Result 3 (1 argument): {result3}")  # Output: 10


#MethodOverriding



class Mathss:
    def add(a ,c=0,b=0):

        return a+b+c
    

Math=Mathss()

print(Math.add(2,3))

print(Math.add(2,3,4))



    



  
    
>>>>>>> b59cf522c424fbf6a2d18df329f6d34c6480da25
