# name = str(input("Enter your name :"))
# age= int(input("Enter your age "))

# print(f" my name is {name}\n my age is {age}")


# lst=['apple','mango','orange','banana','strawberry']

# for fruit in lst:
#     print(fruit.upper())

# def square(num):
#     a = num*num
#     print(a)

# square(7)

numbers=[]

for i in range(3):
    num = int(input(f"Enter number {i+1}:"))

numbers.append(num)

largest = max(numbers)
print("Largest number:",largest)


for num in numbers:
    if num>10:
        print(num)