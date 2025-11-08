# String Operations Program

# 1 Create a string
text = "  Python Programming is Fun  "

# 2 Indexing and Slicing
print("First character:", text[2])          # P (indexing)
print("Slice (0 to 6):", text[2:8])         # Python
print("Last character:", text[-1])          # space

# 3 Basic Operations
print("Length of string:", len(text))       # total number of characters
print("'P' in text:", 'P' in text)          # True (membership)
print("'Java' not in text:", 'Java' not in text)  # True
print("Repeat text 2 times:", text * 2)     # repetition

# 4 String Methods
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Removed spaces:", text.strip())
print("Replace word:", text.replace("Fun", "Awesome"))
print("Count of 'n':", text.count("n"))
print("Find 'is':", text.find("is"))

# 5 String Formatting
name = "Anuj"
language = "Python"
print(f"My name is {name} and I am learning {language}.")  # f-string

# 6 Looping through the string
print("\nCharacters in string:")
for ch in language:
    print(ch, end=" ")

# 7 Immutability Example
original = "Hello"
# original[0] = 'J'   # This will cause an error
new_string = "J" + original[1:]  #  Correct way
print("\n\nAfter modifying:", new_string)
