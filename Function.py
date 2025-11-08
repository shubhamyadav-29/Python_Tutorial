def greet(name):
    print("Hello,", name)

greet("shubham")


def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)


def intro(name, country="India"):
    print("My name is", name, "and I am from", country)

intro("Anuj")
intro("John", "USA")



square = lambda x: x * x
print(square(5))   # 25
