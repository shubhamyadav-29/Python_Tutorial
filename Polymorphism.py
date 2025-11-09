
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



    



  
    
