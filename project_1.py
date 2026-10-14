# Project: Fundamental Booster #
# ============================ #



print("Welcome to the Interactive Personal Data Collector!")
print("Please enter your personal information below.\n")


name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favourite_number = int(input("Please enter your favourite number: "))

age_float = float(age)
height_int = int(height)

current_year = 2026
birth_year = current_year - age

print("\nThank you! Here is the information we collected:\n")

# Display variable values, types, and memory addresses
print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {favourite_number} "
      f"(Type: {type(favourite_number)}, "
      f"Memory Address: {id(favourite_number)})")

print(f"\nYour birth year is approximately: {birth_year} "
      f"(based on your age of {age})")

print("\nType Conversion Examples:")
print(f"Age converted to float: {age_float}")
print(f"Height converted to integer: {height_int}")

print("\nUser Summary:")
print("Hello, " + name + "! Your favourite number is "
      + str(favourite_number) + ".")

print("\nThank you for using the Personal Data Collector. Goodbye!")