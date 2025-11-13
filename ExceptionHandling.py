try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

except ValueError:
    print("Error: Please enter only numbers.")

else:
    print("Division successful!")

finally:
    print("Program execution completed.")
