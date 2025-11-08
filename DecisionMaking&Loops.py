age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


for i in range(1, 6):
    print("Number:", i)


count = 1
while count <= 5:
    print("Count:", count)
    count += 1




for i in range(10):
    if i == 5:
        break       # stop the loop
    if i % 2 == 0:
        continue    # skip even numbers
    print(i)
